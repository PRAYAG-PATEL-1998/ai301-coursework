---
name: pr-precheck
description: Grade a PR package (a candidate pull request read against the plan it claims to implement and the issue that plan belongs to) and decide whether it is ready to submit. Use when checking your own branch, draft PR title, and description before opening the pull request, or when grading an eval package bundle.
---

# pr-precheck: rubric-driven PR grading

## The question

You answer exactly one question about exactly one PR package: **is this
ready to submit?** A PR package is a candidate pull request (its title,
description, commits, diff, and test evidence) read against the plan it
claims to implement and the issue that plan belongs to. The PR is the
thing being graded; the plan, the issue thread, and the repo's stated
PR template and policy are what it is read against.

Never answer a different question (is the idea good, is the code
elegant, would the maintainers merge it). Never grade more than one
package per run. Never answer from gut feel: you answer by executing
`procedure.md`, which applies the checks in `rubric.md` to evidence
located with `references/evidence-guide.md`.

## Inputs and modes

Decide the mode first. If the user hands you a bundle (a markdown
package with a repo-facts block, an issue, a plan context, and a
candidate PR), you are in eval mode. If the user asks you to grade
their own branch or draft PR, you are in live mode.

**Eval mode.** The bundle is the whole world. Every fact comes from the
bundle text: its Repo facts, Issue, Thread highlights, Plan context,
and Candidate PR (title, description, commits, diff, test evidence).
Fetch nothing, run nothing, read no other file, and do not use what you
know about the real repository or issue: the bundle is frozen and wins
over anything live. Eval mode always grades a complete package: every
check in the rubric, with the full verdict rule. The item id in the
JSON is the bundle id you were given.

**Live mode.** Grade the student's own PR before it is opened. Read, in
this order:

1. `scope.md` (see the scope seam below), before anything else.
2. `plan.md` in the top folder of the working copy, including its
   `## Deviations` section if present. This is the plan the PR claims to
   implement. A student on the house chain reads the house plan, and the
   house repro pack as its repro evidence, instead; the same checks
   grade the same things there.
3. The branch's diff: run `git diff main...HEAD` (three dots) from the
   working copy; add `--stat` for the file list. This is every committed
   change the branch makes relative to the repo's default branch.
   Uncommitted or untracked files are not part of the diff and are not
   part of the PR.
4. The draft PR title (first line) and description (the rest) from
   `pr_draft.md`.
5. The test evidence in `test_evidence.md`.
6. The issue and its thread (`gh issue view <issue URL> --comments`),
   the repo's PR template (`.github/PULL_REQUEST_TEMPLATE.md`), and its
   contribution docs (`docs/CONTRIBUTING.md` or `CONTRIBUTING.md`, plus
   any AI policy they name). These are the live equivalents of the
   bundle's repo-facts and thread blocks.

The item id in the JSON is the PR URL if one exists, otherwise the issue
URL or the branch name. If a live-mode input is missing (no `plan.md`,
no `pr_draft.md`, no `test_evidence.md`, an empty diff), do not guess:
grade the checks that need it as `unclear` and say which file is
missing.

## The scope seam (live mode only)

In live mode, read `scope.md` before anything else. It names the one
repo a pull request may target and the house rules of that
environment (own-fork branch, one PR per issue, the template always
used, the disclosure section). Apply those house rules when you read
the evidence.

- Refuse to grade a PR package for any repo other than the one named on
  the `Repo:` line, however tempting.
- If the `Repo:` line still carries an unfilled placeholder (a bracketed
  `<ORG>/<PATH-REVIEW-REPO>` or anything not a real `owner/repo`), stop
  without grading. Tell the student to fill the `Repo:` line in
  `scope.md` with their section's Path Review repo, and emit no verdict.
- Never guess a scope.

In eval mode, ignore `scope.md` entirely.

## The voice seam (live mode only)

In live mode, after reading the package, read `voice-guide.md` and hold
the outgoing PR text, the title and the description, against its rules.
In the readable summary, list each rule the draft breaks, quoting the
rule and the offending phrase. If it breaks none, say so in one line.

The voice guide never changes the verdict on its own, because voice is
personal and the rubric has no check that reads it. Universal
communication-quality checks live in the rubric. In eval mode, ignore
`voice-guide.md` entirely.

## Component reads

The pieces fit together like this:

- `rubric.md` defines the checks (name, evidence, pass condition,
  weight) and the verdict rule. It decides what each grade means and how
  grades become accept or reject.
- `references/evidence-guide.md` is the rubric's map: for each family of
  evidence it says where to find it in a package (eval) and in the
  student's own files (live), and what good looks like there.
- `procedure.md` is how you work: read order, evidence gathering, check
  execution, verdict assembly. Execute it as written, in order.

If the procedure is silent on a step you need, do not improvise around
it: say in your summary which step is missing, then apply the rubric
literally to the evidence you have. If `rubric.md` has no checks or no
verdict rule, or `procedure.md` has no steps, stop and say so: this
tool cannot grade without both, by design, and an empty tool that
invents checks is worse than none. Emit no verdict in that case.

## Verdict and output

The verdict space is binary: `accept` (ready to submit) or `reject`
(hold). There is no third verdict, no "accept with reservations", and no
score. Reservations belong in the evidence line of the check they
concern.

End your reply with the fenced JSON block below: valid JSON, with one
entry in `checks` for every check in the rubric (in rubric order), the
`evidence` a single line quoting or naming the fact that decided the
grade, and the `verdict` produced by the rubric's verdict rule. The
block is the last thing in the reply; write nothing after it. Before it
you may show a short readable summary: a line per check, the deciding
check, and in live mode the scope result and any voice-guide notes.

```json
{
  "item": "<PR URL or bundle id>",
  "checks": [
    {"name": "<check name>", "grade": "pass|fail|unclear",
     "evidence": "<one line: the fact or quote that decided it>"}
  ],
  "verdict": "accept|reject"
}
```

## Grading discipline

- **Evidence first.** Never grade a check without naming the fact or
  quote that decided it. "Looks fine" is not evidence.
- **Grade the thing, not the polish.** A terse, complete PR can be ready
  and a beautiful, confident one can hide drift. Read the diff, the
  output, and the files themselves against the plan, the issue, and the
  stated standards, never the formatting or the length of the write-up.
  A claim in the description is a claim, not proof.
- **The rubric decides, not you.** If a check passes by its stated
  condition but feels wrong, it still passes; note the tension in the
  summary if you want. The fix belongs in the rubric, not in the run.
- **The procedure decides how, not you.** Follow `procedure.md` as
  written and report its gaps instead of papering over them.
- **Unclear.** Treat `unclear` as the rubric's verdict rule directs. If
  the rule is silent, treat `unclear` as `fail`: a PR you cannot verify
  from the package is a PR that is not ready to submit. Use `unclear`
  only when the package truly has no text that bears on the check, and
  say which text is missing.
- **An honest shortfall is not a failure.** A PR that discloses what it
  leaves out, or a deviation it recorded in the plan, is judged as the
  disclosed PR it is. A silent shortfall or silent extra is the failure.
