# Rubric: is this a good first issue?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever checks
you define here. It ships empty on purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where. Name the source
     (repo-facts block, issue body, comment thread, or the locations in
     references/evidence-guide.md). "The repo" is not a source; "the last
     5 default-branch commit dates" is.
   - Pass condition: a condition someone else could apply and get your
     answer. Prefer thresholds with numbers ("a maintainer commented
     within 30 days") over adjectives ("maintainer is responsive").
   - Weight: `required` (a fail here rejects the issue) or `preferred`
     (never changes the verdict; a nice-to-have that helps rank the
     issues you accept).

2. A verdict rule below the table: how the check grades combine into
   accept or reject, including how `unclear` is treated. The verdict
   space is binary. If you write no rule for `unclear`, the skill treats
   it as fail.

Cover what actually kills first contributions. The lecture named four
families: the maintainer is alive, the repo is in use, the scope fits a
newcomer, and nobody else is already on it. A rubric that ignores a family
will fail eval issues designed around that family.
-->

## Checks

| Check                  | Evidence                                                                                                                                           | Pass condition                                                                                                                                                                                                                                                                                                                                                                 | Weight    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| maintainer-alive       | The "last 5 default-branch commits" dates and author names in the repo-facts block (or the front-page commit list in live mode)                    | At least one of the last 5 default-branch commits is dated within 90 days of the captured/current date AND is either authored by a human (a username not ending in `[bot]`) or is a bot-authored merge of a human-opened pull request. Five consecutive commits from bots with no human authorship or human-opened merge (e.g., automated dependency bumps merged by another bot) fail this check even if recent | required  |
| repo-in-use            | The "archived:" flag, "latest release" date, and "last push to any branch" date in repo-facts (or the repo front page / Releases box in live mode) | Repo is not archived, AND (last push to any branch is within 180 days OR the latest release is within 365 days) of the captured/current date                                                                                                                                                                                                                                   | required  |
| scope-fits             | The issue body and comment thread                                                                                                                  | Pass if the issue describes one deliverable a single contributor could complete in one pull request — even if that PR touches several files, the write-up is short, or the body is a numbered breakdown of root causes / implementation suggestions for that one deliverable (a numbered internal breakdown of ONE fix is not the same as a list of many separate sub-issues). A terse bug report or an incompletely-enumerated list ("X, Y, Z, etc.") still passes if the opener is a maintainer/collaborator or the issue carries a "good first issue" label — terseness alone is not a scope failure. Fail if: the issue is explicitly a tracking/umbrella issue (a list of many separate linked issue numbers, or an open invitation for many different contributors to each pick their own small-or-big piece, indefinitely); it is a pure usage/support question; the thread shows an unresolved design disagreement with no maintainer-stated direction; it is a feature request with zero maintainer/collaborator engagement whose own text marks a key implementation detail as undecided/TBD; a maintainer states outright that the fix touches core internals/deep architecture beyond newcomer scope; or the issue has a years-long history of repeated claim/abandon cycles (reassigned and auto-unassigned for inactivity more than once, or a mentioned PR that was opened but never merged), signaling real difficulty despite looking simple | required  |
| unclaimed              | The "this issue: assignees" and "linked PRs" line in repo-facts, plus any PR mentioned in the comment thread (or the Assignees box, Development box, and comment thread in live mode — when the Development box and the thread disagree, believe the thread) | Pass if assignees is none/empty AND no PR — whether formally linked or just mentioned as opened/in-progress in the comment thread — is in an open state. Fail if any assignee is set or any such PR is open. Claim comments with no accompanying open PR ("I'd like to work on this") do not by themselves fail this check | required  |
| ai-contribution-policy | The "contribution policy" line in repo-facts (or CONTRIBUTING.md / AI_POLICY.md in live mode)                                                      | Fail only if the policy states an outright ban on AI-generated contributions with no carve-out for assistive/human-reviewed AI use (e.g., "we do not accept AI-generated code"). Conditions (disclosure, human review, testing requirements) pass. A policy banning only fully-autonomous AI generation while allowing assistive use passes. Silence/no stated policy passes   | required  |
| maintainer-responsive  | The "maintainer first-response sample" lines in repo-facts (or a sample of recently updated issues in live mode)                                   | Pass if at least one sampled issue got a first owner/member/collaborator reply within 14 days of being opened                                                                                                                                                                                                                                                                  | preferred |

## Verdict rule

Accept only if every required check (maintainer-alive, repo-in-use, scope-fits, unclaimed, ai-contribution-policy) passes. `unclear` on any required check counts as a fail for that check. The `maintainer-responsive` preferred check never changes the verdict — it only ranks issues that are already accepted, preferring the one with faster maintainer response.

<!-- State how the grades above combine into accept or reject, and how
unclear is treated. Example shape (write your own): "accept if every
required check passes; preferred checks never change the verdict, they
rank accepted issues; unclear counts as fail." -->
