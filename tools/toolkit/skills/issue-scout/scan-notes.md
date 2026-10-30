# Scan notes: friction logged during live scans

<!-- Friction found while running a scan, to turn into rubric/strategy
patches later. Not loaded by the skill; this is scratch for the
student, dated per scan. -->

## 2026-10-25 scan

- **Templated/farm issues pass scope-fits even though they add no OSS
  workflow value.** `lingdojo/kana-dojo#33150` ("add anime quote 423")
  is a mass-produced Hacktoberfest filler issue — copy a JSON object,
  no codebase reading, no real review. It is technically "one bounded
  deliverable completable in one PR," so the rubric's scope-fits check
  passes it, but it does nothing for the fit-profile goal of practicing
  "reading unfamiliar codebases, working issue-to-PR." The rubric has
  no check for "does this require engaging with the existing code at
  all," and the ranking filters only look at label/assignee/comment
  fields, so a `hacktoberfest`-labelled, numbered/templated title slips
  through both stages. Possible fix: a ranking filter dropping
  `hacktoberfest`-only issues, or a rubric check for "issue requires
  reading/modifying existing source, not just appending a data literal."

- **Unclaimed's claim-comment carve-out doesn't distinguish a casual
  claim from an active one.** `Tencent/teamai-cli#1397` has one comment:
  not "I'd like to work on this" but a full investigation + a 3-step
  implementation plan + "Will open the PR shortly." The rubric's pass
  condition explicitly says claim comments don't fail this check by
  themselves, so it graded `pass`, but taking this issue now risks
  duplicate work within hours. The rubric's stated example is too thin
  to cover this case. Possible fix: fail (or `unclear`) unclaimed when
  a claim comment includes a concrete implementation plan or states a
  PR is imminent, not just "no assignee, no open PR."

- **One org can crowd a language query.** The `good first issue` +
  `language:python` query returned many near-identical
  `mloda-ai/mloda-registry` / `mloda-ai/mloda` issues
  ("[Need support]: ...") all created/updated within seconds of each
  other — reads like an automated issue-generation pipeline, not
  organic backlog. They happened to be genuinely well-scoped this run
  (good evidence, clear acceptance criteria), so nothing failed because
  of it, but a less careful pipeline could flood the top-N with one
  repo's auto-generated backlog. The per-repo cap (2) helped here;
  worth watching whether it needs to be stricter if this recurs.

## 2026-10-25 fixes (after scan 1)

- **Rubric, `unclaimed`:** a claim comment with a concrete plan or "will open the PR shortly" from the last 14 days now grades `unclear`, which counts as fail. Reason: `Tencent/teamai-cli#1397` passed this check but another contributor was already working on it.
- **Strategy, new ranking rule 5:** drop `hacktoberfest`-labelled results unless they also have `bug`. Reason: `lingdojo/kana-dojo#33150` was a filler issue (append one JSON object) that passed `scope-fits` but needs no code reading. Later rules renumbered.
- **Per-repo cap of 2:** left unchanged. `mloda-ai` issues were well scoped this run, so nothing failed. Watch it on the next scan.
- **Not re-tested:** I did not run a second scan ($1). The two fixes are untested.

## 2026-10-25 second change (after reading the five verdicts)

- **Finding:** 3 of the 5 accepted issues were documentation-only (`mloda-registry#1327`, `mloda-registry#1326`, `mloda#2325`). One more was a one-line JSON data edit (`kana-dojo#33150`). Only `teamai-cli#1397` changed code. The rubric accepted all of them, because my profile never said I want code.
- **Fit profile, `scope.md`:** added the sentence "I do not want documentation-only issues: I want a change to code."
- **Strategy, new ranking rule 6:** drop results labelled `documentation`, `docs` or `doc` unless they also have `bug`. Later rules renumbered.
- **Limit:** a label rule cannot catch a docs-only issue that has no docs label. The rubric would have to check it after the issue page is open. Not changed yet.
- **Not re-tested:** no second scan.

## 2026-10-25 third change (before scan 2, after asking what I want)

