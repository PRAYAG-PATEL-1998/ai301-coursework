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
| scope-feasible         | The issue body: the work it asks for | The issue describes one identifiable piece of work someone could start: a behavior, a gap, or a task you can point at. It fails only when there is no single piece of work in it: a codebase-wide checklist, an "improve X everywhere", or a container issue tracking many sub-tasks. An open design edge, an "etc.", or several files involved never fails this check; that raises the difficulty note instead | required  |
| code-change            | The issue body and comment thread: what the fix must change | Pass if the fix must change program logic or behavior: a bug, crash, wrong output, missing validation or error handling, performance or security problem, a missing feature that maintainers asked for, or missing tests for real logic. Fail if the whole fix is only documentation (README, guides, docstrings, comments, typos, wording), only styling (CSS, colors, spacing, sizes, layout), formatting or renaming with no behavior change, a translation, adding one entry to a data file (JSON, YAML, list), or a bulk-produced filler task. Grade `unclear` (counts as fail) if the issue body does not show what the fix changes | required  |
| unclaimed              | The "this issue: assignees" and "linked PRs" line in repo-facts, plus any PR mentioned in the comment thread (or the Assignees box, Development box, and comment thread in live mode — when the Development box and the thread disagree, believe the thread) | Pass if assignees is none/empty AND no PR — whether formally linked or just mentioned as opened/in-progress in the comment thread — is in an open state. Fail if any assignee is set or any such PR is open. Claim comments with no accompanying open PR ("I'd like to work on this") do not by themselves fail this check. Grade `unclear` (which counts as fail) if a comment from the last 14 days gives a concrete implementation plan or says a PR is coming ("will open the PR shortly"): that person is actively working on it | required  |
| outsider-pr            | CONTRIBUTING.md, README and the repo's workflow names (live mode: the file list under .github/workflows) | Pass if a contributor with no write access can open a pull request from a fork. Fail if CONTRIBUTING.md or a workflow says pull requests must come from branches in the main repo, not forks (for example a `close-fork-prs` workflow), or says the project does not take pull requests, or limits pull requests to members. Silence passes. Grade `unclear` (counts as fail) if the policy exists but you cannot tell if outsiders may open a PR | required  |
| ai-contribution-policy | The "contribution policy" line in repo-facts (or CONTRIBUTING.md / AI_POLICY.md in live mode)                                                      | Fail only if the policy states an outright ban on AI-generated contributions with no carve-out for assistive/human-reviewed AI use (e.g., "we do not accept AI-generated code"). Conditions (disclosure, human review, testing requirements) pass. A policy banning only fully-autonomous AI generation while allowing assistive use passes. Silence/no stated policy passes   | required  |
| maintainer-responsive  | The "maintainer first-response sample" lines in repo-facts (or a sample of recently updated issues in live mode)                                   | Sample the repo's 3 most recently closed issues, not only this issue, so a brand-new issue is never `unclear` for being new. Pass if at least 2 of the 3 sampled issues got a first owner/member/collaborator reply within 14 days of being opened. Fail if fewer than 2 did. If all sampled issues were opened by the owner, sample the 3 most recent pull requests from other people instead and use their time to first review. Grade `unclear` only if the repo has no outside issues or pull requests to sample                                                                                                                                                                                                                                                                  | preferred |

## Difficulty note

With each accepted candidate, report a one-line difficulty note in the read-out summary:

- **straightforward**: the issue names where the change lives and the change is bounded.
- **moderate**: the location is yours to find, or several files are involved.
- **ambitious**: an open design edge, or an unfamiliar subsystem; name the edge, because claiming this issue means raising it with the maintainer early.

The note is information for the chooser, never a verdict input: it does not appear in the fenced JSON block, it never changes accept or reject, and in eval mode it is skipped entirely.

## Verdict rule

Accept only if every required check (maintainer-alive, repo-in-use, scope-feasible, code-change, unclaimed, outsider-pr, ai-contribution-policy) passes. `unclear` on any required check counts as a fail for that check. The `maintainer-responsive` preferred check never changes the verdict — it only ranks issues that are already accepted, preferring the one with faster maintainer response.

<!-- State how the grades above combine into accept or reject, and how
unclear is treated. Example shape (write your own): "accept if every
required check passes; preferred checks never change the verdict, they
rank accepted issues; unclear counts as fail." -->
