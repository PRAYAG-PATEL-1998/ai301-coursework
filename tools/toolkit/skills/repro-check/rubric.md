# Rubric: is this reproduction package ready to post?

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| env-recorded | The repro report's Environment line (tool version, OS, and — for compiled languages — commit/build), read against the issue's own stated version. | Names the version and OS the repo's bug template asks for, and either matches the issue's target version or explicitly says why it differs. | required |
| steps-followable | The repro report's steps, read in order starting from a fresh clone of the repo at the pinned version. | Every step is a concrete, executable action (a command, not "set up the project"); a stranger with only the repo's public docs could run the same sequence and reach the same starting state before the bug triggers. | required |
| behavior-matches | The artifact in the repro report (terminal output, log excerpt, or described screenshot), read against the specific error or behavior the issue names. | The artifact shows the same failure the issue describes (same error message, same exit code, same symptom) — not a different or merely adjacent one — with expected vs. actual stated explicitly. | required |
| honest-outcome | The report's concluding claim ("reproduced", "could not reproduce", "partially reproduced"), read against what its own artifact actually demonstrates. | The claim never says more than the artifact backs up. An evidenced "could not reproduce on <version>" passes fully; a confident claim whose artifact doesn't back it does not. | required |
| claim-specific | The claim comment's own wording, read against the issue it answers. | Names the specific behavior or scenario from the issue (not "this bug" or a generic paraphrase) — specific enough that the comment could not be mistaken for a claim on a different issue — and promises the next artifact (a report) rather than a fix timeline or a merge. A version number is one way to be specific but is not required on its own when the issue itself isn't version-scoped, as long as the named scenario is unambiguous. | required |
| conventions-respected | Both comments, read against the repo's stated CONTRIBUTING policy, issue/PR templates, and any AI-assistance disclosure requirement (from the repo-facts block, or the repo itself in live mode). | Follows whatever the repo's own conventions require, including disclosing AI assistance if the repo's policy asks for it; reads as this contributor's own words, not generic boilerplate. | required |

## Verdict rule

Accept only if every required check grades `pass`. Any required check graded `fail` or `unclear` results in `reject` — `unclear` is treated as `fail`, since proof that cannot be verified is proof that is not ready to post. There are no `preferred` checks in this rubric: every family above (environment, steps, behavior, honesty, comms/conventions) gates the verdict, because a rubric that treats one of them as optional will miss the eval packages built to test exactly that family.