- **Answers:** any change type (bug fix, tests, small feature, performance or security fix); any project type; issue quality matters more than repo size, but the repo must be active; about 8 to 10 hours of effort; no documentation-only work.
- **Rubric:** new required check `code-change` (fails docs-only, typo, data-entry and filler issues; `unclear` counts as fail). Added to the verdict rule.
- **Rubric:** new preferred check `issue-quality` (expected behavior plus a pointer to the code or a repro, doable in about 8 to 10 hours). It ranks accepted issues and never changes the verdict.
- **Strategy:** ranking rule 4 now keeps feature-labelled issues that also have `bug`, `help wanted` or `good first issue`. Eight new queries: C#, Java and Python/TypeScript bugs, `help wanted`, and "tests" in the title.
- **Profile (`scope.md`):** added the change types, project types, effort and "issue quality over repo size".
- **Limit:** no `gh` field shows repo stars or issue quality, so only the rubric can judge them.

## 2026-10-25 scan 2 (after the rubric and strategy changes)

- **Worked:** the `code-change` check rejected `Bees-bot/bees-desktop#283` (a report-back task, no pull requests accepted). The documentation rule dropped 68 docs-only results and the hacktoberfest rule dropped 118. The `kana-dojo` filler and the three `mloda` documentation issues did not return. Two code issues were accepted: `mloda-registry#1333` (Python) and `rcv-simulator-va#16` (TypeScript/CSS).
- **Missing filter:** the ranking rules cannot see the `stage/040-covered-by-pr` label that sank `projectbluefin/utah-packages#476` (open PRs #627 and #633). Possible fix: drop results whose labels contain `covered-by-pr` or `in-progress`.
- **Fresh issues:** newest-first puts brand-new issues (`mlcommons/chakra#232`, opened under an hour before) at the top before maintainers react. Possible fix: prefer issues at least one day old.
- **Dead filters:** ranking rules 1 (assignee) and 2 (90 days) removed nothing, because the queries already use `--no-assignee` and `--sort updated`. They stay as a safety net.
- **Weak points left:** `maintainer-responsive` is `unclear` for both accepted issues, so no first-reply time was measured. Both repos are tiny (6 stars and 0 stars), which matches the limit already logged: no `gh` field shows repo size.

## 2026-10-25 fixes after scan 2

- **Missing filter:** new ranking rule 7 drops results whose labels contain `covered-by-pr`, `in-progress`, `in progress`, `wip`, `claimed` or `assigned`. Reason: `projectbluefin/utah-packages#476` had open PRs but no assignee.
- **Fresh issues:** all queries now return `createdAt`. New ranking rule 8 drops results created less than 24 hours before the scan. Reason: `mlcommons/chakra#232` was under an hour old and had no maintainer reaction.
- **Dead filters:** rules 1 and 2 stay as a safety net. The file now says why.
- **Reply speed:** the preferred check `maintainer-responsive` now samples the repo's 3 most recent closed issues. Pass needs a first reply within 7 days on at least 2 of 3. It is `unclear` only for a repo with fewer than 3 closed issues. Reason: both accepted issues were `unclear`, because one was new and one had no comments.
- **Rules renumbered:** the cap per repo is now rule 9 and the order is rule 10.
- **Not re-tested with a scan.** I tested only that all 15 queries still run.

## 2026-10-26 scan 3 (after the three weak-spot fixes)

- **Fixes that worked:** rule 8 dropped 350 results created under 24 hours ago. `mlcommons/chakra#232` and `projectbluefin/utah-packages#476` did not return. The filters dropped 595 of 1,342 results in total.
- **Result:** 1 accepted (`jerseycheese/rcv-simulator-va#16`) and 4 rejected. Scan 2 accepted 2.
- **Still open, `maintainer-responsive`:** `unclear` for the accepted issue. The repo's closed issues were all opened by the owner, so there is no outside first-reply time. The new sampling rule cannot grade a solo repo.
- **Still open, issue linked only in the text:** `run-llama/llama_index#23667` reached the top 5 because PR #22407 was named in the issue body and not formally linked. `-linked:pr` missed it. Only the rubric caught it, and it cost a grading slot.
- **Still open, claimed issues:** 3 of the 5 top results were claimed or already in progress (`aquascope#346`, `omxterm#223`, `bees-desktop#283`). Newest-update-first favours issues with fresh activity, and that activity often means someone is working on it. Possible fix: prefer issues with 0 comments, or drop issues with a comment in the last 14 days that contains a claim phrase.
- **Still open, report-only issues:** no search-time filter finds "we don't take pull requests". The rubric rejects it, but it cost a grading slot. Possible fix: drop results whose title contains "report" or "test on", or accept the cost.
- **Thin code change:** `rcv-simulator-va#16` is a CSS size change. It passes `code-change` under the rubric wording. It is the thinnest code change of the five. Possible fix: require a logic change in `code-change`.
- **Overlap:** query 1 and query 10 both returned `llama_index#23667`. The merge step removes duplicates, so this costs nothing.

## 2026-10-26 fixes after scan 3

- **Claimed issues:** ranking rule 3 now drops results with 4 or more comments (was 10). Ranking rule 10 now orders by fewer comments first, then newest update. Reason: 3 of the 5 top results in scan 3 were claimed, and a fresh comment is often a claim. No `gh` field shows comment text, so comment count is the only free signal.
- **Thin code change:** `code-change` now needs a change to program logic or behavior. A styling-only fix (CSS, colors, spacing, sizes, layout) fails. Reason: `rcv-simulator-va#16` was only a size change.
- **Solo repos:** `maintainer-responsive` now falls back to the 3 most recent pull requests from other people when every sampled issue was opened by the owner. It is `unclear` only when the repo has no outside issues or pull requests.
- **Not fixed:** a PR named only in the issue text (`llama_index#23667`) and report-only issues. No ranking field shows body text. The rubric catches both after a grading slot is spent.

## 2026-10-26 scan 4 (after the scan 3 fixes)

- **Result:** 1 accepted (`allenporter/supernote#234`, Python: add default tags to generated transcripts and AI summaries) and 4 rejected. The funnel was 1,340 unique results, then 371 after the filters and the cap of 2 per repo.
- **Worked:** the stricter `code-change` check rejected `rcv-simulator-va#16` (styling only) and `orazaka#29` (a chore with no behavior change). The rule that sorts by fewer comments put 0-comment issues first. Three of the five graded issues were not claimed.
- **Still open, non-code issues:** two of the five (`#16`, `#29`) were non-code. Possible fix: drop results labelled `chore`, `ui`, `css` or `styling` unless they also have `bug`.
- **Still open, refactors:** the rubric does not say if a pure refactor counts as a code change, so `supernote#122` got `unclear`. Decision needed: I want a behavior or logic change, so a pure refactor should fail.
- **Still open, rule 8:** it removed about half of the results (1,014 down to 557), which is heavy for a 24-hour rule. Cause: the scan ran with a 24-hour window on a sort by newest update, and many issues are new. Possible fix: keep the rule, because the 24-hour wait did stop `chakra#232` from returning.
- **Still open, `maintainer-responsive`:** `unclear` again for `supernote#234`. The scout did not take the outside-PR sample that the new rule asks for. The check is preferred, so it does not change the verdict.
- **Caveat for `supernote#234`:** the issue line "Ensure tag records exist in SummaryTagDO if needed" is vague. Ask the maintainer before you start.

## 2026-10-26 maintainer-responsive window restored to 14 days

- **Change:** `maintainer-responsive` uses the original 14-day window again (it was 7 days after my change). The rest of my change stays: sample the repo's 3 most recent closed issues, pass on at least 2 of 3, and fall back to other people's pull requests for solo repos.
- **Reason:** I chose the original window. The check is preferred, so it never changes a verdict.

## 2026-10-26 issue-quality moved out of the rubric

- **Change:** removed the preferred check `issue-quality` from `rubric.md`. The expectation (expected behavior stated, the file or error named or repro steps given, about 8 to 10 hours of work) is now a sentence in the fit profile in `scope.md`.
- **Reason:** I chose to keep the rubric closer to the original. The profile ranks accepted issues and never changes a verdict, which is what `issue-quality` did.
- **Effect:** the read-outs of scans 2 to 4 list an `issue-quality` check. A new scan will not.

## 2026-10-26 scan 5 (after removing `issue-quality` and restoring the 14-day window)

- **Result:** 1 accepted (`baipix/baipix#530`, TypeScript: preview the brush when an Apple Pencil hovers) and 4 rejected. 1,340 unique results, 674 after the ranking filters.
- **Worked:** the read-out has no `issue-quality` check, as intended. `code-change` rejected three issues (`dotline#2` report, `rcv-simulator-va#16` styling, `orazaka#29` configuration). `maintainer-responsive` gave a real `pass` for `baipix#530` by sampling outside pull requests.
- **Caveats for `baipix#530`:** testing needs pen-hover input, probably an iPad. The repo has 5 stars.
- **Still open, wasted grading slots:** 4 of the 5 graded slots went to issues the rubric rejects. Two repeat from earlier scans (`llama_index#23667`, `rcv-simulator-va#16`, `orazaka#29`). Possible fix: drop results labelled `chore`, `ui`, `css`, `styling`, `config` or `ci` unless they also have `bug`.
- **Still open, repeats:** the same rejected issues return every scan. The scout has no memory of earlier verdicts. Possible fix: add a list of rejected URLs to `search-strategy.md` and drop them.
- **Still open, rule 8:** it removed 337 results. The scout thinks the system clock is about a day ahead of the stated date, so some removed issues may be older than 24 hours. Not changed.

## 2026-10-26 Issue Selection site, and the first graded pick

- **Site problem:** the site lists issues alphabetically by organization and shows no dates. Python + `bug` gave 244 issues. I checked 56 on GitHub. Only 14 were open, unassigned, updated in 60 days and had 3 or fewer comments. Four of the five `apache/mahout` issues already had an open PR (#1544, #1532, #1561, #1534), and one Rust issue had two PRs. The site shows issues as available when they are not. Rule: check GitHub before you trust the site.
- **Graded pick:** `monarch-initiative/dismech#10458` (Python regex bug in `src/dismech/preflight_dr.py:103`) graded `accept`. All six required checks passed. `maintainer-responsive` (preferred) failed: the sampled replies came from a bot.
- **Fork rule (checked in CONTRIBUTING.md):** the repo does not accept PRs from forks. The `close-fork-prs` workflow closes them. New contributors must first ask for access, by opening an issue. The rubric has no check for this, so the verdict did not show it. It could stop the contribution. Possible fix: add a required check "can an outsider open a PR".
- **Bot replies:** the `maintainer-responsive` sample counts bot replies. Possible fix: ignore bot authors.
- **Claim rule:** if I commit to this issue, I claim it upstream on the issue first (`scope.md`).

## 2026-10-26 site check and two scout fixes

- **Site check:** `allenporter/supernote#234` and `baipix/baipix#530` are NOT on the Issue Selection site (title searches gave 0 results, and `?org=allenporter` and `?org=baipix` gave 0 issues, while `?org=apache` gave 476). The site needs the `org=` parameter in the URL. The course says your real issue comes from the site, so these two are practice results from the scan only.
- **New required check `outsider-pr`** in `rubric.md`: fails if CONTRIBUTING.md or a workflow blocks pull requests from forks or limits pull requests to members. Reason: `dismech#10458` passed all checks, but the repo auto-closes fork PRs. Added to the verdict rule.
- **Rejected-issues list** in `search-strategy.md` (20 URLs) and new ranking rule 9, which drops them. Reason: scans 2 to 5 graded the same rejected issues again. The cap per repo is now rule 10 and the order is rule 11.
- **Not tested:** no scan after these changes. The two fixes are untested.
- **Effect on `dismech#10458`:** it would now fail `outsider-pr`, so it is no longer a good pick.

## 2026-10-26 graded picks 2 and 3

- **Result:** `allenporter/supernote#234` and `baipix/baipix#530` both graded `accept`, with all required checks and `maintainer-responsive` passing. `maintainer-responsive` passed because the scout sampled pull requests from other people (first review in 11 to 80 minutes). The new sampling rule worked.
- **`outsider-pr`:** the grade ran before I added the check. I checked both repos by hand: no fork-blocking workflow, no member-only rule, and forking is allowed. Both pass.
- **Not on the site:** neither issue is on the Issue Selection site. The course says the real issue comes from the site, so these two are practice results.
- **Fit:** `supernote#234` is Python backend work on an AI tool and touches a database model (`SummaryTagDO`). `baipix#530` is a small TypeScript task, but testing needs an Apple Pencil or simulated pen events, and the guide asks for French and English strings, a changelog line and tests.

## 2026-10-26 full site scan, tag `good first issue` (2,793 issues, 28 pages)

- **Method:** I read all 28 pages of the Issue Selection site (languages Python, TypeScript, JavaScript, Java, C#; tag `good first issue`) and checked each issue on GitHub with the GraphQL API (read-only). Filters: open, unassigned, no open PR, no claim comment, fewer than 4 comments, repo pushed in 14 days, main repo language in my stack, body at least 300 characters, no docs/typo/styling labels or titles, not already rejected. 2,725 issues checked, 299 survived.
- **Biggest losses:** open PR mentions the issue (about 450), a claim comment (about 430), repo language outside my stack (about 1,000).
- **New finding, AI policy:** the scout does not read AI policies well. `beetbox/beets#5411` looked perfect (Python bug, 15.8k stars, 0 comments), but `AI_POLICY.md` says "AI is not for good first contribution issues" and "Agents may only interact with the repository for code review." PR #7084 for this exact issue was closed in an hour with "See our AI policy." The rubric check `ai-contribution-policy` fails only on an outright ban, so it may pass this repo. Possible fix: make it `unclear` (a fail) when a policy limits AI use on good first issues.
- **Another finding, hostile PR:** beets PR #7111 for the same issue was a malicious PR (an obfuscated script in `.vscode/tasks.json`). Do not check out unknown PR branches in an editor.
- **Another finding, stale issues:** `apache/beam#19712` was already fixed in the code (a client cache exists). Always read the current code before choosing.
- **Best candidates after reading the issues and the repo policies:** `cuthbertLab/music21#1659`, `cuthbertLab/music21#1234`, `code-charity/youtube#4314`, `nusmodifications/nusmods#3060`, `ROCm/iris#589`.
- **music21 policy:** welcomes AI-assisted contributions, with `(AI)` in the PR title when the work is mainly AI. Outside PRs: 8 of 8 merged, median first response about 12 minutes.

## 2026-10-26 graded picks 4 to 6 (music21 x2, ImprovedTube)

- **Result:** `cuthbertLab/music21#1659`, `cuthbertLab/music21#1234` and `code-charity/youtube#4314` all graded `accept`. The new `outsider-pr` check ran for the first time and passed for both repos. `ai-contribution-policy` passed for music21 because its rules are conditions only (declare AI use in the PR title).
- **`maintainer-responsive` is wrong for music21:** the scout graded it `fail` (1 of 3 closed issues had a maintainer comment). My own check of outside pull requests found 8 of 8 merged and a median first response of about 12 minutes. The scout samples closed issues, and a maintainer who closes an issue without a comment looks silent. The rubric falls back to outside PRs only when the owner opened every sampled issue. Possible fix: always sample outside PRs first, and count a closed or merged PR as a reply.
- **Warning for `youtube#4314`:** PR #4319 ("Fix settings restore persistence race") was closed unmerged on 2026-10-03. Someone tried to fix this already, and the report is vague. It is the weakest of the three.
- **Claim rule:** if I choose one, I comment on the issue first (`scope.md`).
- **Order by fit:** 1) `music21#1659`, 2) `music21#1234`, 3) `youtube#4314`.

