# Search strategy: where your scout looks, and why

<!--
THIS IS THE PART YOU WRITE. The scout in SKILL.md executes whatever
queries and filters you define here. It ships empty on purpose: the
strategy is your judgment about where YOUR first contribution lives,
and a scan without authored queries is just someone else's defaults.

A filled strategy must contain:

1. At least one query in the Queries section. Each query is a real
   `gh search issues` invocation, and each should trace to a sentence
   of your fit profile in scope.md: if you cannot say which sentence
   produced a query, the query is probably not yours. Search breadth
   is the point at this stage: prefer generous limits and let the
   ranking filters do the narrowing.

2. At least one ranking filter in the Ranking filters section. A
   filter is a condition or an ordering over fields the search
   results already carry (last activity date, assignee presence,
   label set, comment count, repo). It must be checkable from the
   result fields alone: if deciding it would need opening the issue
   page, it belongs in your rubric, not here. Ranking is the free
   stage; keep it free. Make at least one filter an ordering, or
   state your tie-break: with drop conditions alone, the scout takes
   the top of whatever order the searches happened to return, and
   the graded candidates stop being traceable to you.

3. The top-N line, kept or deliberately changed.
-->

## Queries

<!-- Real gh search invocations; each has a comment naming the profile sentence. -->

# Profile: "I have experience with Python, JavaScript/TypeScript, and Java/C#" (Python)
gh search issues --label "good first issue" --language python --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "I have experience with Python, JavaScript/TypeScript, and Java/C#" (TypeScript)
gh search issues --label "good first issue" --language typescript --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "I have experience with Python, JavaScript/TypeScript, and Java/C#" (JavaScript)
gh search issues --label "good first issue" --language javascript --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "I have experience with Python, JavaScript/TypeScript, and Java/C#" (Java)
gh search issues --label "good first issue" --language java --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "avoid ... repos that look inactive or unresponsive" + small bug fix (Python bugs)
gh search issues --label bug --label "help wanted" --language python --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: same sentences (TypeScript bugs)
gh search issues --label bug --label "help wanted" --language typescript --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "avoid ... repos that look inactive or unresponsive" (established organizations, not tiny repos)
gh search issues --label "good first issue" --owner apache --owner open-telemetry --owner pytorch --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "Python, JavaScript/TypeScript, and Java/C#" + "I want a change to code" + small bug fix (C# bugs)
gh search issues --label bug --label "good first issue" --language "c#" --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "Python, JavaScript/TypeScript, and Java/C#" + "I want a change to code" + small bug fix (Java bugs)
gh search issues --label bug --label "help wanted" --language java --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "Python, JavaScript/TypeScript, and Java/C#" + "I want a change to code" + small bug fix (Python bugs, good first issue)
gh search issues --label bug --label "good first issue" --language python --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "Python, JavaScript/TypeScript, and Java/C#" + "I want a change to code" + small bug fix (TypeScript bugs, good first issue)
gh search issues --label bug --label "good first issue" --language typescript --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "I want a change to code" + about 8 to 10 hours + any change type (tests, small features) (Python, help wanted)
gh search issues --label "help wanted" --language python --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "I want a change to code" + about 8 to 10 hours + any change type (tests, small features) (TypeScript, help wanted)
gh search issues --label "help wanted" --language typescript --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "I want a change to code" + about 8 to 10 hours + any change type (tests, small features) (Python, add tests)
gh search issues "tests" --match title --label "good first issue" --language python --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "I want a change to code" + about 8 to 10 hours + any change type (tests, small features) (TypeScript, add tests)
gh search issues "tests" --match title --label "good first issue" --language typescript --state open --no-assignee --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,createdAt,updatedAt,url -- -linked:pr

# Profile: "avoid issues ... that need deep spelunking through a large, legacy codebase"
# No query or ranking filter can check this. The result fields do not show codebase size
# or fix depth. The rubric checks it after the issue page is opened.

## Ranking filters

Apply in this order to the merged, de-duplicated results. Day counts are relative to the scan date.

1. Drop any result with an assignee.
2. Drop any result not updated in the last 90 days (inactive or unresponsive repo).
3. Drop any result with 4 or more comments (crowded thread; comments on a fresh issue are often claims by strangers).
4. Drop any result labelled `feature`, `enhancement` or `feature request` unless it also has `bug`, `help wanted` or `good first issue` (small features are fine when maintainers asked for help; speculative requests are not).
5. Drop any result labelled `hacktoberfest` unless it also has `bug` (mass-produced filler issues add no codebase reading).
6. Drop any result labelled `documentation`, `docs` or `doc` unless it also has `bug` (I want a code change, not a documentation-only change).
7. Drop any result with a label that contains `covered-by-pr`, `in-progress`, `in progress`, `wip`, `claimed` or `assigned` (someone is already working on it, even with no assignee set).
8. Drop any result created less than 24 hours before the scan (maintainers have not reacted yet; wait a day).
9. Drop any result whose URL is in the Rejected issues list below (the scout does not remember earlier verdicts, so it must not grade the same issue twice).
10. Keep at most 2 results per repo (one repo must not fill the top five).
11. Order: fewer comments first (0 comments is best). Break ties with newest update first.

Rules 1 and 2 removed nothing in scan 2, because the queries already use `--no-assignee` and `--sort updated`. They stay as a safety net.

## Rejected issues

Add the URL of every issue that a scan or a grade rejected, with the reason. Ranking rule 9 drops these URLs.

- https://github.com/run-llama/llama_index/issues/23667 (open PR #22407)
- https://github.com/jerseycheese/rcv-simulator-va/issues/16 (styling only)
- https://github.com/krizaka/orazaka/issues/29 (configuration across 19 repos)
- https://github.com/Bees-bot/bees-desktop/issues/283 (report only, no PRs accepted)
- https://github.com/projectbluefin/utah-packages/issues/476 (open PRs #627, #633)
- https://github.com/mlcommons/chakra/issues/232 (four tasks in one issue)
- https://github.com/Grit-77/dotline/issues/2 (verification report, not code)
- https://github.com/allenporter/supernote/issues/122 (pure refactor, design open)
- https://github.com/Rekin226/aquascope/issues/346 (claimed, research first)
- https://github.com/luizomf/omxterm/issues/223 (claimed, packaging merged)
- https://github.com/lingdojo/kana-dojo/issues/33150 (filler issue)
- https://github.com/mloda-ai/mloda-registry/issues/1327 (documentation only)
- https://github.com/mloda-ai/mloda-registry/issues/1326 (documentation only)
- https://github.com/mloda-ai/mloda/issues/2325 (documentation only)
- https://github.com/Tencent/teamai-cli/issues/1397 (claimed, PR coming)
- https://github.com/apache/mahout/issues/1507 (open PR #1544)
- https://github.com/apache/mahout/issues/1509 (open PR #1532)
- https://github.com/apache/mahout/issues/1510 (open PR #1561)
- https://github.com/apache/mahout/issues/1472 (open PR #1534)
- https://github.com/ai-dynamo/dynamo/issues/14069 (open PRs #14689, #17027)

## How many to grade

Grade the top **5** ranked results per scan.

<!-- Five is the default because grading is the only stage that costs
money: about $0.20 per candidate, so a scan is about $1, and you can
iterate the strategy several times for less than one full regression
run. You need one good issue, not ten. Raising this number is
allowed, but it is a decision you state here in a sentence, with the
cost you are accepting; it is not a number you bump because a scan
disappointed you once. -->
