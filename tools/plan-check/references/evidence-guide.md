# Evidence guide: where evidence lives in a plan package

An eval package is one markdown file with these sections, in order: `## Repo facts`, `## Issue`, `## Thread highlights`, `## Repro evidence`, `## Candidate plan`, `## Candidate plan comment`. Live mode maps to the same pieces: the repo's CONTRIBUTING and AI policy (read with `gh api repos/<owner>/<repo>/contents/CONTRIBUTING.md`, plus any AI policy file it names); the issue and its comments (`gh issue view <url> --comments`); the student's posted repro comment on that issue (this is the Repro evidence block); `plan.md` (the Candidate plan); and the draft comment file (the Candidate plan comment). In live mode, grade only what those drafts contain and quote.

## Diagnosis and grounding

- Where it lives: the cause is in the plan's `Diagnosis` section (or the first lines of the plan). The behavior it must explain is in `## Repro evidence`: the numbered `Steps`, the `Control runs` (or runs with a component off, disabled, or bypassed), and the `Actual` paragraph.
- What good looks like: the cause names a component that the repro's own results point at, and every step and control is what that cause would produce. Bad looks like: the repro shows the failure persisting with the suspected component removed or bypassed; or a plan that starts "as identified in the thread" and the repro never tests it. A polished or confident Diagnosis is not evidence.

## Scope

- Where it lives: the plan's `Scope` section (an in-scope statement and a not-in-scope line) and its list of `Changes` or `Approach` steps.
- What good looks like: one failing behavior, one named place to change, a not-in line that names things left out, and each change listed is needed to stop that behavior. Smaller than the issue is fine when the plan says what it defers. Bad looks like: a fix plus a rename, config migration, new option, state-machine or printer rewrite, module restructure, or port to a sibling feature.

## Executability

- Where it lives: `Changes`/`Approach` and any `Files` list in the Candidate plan.
- What good looks like: a named file, module, or code path and the chosen way to change each, so a stranger could open it and start; the exact function may be left to tracing. If the location or the approach itself is undecided, it is not executable. Bad looks like: "somewhere", "upstream or vendored, whichever is easier", "investigate", "maybe also check", "not sure which layer"; no files named.

## Test plan

- Where it lives: the plan's `Test plan` section, read next to the repro steps in `## Repro evidence`.
- What good looks like: the repro's own command or action re-run with a specific expected result after the fix (an exit code, a number, a visible output), something that would look different if the fix failed. Bad looks like: "should feel fast", "nothing else should feel broken", "run the full test suite" with no outcome named for this fix.

## Honesty

- Where it lives: the plan's `Risks`/`Unknowns` text, hedges inside `Approach`, and hedges in the plan comment (for example "the exact site may be one layer up").
- What good looks like: an unknown stated as an unknown, with how it will be settled. Bad looks like: an unverified guess written as settled fact. In live mode, an honest mid-build change is recorded under `## Deviations` in `plan.md`.

## Comms

- Where it lives: the `## Candidate plan comment`; compared with `## Thread highlights` (maintainer lines marked COLLABORATOR, MEMBER, or OWNER carry the direction) and `## Repo facts` (the `contribution policy` line states any AI rule, and says whether it covers issues and comments or only pull requests; the `bug reports` line states the template asks).
- What good looks like: the comment quotes or answers the maintainer's constraint, culprit, chosen option, or prior-art PR, and promises only what the plan holds. When the policy requires AI disclosure or human-written comments for issues or comments, the comment says so in plain words naming the tool and extent. Bad looks like: a plan or comment that ignores the owner's stated direction; "Hi, I can fix this, please assign me" with no plan; a promised timeline; a missing disclosure where the policy requires one. A disclosure ask that applies only to pull requests puts nothing on the comment.
