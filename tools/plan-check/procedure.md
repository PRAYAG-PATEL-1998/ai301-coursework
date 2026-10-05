# Procedure: how this skill grades a plan package

Follow these steps in order. They grade a plan; they do not write one. If a step cannot be done as written, say which step in the summary instead of improvising.

## Read order

1. Read the Repo facts block (eval mode) or `scope.md` plus the repo's CONTRIBUTING and AI policy (live mode). Write down two things: the exact AI-use rule, if any, and whether it covers issue comments or only pull requests; and what the bug-report template asks for.
2. Read the Issue and the Thread highlights. Write down every maintainer line that gives direction: a constraint ("keep the current API"), a named culprit or file, a chosen option, a requested action, and any open PR or prior art. Write "none" if there is no such line.
3. Read the Repro evidence block BEFORE the plan. List each numbered step with its result, then each control run with its result. Write one sentence on what behavior the evidence pins down and what it rules out. This list is what the diagnosis is judged against, so read it before the plan can persuade you.
4. Read the Candidate plan: Diagnosis, Scope (in and not-in), Changes or Approach, Files, Test plan, Risks or Unknowns. Write down the stated cause, the list of changes, and the test plan's expected result.
5. Read the Candidate plan comment last. Write down what it claims it found, what it promises, and whether it mentions the thread direction from step 2 and any AI statement.

## Evidence gathering

6. For diagnosis-grounded: take the stated cause from step 4 and the step/control list from step 3. For each control run, ask: if the stated cause were true, would this control have come out as it did? Record the first step or control that contradicts the cause, quoting its result. A contradiction means a result that could not happen if the cause were true; a mechanism the repro does not directly show is not a contradiction. If none contradicts it, record which steps and controls the cause fits and what differs between the failing run and the controls that it accounts for. If the plan says the cause comes from the thread, check the same list: the thread is a claim, not evidence.
7. For bounded-scope: copy the change list from step 4 and mark each item "needed" (the failing behavior from step 3 stops without it only if this change is made) or "extra" (anything else: refactor, rename, migration, new option, rewrite, port, docs pass, extra feature). Copy the plan's not-in line, or record that there is none.
8. For buildable-by-stranger: record the file, module, or code path named for each change, and the chosen approach for it. A named module or path with an exact function still to be pinned counts as located. Record every hedge phrase that leaves the location or the approach itself open ("somewhere", "whichever", "investigate", "maybe", "not sure which layer"); a hedge about the exact function or line does not count.
9. For test-decisive: record the test plan's command or action and its expected result. Record whether the result is something that would look different with and without the fix, using the repro steps in step 3 as the reference.
10. For thread-engaged: put the direction lines from step 2 beside the comment from step 5. Record for each: followed, mentioned with a reason, or ignored. Record every promise the comment makes and whether the plan contains it.
11. For conventions-met: put the policy from step 1 beside the comment. Record what the policy requires of an issue comment, and whether the comment contains it (for example an AI-use statement naming the tool and extent, or a statement that the comment is in the author's own words).
12. For honest-unknowns: record each uncertainty the plan states, and any guess written as fact.

## Check execution

13. Grade the checks in this order: diagnosis-grounded, bounded-scope, buildable-by-stranger, test-decisive, thread-engaged, conventions-met, honest-unknowns. Grade each from the facts recorded in steps 6 to 12; do not re-read the whole package, only re-open a part to confirm a quote.
14. Each grade is `pass`, `fail`, or `unclear`. Apply the rubric's pass condition literally. Grade `fail` when the recorded facts show a violation. Grade `unclear` only when the package truly has no text that bears on the check, and say which text is missing.
15. Every grade carries one line of evidence that quotes the package's own words (or states "no such text" if absent). Never write "looks fine".
16. A terse plan is judged by the same conditions as a long one. A plan that is polished, confident, or adopts the thread's diagnosis gets no credit for that. Do not let step 4 or 5 change a grade already earned in step 6: the repro evidence decides diagnosis-grounded.
17. A plan that defers part of the issue and says so is not a scope failure. Only an extra change that the repro does not need is.

## Verdict assembly

18. Apply the rubric's verdict rule: `accept` only if every required check is `pass`; any required `fail` or `unclear` makes it `reject`; `honest-unknowns` is reported but never changes the verdict.
19. In the summary, name the deciding check: for `reject`, the first failed required check in the order of step 13, quoting its evidence line; for `accept`, state that every required check passed.
20. Output the readable summary (one line per check, then the deciding check), then the fenced JSON block as the last thing in the output.
