# Unit 4 — Test and Submit

Path: `beat-1-sandbox/unit-4/pull-request.md`

Record of the pull request you opened against the Path Review repo, and of the evaluation
runs that produced `eval-run.txt`. This file is graded at the path above; a copy kept
anywhere else in the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Your pull request

**Pull request**

PENDING: the PR is not opened yet. Replace this line with the link to the pull request's own page on codepath/pathreview-ai301-fa26-s1 (`https://github.com/codepath/pathreview-ai301-fa26-s1/pull/<number>`) once it is open.

**Branch**

fix/32-delete-profile-vector-cleanup

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

Scores in order (each run's `agreement` line, scored packages only):

1. `--only pkg-01..pkg-05`: 4/5 (pkg-05 rejected, failed `fix-shown-before-after` and `repo-checks-outcome`)
2. `--only pkg-05,pkg-04,pkg-01` after loosening `repo-checks-outcome` and `fix-shown-before-after` once: 3/3
3. `--only pkg-06..pkg-10`: 5/5
4. `--only pkg-11..pkg-15`: 3/5 (pkg-11 and pkg-13 rejected, both failed `fix-shown-before-after`)
5. `--only pkg-16..pkg-20`: 5/5
6. `--include-calibration --only pkg-11,pkg-13,pkg-05,pkg-04,pkg-07,pkg-10,pkg-14,calib-03,calib-04` after rewriting `fix-shown-before-after`: 7/7 scored (both calibration packages still reject, unscored)
7. Full run, all 20: 20/20 (bar: 18/20: PASS)

The last score, 20/20, matches the `agreement: 20/20 scored items  (bar: 18/20: PASS)` line in `eval-run.txt`.

**Package analysis**

**pkg-11** (clear-accept). Gold label: `accept`. My rubric first said `reject` (run 4, `failed: fix-shown-before-after`) and says `accept` in runs 6 and 7.

Why it read that way. The package's test evidence shows the repro as a command with the before and after results written as annotations beside it: "# before: rg: ./.gitignore: line 1: error parsing glob 'foo\': dangling '\'" and "# after: searches normally, no error", then "'foo ' not listed (ignored), matching git check-ignore -v 'foo '", and "`cargo test -p ignore` passes (214 tests)". My first pass condition wanted real printed output and treated a remark after `#` as not output, so it failed a package whose before and after both name a specific observed result and whose expected-after is stated ("no parse error and parity with git on `foo `"). I rewrote the condition so what matters is a specific observed result for the before and the after, and a bare assertion ("matches the expected output", "tests pass") is what fails. That is why calib-03, whose after is only "matches the issue's expected output byte for byte", still rejects.

**Check rationale**

`fix-shown-before-after`, as it reads in `tools/pr-precheck/rubric.md`:

| fix-shown-before-after | Not tested. The Candidate PR's test-evidence section, read against the plan's test plan and the repro evidence's own steps. | Pass if the evidence re-runs the plan's own reproduction (the command or action the plan's test plan names) and names a specific observed result both before and after the change: an error message, exit code, number, row count, or the visible output, either pasted or given as the result beside the command (a `# before: ...` / `# after: ...` annotation that quotes the concrete result counts), with the expected-after outcome stated or visible (for example 41 rows then 42, an error then a clean parse, `code = 1` then `code = 0`). Fail if the after-state is only asserted to be right without a specific observed result ("matches the expected output", "behaves as expected", "works", "tests pass", "verified manually"), if there is no after-run or no observable named for the before, if the after-run is a different test than the one that showed the failure, or if the plan's test plan names an additional check on the fix and the evidence says nothing about its outcome and does not disclose that it was not run. An additional test-plan item passes when the evidence reports its concrete outcome, even in a sentence (for example "same-key redefine prints the one-time warning"). A disclosed "not run, because ..." for such an item passes. | required |

Why it reads that way. The first version required "real output" and said "a remark after `#`" did not count. It rejected pkg-11 and pkg-13 (both gold `accept`), whose before and after results sit beside the command as annotations such as "-- after:  { code = 0, stderr = "" }". I rewrote it around one question: does the evidence name a specific observed result for the before and the after? I rejected two other directions: keeping "printed output only", which fails correct PRs, and accepting any statement that the fix works, which would let calib-03's "matches the issue's expected output byte for byte" through, and pkg-04, pkg-07, pkg-10 and pkg-14 (all `reject`, not-tested).

**Trade-offs**

What `fix-shown-before-after` gives up: a PR can paste a convincing-looking result beside the command that was never actually run, because the check reads what the text names and cannot rerun anything. Eval mode cannot catch that either; only a maintainer running it can.

What changed because of it: pkg-11 and pkg-13 flipped from reject to accept. Canaries I re-ran with `--only` after rewriting it: the already-agreeing clear-accept pkg-05, the not-tested rejects pkg-04, pkg-07, pkg-10 and pkg-14, and (with `--include-calibration`) calib-03 and calib-04, which are the free trap checks for an after-state that is only asserted. All stayed as they were (run 6), and the final full run (20/20, every category matched) confirmed nothing else flipped. The earlier loosening of `repo-checks-outcome` was checked against pkg-04 (not-tested) and pkg-01 (standards-wall) in run 2.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/pr-precheck/`.
