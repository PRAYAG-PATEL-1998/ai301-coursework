# Evidence guide: where proof lives in a reproduction package

## Environment

**Where it lives:** In an eval bundle, compare the repo-facts block's stated version/OS and the issue context's own version report against the repro report's Environment line (usually the first line of the report). In live mode, compare the issue thread's reported version against the draft repro report's Environment line.

**What good looks like:** It names the exact tool version, OS, and — for a compiled language — the commit or build info the repo's own bug template asks for, and it matches the issue's stated version or explicitly says why it doesn't (for example, confirming the bug still reproduces on a newer tag than the one in the original report).

## Steps

**Where it lives:** The repro report's ordered steps, read starting from a fresh clone of the repo at the pinned version named in the Environment line.

**What good looks like:** Every step is a concrete, executable action — a command, a specific file, a specific input — never a vague gesture like "set up the project" or "ran the tool on a file." A stranger with only the repo's README and CONTRIBUTING could execute the same sequence and land on the same starting state before the bug triggers.

## Behavior shown

**Where it lives:** The artifact block in the repro report — a terminal log excerpt, error output, or a described screenshot — read against the specific error or behavior the issue names in its own body.

**What good looks like:** The artifact shows the exact behavior the issue describes: the same error message or exit code, the same symptom, not a superficially similar but different failure (a config error standing in for a panic is a fail, not a pass). Expected vs. actual is stated explicitly, not left implied.

## Honesty

**Where it lives:** The report's concluding claim (its verdict on itself: "reproduced," "could not reproduce," "partially reproduced, here's what differs") read against what the artifact quoted above it actually demonstrates.

**What good looks like:** The claim never outruns its own evidence. An honest, evidenced "could not reproduce on v1.20.0, tried X and Y" is a full pass — a cannot-reproduce is a valid, postable outcome. A confident "reproduced!" resting on a mismatched, missing, or vague artifact is not, no matter how well-formatted the write-up is.

## Comms

**Where it lives:** The claim comment's own wording, read against the issue it answers; and both comments read against the repo's stated conventions — CONTRIBUTING, issue/PR templates, and any AI-assistance disclosure requirement — found in the repo-facts block (eval mode) or on GitHub itself (live mode, via `scope.md`'s house rules and the repo's own docs).

**What good looks like:** The claim comment names the specific behavior or scenario from the issue (never "this bug"), specific enough that it couldn't be mistaken for a claim on a different issue, and promises the next artifact — a report — rather than a fix timeline or a merge. A version number is one way to be specific, but isn't required by itself when the issue isn't version-scoped (for example, a bug the issue says "applies to all" versions) — what matters is that the named scenario is unambiguous. Both comments follow whatever the repo's own conventions actually require, including disclosing AI assistance where the repo's policy asks for it, and read as this contributor's own specific words rather than interchangeable boilerplate that could be pasted onto any issue.
