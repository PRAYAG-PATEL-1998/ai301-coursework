# Evidence guide: where evidence lives in a PR package

An eval package is one markdown file with these sections: `## Repo facts`
(the repo's PR-template asks, contribution policy, AI rule), `## Issue`,
`## Thread highlights`, `## Plan context` (the accepted plan and the repro
evidence it built on), and `## Candidate PR` with `### Title`,
`### Description`, `### Commits`, `### Diff`, and `### Test evidence`.
Live mode maps to the same pieces: the repo-facts block is the PR
template (`.github/PULL_REQUEST_TEMPLATE.md`) and the contribution docs
(`docs/CONTRIBUTING.md` or `CONTRIBUTING.md`, plus any AI policy they
name); the issue and thread come from `gh issue view <url> --comments`;
the plan context is `plan.md` with its `## Deviations`; the candidate PR
is the diff from `git diff main...HEAD`, the title (first line) and
description of `pr_draft.md`, and `test_evidence.md`. Live mode grades
only committed changes and only what those drafts contain; untracked
files such as `plan.md`, `pr_draft.md`, and `test_evidence.md` are the
package's text, not part of the diff.

## Plan fidelity (harness category: silent-drift)

- Where it lives: the plan's scope in the `## Plan context` block (the
  `Files:` line, the in-scope statement, the `Not in scope` line, and any
  deviation note; live, `plan.md` sections Scope, Files I will touch, and
  `## Deviations`); what actually changed is the `### Diff` (every
  `--- a/` / `+++ b/` header; live, `git diff main...HEAD --stat`) and
  `### Commits`; the description's fidelity claims are in
  `### Description`.
- What good looks like: every changed file falls inside the plan's named
  files, folders, or areas, or inside a deviation note, and nothing under
  "not in scope" is touched. A deviation is an honest re-tie only when it
  is recorded (in the plan's deviation note, and restated in the
  description) and says what changed and why. Silent drift looks like a
  file or hunk the plan never named (more than the plan), a planned part
  missing with no note (less than the plan), or a description saying
  "exactly the plan" or "no other changes" over a diff that contradicts it
  or a description naming a test or changelog file that is not in the
  diff. A description that claims more or less than the diff delivers is
  silent drift, not a comms problem.

## Test evidence (harness category: not-tested)

- Where it lives: `### Test evidence` (live, `test_evidence.md` and the
  Testing section of `pr_draft.md`), read against the plan's test plan
  and the repro evidence's own command or steps in `## Plan context`.
  The repo's own checks are those the plan's test plan and the repo-facts
  block name (the test suite, linter, type checker, build; Path Review's
  template lists `make test-unit`, `make test-integration`, `make lint`,
  `make typecheck`).
- What good looks like: the plan's reproduction re-run, before and after,
  each shown as the command or action plus the specific observed result
  (pasted output, or the concrete result quoted beside the command), with
  the expected-after outcome stated or plainly visible (41 rows then 42;
  an error then a clean parse; `code = 1` then `code = 0`), and each repo
  check shown with its outcome (a pass count, "clean", "ok"). What does
  not count is an after that is only asserted: "matches the expected
  output", "works", "tests pass" name no observed result. A
  failing check reported honestly with its reason is evidence too (for
  Path Review, `make test-integration` stopping with "no tests ran" is
  expected and counts when pasted as is); a hidden failure, "tests pass"
  with no output, or an after-run of a different test than the failing
  one is not. If the test plan names a second check and the evidence
  neither shows nor discloses it, that is a gap.

## Diff quality (harness category: unreviewable)

- Where it lives: the hunks of `### Diff` and the `### Commits` list
  (live, `git diff main...HEAD` and `git log main..HEAD --oneline`).
- What good looks like: the fix is visible and so are its tests, and
  every changed line serves the planned change. The debris tells: debug
  prints or logging left in, commented-out code, dead or unused
  definitions, whitespace or formatting churn, a rewrite or reordering of
  lines the change did not need (same behavior, different shape),
  drive-by edits in unrelated files, scratch or generated files
  committed (live: repro scripts, notes, drafts in the diff). Judge by
  whether the plan's change needs the line, not by how few lines there
  are.

## Standards and comms (harness category: standards-wall)

- Where it lives: the `## Repo facts` block's `pull requests:` line
  (template sections, checklist, asks such as a changelog entry, tests,
  docs, a conventional-commit title, a `Closes #` line) and its
  `contribution policy` line (including any AI-use disclosure rule, and
  whether it covers pull requests); the `## Thread highlights` and
  `## Issue` for explicit maintainer direction (lines marked
  COLLABORATOR, MEMBER, or OWNER, a contribution gate, a ban, a chosen
  option); and where the PR honors them: `### Title` and `### Description`
  (live, `pr_draft.md` against `.github/PULL_REQUEST_TEMPLATE.md`).
- What good looks like: each stated section present with real content in
  the author's own words about this change; the issue referenced as the
  repo asks; each asked-for action done in the diff or explained; each
  ticked box true (Path Review: the CI box left unticked in a draft);
  where the policy asks for AI disclosure, a plain statement naming the
  tool and the extent (the course always discloses where the policy asks;
  for Path Review it goes under Notes for Reviewers); and explicit
  maintainer direction followed or answered with a reason. Boilerplate
  next to a visibly ignored ask is the failure: an empty section, a
  template comment left in place, a missing disclosure the policy
  requires, a restriction the thread states that the PR ignores. Where the
  repo asks nothing, nothing is graded. (Whether the description's claims
  match the diff is plan fidelity, above.)