## 2026-10-29 unit 6 scope patch

- **Check replaced:** `scope-fits` is now `scope-feasible`, using the staff patch text (`skill/rubric-scope-patch.md` in the unit 6 materials). It fails only when the issue holds no single piece of work (a codebase-wide checklist, an "improve X everywhere", or a container issue). An open design edge, an "etc." or several files now raise a difficulty note instead of rejecting.
- **Difficulty note:** added a section under the checks table: straightforward, moderate or ambitious. It is information for me and never changes the verdict.
- **Verdict rule:** now lists `scope-feasible` in place of `scope-fits`.
- **Why:** in my five scans, `scope-fits` rejected issues with an open edge (for example `kaoto#3789`, which waits for a maintainer decision). The three issues I claimed all have a small open edge (for example, whether to change the default of `AutoClose` in `MudBlazor#13128`), which the note will name.


## 2026-10-29 re-grade of my three claimed picks (patched rubric)

- **Result:** `nusmods#3060` accepted (difficulty: moderate). `MudBlazor#13128` and `openedx#897` rejected, both on `unclaimed` = `unclear`.
- **Scout flaw, my own claim blocks me:** the `unclaimed` check counted MY OWN claim comment (2026-10-26) as an active claim by someone else, so it graded `unclear` and rejected two issues I had legitimately claimed. The rule I added in the first round (a plan or "PR coming" comment from the last 14 days gives `unclear`) does not exclude the grader's own user. Possible fix: ignore comments written by my own GitHub username (`PRAYAG-PATEL-1998`).
- **Maintainer replies the scout did not weigh:** `MudBlazor#13128` (danielchalmers): the current close behavior is by design and stays in v9, and only a docs PR is welcome now. That makes it a docs fix for now, which I do not want. `openedx#897` (bradenmacdonald): "Please open one PR for all seven and anything else related to the titles." That is a go-ahead.
- **`maintainer-responsive` is still unreliable:** it samples the 3 newest closed issues by creation order and counts only comments. Still a preferred check, so it changes no verdict.
- **Decision input:** the maintainers' replies matter more than the scout's verdict here. `openedx#897` has an explicit go-ahead. `MudBlazor#13128` has a clear no for a code fix. `nusmods#3060` has no reply yet.
