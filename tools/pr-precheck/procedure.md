# Procedure: how this tool grades a PR package

Follow these steps in order. They grade a pull request; they do not
write or fix one. If a step cannot be done as written, say which step in
the summary instead of improvising. In eval mode the bundle is the only
source for every step; in live mode the sources are named in
`references/evidence-guide.md`.

## Read order

The plan is read before the diff and the diff before the description, so
that the plan fixes what "in scope" means before anything can persuade
you, and the description is read last as a set of claims to test rather
than a map to trust.

1. Read the repo-facts block (eval) or `scope.md`, the PR template, and
   the contribution docs (live). Write down: every section and checklist
   ask of the PR template; every action the template or contribution docs
   ask for (changelog entry, tests, docs, marker removal, title format,
   issue reference); the exact AI-use rule, if any, and whether it covers
   pull requests; and any contribution gate (CLA, discuss-first,
   restriction). Write "none" for each that is not stated.
2. Read the Issue and the Thread highlights. Write down every maintainer
   line that gives direction (a constraint, a gate, a named restriction,
   a chosen option, work in flight). Write "none" if there is no such line.
3. Read the plan context (eval) or `plan.md` with its Deviations (live).
   Write down: the plan's Files line (each named file, folder, or area);
   its scope (in) and not-in lines; every change it promises; its test
   plan (each command or action and the expected result); and every
   deviation note.
4. Read the Candidate PR's diff. List every changed file from its
   `---`/`+++` headers with a one-phrase note of what its hunks do, and
   mark each added test, changelog, or doc file. Read the commit list.
   Do this before opening the description.
5. Read the Candidate PR's test evidence. List each command or action
   shown, whether real printed output follows it, and which repo checks
   (suite, lint, types, build) appear with an outcome.
6. Read the title and description last. List each factual claim (what
   changed, what was added or not added, "exactly the plan", tests,
   changelog, issue reference), each template section with whether it is
   filled, each ticked checkbox, any AI-use statement, and any disclosed
   deviation or shortfall.

## Evidence gathering

7. For diff-within-plan: put each changed file from step 4 next to the
   plan's Files line and scope from step 3. Mark each file "named" (the
   file, its folder, or its area is in the Files line; a changelog entry
   or tests for the fix count when the plan promises them), "covered by a
   deviation note", or "unplanned". Then list the plan's promised changes
   and mark each "present in the diff" or "absent". Record any file in a
   not-in area. A file that appears in the diff is changed, even if the
   description does not mention it.
8. For description-true-to-diff: take each claim from step 6 and look for
   it in the diff and commit list. Mark each "true", "contradicted"
   (the diff shows the opposite, or a claimed file is not in the diff), or
   "unsupported" (nothing in the diff bears on it). A claim of fidelity to
   the plan ("exactly", "no changes beyond it") is checked against step 7.
9. For fix-shown-before-after: take the plan's reproduction command or
   action from the test plan (step 3) and find it in the test evidence.
   Record the specific observed result named for the before and for the
   after (an error message, exit code, number, row count, or visible
   output; pasted, or quoted as a result beside the command), whether the
   after-run is the same command or action as the failing one, and
   whether the expected-after outcome is visible or stated. An after that
   is only asserted ("matches the expected output", "works", "tests
   pass") names no observed result. Record each additional check the test
   plan names and whether its outcome is reported or disclosed as not
   run.
10. For repo-checks-outcome: take the checks named in the plan's test plan
    and the repo asks from step 1 and find each in the evidence. Record
    its concrete outcome (a count, "clean", "ok", an exit status, pasted
    or stated), or a disclosed failure with a reason. Record any check
    that is only claimed vaguely ("tests pass" with no count or named
    check) or absent, and any output that contradicts a claim.
11. For diff-reviewable: read every hunk once more as a reviewer. Record
    each debug print or leftover log line, commented-out code, dead or
    unused code, whitespace or formatting churn, rewrite or reordering of
    lines the plan's change does not need, and scratch or generated file.
    For each, ask "does the plan's change need this line?" Write "none" if
    every hunk serves the planned change.
12. For template-asks-honored: put each ask from step 1 beside the
    description and diff. Record for each: met with real content, met by
    an action in the diff, explained as not applicable with a reason, or
    ignored (missing, placeholder, template comment left in, issue not
    referenced where asked, action asked for but absent from the diff and
    not explained, or a ticked box the evidence contradicts).
13. For ai-policy-honored: record what the policy requires of a pull
    request (from step 1) and whether the description satisfies it in its
    own words, naming the tool and the extent where the policy asks. Where
    the policy is silent about pull requests, record "nothing asked".
14. For maintainer-direction-engaged: put each direction line from step 2
    beside the description and diff. Record for each: followed, mentioned
    with a reason, ignored, or no direction.
15. For title-says-what-and-where: record whether the title names what
    changed and where.

## Check execution

16. Grade the checks in rubric order: diff-within-plan,
    description-true-to-diff, fix-shown-before-after,
    repo-checks-outcome, diff-reviewable, template-asks-honored,
    ai-policy-honored, maintainer-direction-engaged,
    title-says-what-and-where. Grade each from the facts recorded in
    steps 7 to 15; re-open the package only to confirm a quote.
17. Each grade is `pass`, `fail`, or `unclear`. Apply the rubric's pass
    condition literally. Grade `fail` when the recorded facts show a
    violation. Grade `unclear` only when the package has no text that
    bears on the check, and say which text is missing. If the evidence for
    a check is genuinely absent, that is `unclear`, which the verdict rule
    treats as a hold.
18. Every grade carries one line of evidence that quotes the package's own
    words (a file name from the diff, a command and its output, a line of
    the description) or states "no such text" if absent. Never write
    "looks fine".
19. A terse PR is judged by the same conditions as a long one. A polished,
    confident description earns nothing: do not let step 6 change a grade
    that steps 7 to 11 earned. A disclosed deviation or shortfall passes
    the check it concerns; do not fail a PR for doing less than the issue
    when the description says so.
20. Do not double-penalise. If one unplanned file is also debris, fail
    both diff-within-plan and diff-reviewable on their own conditions,
    but do not invent a failure in a third check from it.

## Verdict assembly

21. Apply the rubric's verdict rule: `accept` only if every required
    check is `pass`; any required `fail` or `unclear` makes it `reject`;
    `title-says-what-and-where` is reported but never changes the verdict.
22. In the summary, name the deciding check: for `reject`, the first
    failed (or unclear) required check in the order of step 16, quoting
    its evidence line; for `accept`, state that every required check
    passed. In live mode, add the scope result and any voice-guide notes
    before the deciding check.
23. Output the readable summary (one line per check, then the deciding
    check), then the fenced JSON block as the last thing in the output,
    with one entry per rubric check in rubric order and nothing after it.
