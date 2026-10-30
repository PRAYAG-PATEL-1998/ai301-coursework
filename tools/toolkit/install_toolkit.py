#!/usr/bin/env python3
"""Install the AI301 toolkit on this computer, for any project.

What it installs (all from the folders next to this file):
  skills/       issue-scout, issue-select, repro-check, plan-check, pr-precheck
  voice-guard/  the voice guard (checks your comments and PR text before they post)
  ship-gate/    the ship-gate (checks a branch before a PR opens)
  hooks         one entry each for the voice guard and the ship-gate, in settings.json

Usage:
  python3 install_toolkit.py                  install into ~/.claude
  python3 install_toolkit.py --dry-run        show what would change, change nothing
  python3 install_toolkit.py --repo <clone>   also prepare a project clone (manifest + excludes)
  python3 install_toolkit.py --claude-dir D   install into another folder named .claude
  python3 install_toolkit.py --force          overwrite skills that already exist

Safe to run twice. Anything it overwrites is copied first to
<claude dir>/_backup-toolkit-<date>/. It never overwrites your voice guide
if you already have one.
"""
import argparse
import datetime
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
POINTER = "My voice guide now lives at ~/.claude/voice-guard/voice-guide.md; read it there.\n"
SKIP_ON_INSTALL = {"scan-output.md", "scan-notes.md"}  # personal scan history stays in the repo only
EXCLUDES = ["ship-manifest.md", "plan.md", "plan-comment.md", "test_evidence.md", "pr_draft.md",
            "repro-draft.md", "claim-draft.md", "CLAUDE.local.md"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--claude-dir")
    ap.add_argument("--repo")
    a = ap.parse_args()

    claude = Path(a.claude_dir).expanduser().resolve() if a.claude_dir else Path.home() / ".claude"
    if claude.name != ".claude":
        sys.exit("toolkit: the install folder must be named .claude (the ship-gate checks this). Nothing changed.")
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = claude / f"_backup-toolkit-{stamp}"
    dry = a.dry_run

    def say(msg):
        print(("[dry-run] " if dry else "") + "toolkit: " + msg)

    def save_backup(path):
        if not path.exists():
            return
        dest = backup / path.relative_to(claude)
        say(f"backup {path} -> {dest}")
        if not dry:
            dest.parent.mkdir(parents=True, exist_ok=True)
            if path.is_dir():
                shutil.copytree(path, dest, dirs_exist_ok=True)
            else:
                shutil.copy2(path, dest)

    def put(src, dst):
        if dst.exists() and dst.read_bytes() == src.read_bytes():
            return False
        save_backup(dst)
        say(f"write {dst}")
        if not dry:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        return True

    # 1. voice guard: scripts always, the guide only if you have none
    vg = claude / "voice-guard"
    for name in ("check_voice.py", "hooks-settings.json"):
        put(HERE / "voice-guard" / name, vg / name)
    guide = vg / "voice-guide.md"
    if guide.exists():
        say(f"keep your voice guide: {guide}")
    else:
        put(HERE / "voice-guard" / "voice-guide.md", guide)

    # 2. ship-gate files
    for src in sorted((HERE / "ship-gate").iterdir()):
        if src.is_file():
            put(src, claude / "ship-gate" / src.name)

    # 3. skills (skipped when they exist, unless --force)
    for sk in sorted((HERE / "skills").iterdir()):
        if not sk.is_dir():
            continue
        dst = claude / "skills" / sk.name
        if dst.exists() and not a.force:
            say(f"skill {sk.name} already installed (use --force to overwrite)")
            continue
        if dst.exists():
            save_backup(dst)
        say(f"install skill {sk.name}")
        if not dry:
            shutil.copytree(sk, dst, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns(*SKIP_ON_INSTALL))
    # one guide: the three checking skills read the voice guard's guide through a pointer line
    for sk in ("repro-check", "plan-check", "pr-precheck"):
        vgfile = claude / "skills" / sk / "voice-guide.md"
        if (claude / "skills" / sk).exists() and (not vgfile.exists() or vgfile.read_text(encoding="utf-8") != POINTER):
            save_backup(vgfile)
            say(f"pointer to the one voice guide in {sk}")
            if not dry:
                vgfile.write_text(POINTER, encoding="utf-8")

    # 4. hooks in settings.json
    settings = claude / "settings.json"
    try:
        data = json.loads(settings.read_text(encoding="utf-8")) if settings.is_file() and settings.read_text(encoding="utf-8").strip() else {}
    except ValueError as e:
        sys.exit(f"toolkit: {settings} is not valid JSON ({e}). Fix it first. Nothing was changed in settings.")
    hooks = data.setdefault("hooks", {})
    pre = hooks.setdefault("PreToolUse", [])
    added = []
    for marker, rel in (("voice-guard/check_voice.py", "voice-guard"), ("ship-gate/check_gate.py", "ship-gate")):
        if any(marker in h.get("command", "") for e in pre for h in e.get("hooks", [])):
            continue
        block = json.loads((HERE / rel / "hooks-settings.json").read_text(encoding="utf-8"))
        for e in block["hooks"]["PreToolUse"]:
            for h in e["hooks"]:
                h["command"] = (h["command"].replace('$HOME/.claude', str(claude).replace("\\", "/"))
                                .replace("$HOME", str(Path.home()).replace("\\", "/")))
            pre.append(e)
        added.append(rel)
    if added:
        save_backup(settings)
        say("add hooks to settings.json: " + ", ".join(added))
        if not dry:
            settings.write_text(json.dumps(data, indent=2), encoding="utf-8")
    else:
        say("hooks already in settings.json")

    # 5. a project clone: manifest, memory template, excludes
    if a.repo:
        repo = Path(a.repo).expanduser().resolve()
        if not (repo / ".git").is_dir():
            sys.exit(f"toolkit: {repo} is not the top folder of a git clone. The rest was installed.")
        for src, name in ((HERE / "templates" / "ship-manifest-template.md", "ship-manifest.md"),
                          (HERE / "templates" / "claude-local-template.md", "CLAUDE.local.md")):
            if not (repo / name).exists():
                say(f"create {repo / name}")
                if not dry:
                    shutil.copy2(src, repo / name)
        ex = repo / ".git" / "info" / "exclude"
        have = ex.read_text(encoding="utf-8").split() if ex.exists() else []
        new = [x for x in EXCLUDES if x not in have]
        if new:
            say("exclude from commits: " + ", ".join(new))
            if not dry:
                ex.parent.mkdir(parents=True, exist_ok=True)
                with ex.open("a", encoding="utf-8") as f:
                    f.write("\n".join(new) + "\n")
    say("done. Quit any open claude session: hooks load only when a session starts.")


if __name__ == "__main__":
    main()
