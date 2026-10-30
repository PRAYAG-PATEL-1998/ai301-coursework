# AI301 toolkit: reusable on any project

This folder is a working snapshot of the tools I built in AI301 (units 1 to 7),
with an installer. Copy it to a new computer, run one command, and every tool
works on any repo. Snapshot date: 2026-10-29.

## Install in one command

```bash
python3 tools/toolkit/install_toolkit.py              # into ~/.claude
python3 tools/toolkit/install_toolkit.py --dry-run    # show changes first
python3 tools/toolkit/install_toolkit.py --repo <path to a clone>   # also prepare a project
```

- Safe to run twice. Files it overwrites are copied first to `~/.claude/_backup-toolkit-<date>/`.
- It never overwrites my voice guide if one exists.
- Skills that already exist are skipped. Use `--force` to replace them.
- Quit any open `claude` session afterwards. Hooks load only when a session starts.
- Needs Python 3.8+, `git`, `gh` (logged in with `gh auth login`) and Claude Code.

## What is inside

| Folder | What it is | Used for |
|---|---|---|
| `skills/issue-scout` | Searches GitHub with my queries, ranks for free, grades the top 5 | Finding and grading issues |
| `skills/issue-select` | The unit 1 grader (my rubric) | Grading one issue |
| `skills/repro-check` | Grades a claim comment and a repro report | Before posting a claim |
| `skills/plan-check` | Grades a fix plan and a plan comment | Before building |
| `skills/pr-precheck` | Grades a branch, plan, evidence and PR text | Before opening a PR |
| `voice-guard/` | Hook: checks every comment and PR body against my voice guide | Runs on `gh issue comment` and `gh pr create` |
| `ship-gate/` | Hook: runs the repo's own checks, then pr-precheck, before a PR opens | Runs on `gh pr create` |
| `templates/` | `ship-manifest-template.md`, `claude-local-template.md`, `voice-guide-upstream.md` | Per-project files |

The folders `tools/issue-select`, `tools/repro-check`, `tools/plan-check` and
`tools/pr-precheck` next to this one are the versions I submitted for the course.
`tools/toolkit/skills/` holds the versions I actually use now (real-repo scopes).

## Using it on a new project

1. **Pick an issue.** `claude "issue-scout: run a scan"` or `claude "issue-scout: grade <issue URL>"`.
   Read every comment first: if anyone asked to work on it, it is taken. Read `CONTRIBUTING.md` and any AI policy.
2. **Claim it.** Write `claim-draft.md` (intent, a first step, when I will report back). Check it:
   `claude "repro-check: grade my draft claim comment in claim-draft.md for issue <URL>"`.
   Post it through Claude Code so the voice guard checks it:
   `claude "run this command: gh issue comment <URL> --body-file claim-draft.md"`.
3. **Prepare the clone.** Fork, clone, then `python3 tools/toolkit/install_toolkit.py --repo <clone>`.
   It creates `ship-manifest.md` and `CLAUDE.local.md` and keeps my working files out of commits.
   Fill in the manifest (2 to 4 of the repo's own checks, each with its command and source).
   Follow `CLAUDE.local.md` to write the repo memory file.
4. **Reproduce, plan, build.** Write `repro-draft.md`, then `plan.md` and `plan-comment.md`:
   `claude "plan-check: grade my plan in plan.md and draft comment in plan-comment.md for issue <URL>"`.
   Build on a branch, with a test that fails without the fix. Save before and after output in `test_evidence.md`.
5. **Ship.** Write `pr_draft.md`. Run by hand until it says PASS:
   `python3 ~/.claude/ship-gate/check_gate.py --branch --title "<title>" --body-file pr_draft.md`.
   Then `git push -u origin <branch>`, `gh repo set-default <owner>/<repo>`, and
   `claude "run this command: gh pr create --title '<title>' --body-file pr_draft.md"`.

## Rules I learned (keep them)

- A stranger's claim stands, even with no assignee. First claim stands, theirs or mine.
- Promise a first step, not a finish line. Ping once, on the repo's clock.
- Read the repo's AI policy before choosing it. Disclose AI use as the repo asks.
- Check the current code before choosing an old issue: it may already be fixed.
- Check that outsiders can open PRs (some repos close fork PRs) and that PRs get answered.
- The scout's `unclaimed` check counts my own claim comment as a claim. Read the thread myself.

## What is NOT here, on purpose

- Logs (`guard-log.md`, `gate-log.md`), `settings.local.json` and backups: they stay on my computer.
- Scan history (`scan-output.md`, `scan-notes.md`) is in `skills/issue-scout/` as a record. The installer does not copy it.

## Costs and limits

- The voice guard and the ship-gate call `claude` (Sonnet) to check text: a few cents per check.
- A scout grade is about $0.20 per issue. A scan is about $1.
- Hooks fire for any repo when installed in `~/.claude/settings.json`. To limit them to one repo,
  install with `--claude-dir` into that repo's own `.claude` folder, or move the two hook entries
  into that repo's `.claude/settings.local.json`.
