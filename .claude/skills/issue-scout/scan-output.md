# Scan output

## Scan 1: 2026-10-25 (`issue-scout: run a scan`)

Ran all 7 queries from search-strategy.md (683 unique issues after dedup), applied the 6 ranking filters (505 survived the drop conditions, 299 after the per-2-per-repo cap), and graded the top 5 against rubric.md.

All 5 graded candidates verdict accept — ranked below by fit (profile: Python/JS/TS/Java, OSS-workflow learning, avoid deep legacy spelunking, avoid dead repos):

1. mloda-ai/mloda-registry#1327 (https://github.com/mloda-ai/mloda-registry/issues/1327) — replace leftover em/en dashes in docs. Surfaced by gfi-python (good-first-issue+python). Exact file/line pointers, acceptance criteria, tox gate, zero comments, active human commits within the hour, release yesterday. Best fit: bounded, Python tooling, teaches the workflow without deep spelunking.
2. mloda-ai/mloda-registry#1326 (https://github.com/mloda-ai/mloda-registry/issues/1326) — same repo, same quality (docs wording fix). Surfaced by gfi-python.
3. mloda-ai/mloda#2325 (https://github.com/mloda-ai/mloda/issues/2325) — list optional pip extras on the install page. Surfaced by gfi-python. Needs slightly more domain understanding (dependency extras) but still well-scoped with clear acceptance criteria.
4. Tencent/teamai-cli#1397 (https://github.com/Tencent/teamai-cli/issues/1397) — missing request timeout on a GitHub-org-import path. Surfaced by bug-hw-typescript. Real bug, clean repro, active repo (6.6k⭐, releases days old) — but flagged: a contributor already posted a detailed investigation + 3-step implementation plan + "will open the PR shortly." The rubric's unclaimed check passes this by its literal wording (no PR formally open yet), but I'd treat it as effectively claimed — confirm on the issue before starting, or skip.
5. lingdojo/kana-dojo#33150 (https://github.com/lingdojo/kana-dojo/issues/33150) — add one hardcoded anime-quote JSON entry. Surfaced by gfi-typescript. Passes every required check, but it's a mass-produced Hacktoberfest filler issue (numbered #423, templated body, "up for grabs, auto-assign") with zero codebase engagement — technically bounded, practically no learning value for your stated goals. Ranked last on purpose.

No candidates were rejected outright this scan — all 5 passed every required check. The two tension points above (farm-style issues sliding through scope-fits, and a thin claim-comment carve-out in unclaimed) are logged in scan-notes.md as rubric patches worth making, not overrides I applied here.

```json
[
  {
    "item": "https://github.com/mloda-ai/mloda-registry/issues/1327",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "TKaltofen committed 2026-10-26T01:16:45Z, within the hour"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "not archived; pushed 2026-10-26T01:21:02Z; release 2026-10-25T10:37:48Z"},
      {"name": "scope-fits", "grade": "pass", "evidence": "body lists exact files/lines to edit, one deliverable, acceptance criteria, tox gate"},
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: [], comments: [] (none)"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "no AI ban in CONTRIBUTING.md; AGENTS.md present (agent-friendly signal)"},
      {"name": "maintainer-responsive", "grade": "pass", "evidence": "sibling issues (#1321, #1317, #1312) closed same day they were opened"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/mloda-ai/mloda-registry/issues/1326",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "same repo, commits within the hour"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "same repo facts as #1327"},
      {"name": "scope-fits", "grade": "pass", "evidence": "body lists exact README/doc lines to reword, one deliverable, acceptance criteria"},
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: [], comments: [] (none)"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "same repo CONTRIBUTING.md, no ban"},
      {"name": "maintainer-responsive", "grade": "pass", "evidence": "same repo's recent issues close same day"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/mloda-ai/mloda/issues/2325",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "TKaltofen committed 2026-10-26T00:26:21Z"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "not archived; pushed 2026-10-26T00:26:23Z; release 2026-10-25T16:02:31Z"},
      {"name": "scope-fits", "grade": "pass", "evidence": "body names exact page/section and pyproject.toml extras to document, with acceptance criteria"},
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: [], comments: [] (none)"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "same org, no AI ban found"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "no comment thread sampled to confirm first-reply latency"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/Tencent/teamai-cli/issues/1397",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "5 commits by distinct humans in the last day (peremunoz, aryansinha1908, etc.)"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "not archived; pushed 2026-10-25T23:34:50Z; release 2026-10-21T06:59:15Z; 5653 stars"},
      {"name": "scope-fits", "grade": "pass", "evidence": "body names exact file/line (gh-org.ts:26) and the fix shape (pass timeoutMs through ghExec)"},
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: []; one comment is a claim with a plan but no PR is formally open yet, which the rubric's carve-out does not fail by itself"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "no CONTRIBUTING.md or AI_POLICY.md found (404) — silence passes"},
      {"name": "maintainer-responsive", "grade": "pass", "evidence": "sampled closed issues (#1393, #1378, #1377) got same-day comments/closure"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/lingdojo/kana-dojo/issues/33150",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "tentoumushii committed 2026-10-26T01:15:57Z"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "not archived; pushed 2026-10-26T01:15:58Z; 3718 stars"},
      {"name": "scope-fits", "grade": "pass", "evidence": "body is a single bounded edit (append one JSON object to anime-quotes.json)"},
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: []; one comment is a maintainer invite to claim, not a claim itself"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "no AI mention in CONTRIBUTING.md or CONTRIBUTING-BEGINNERS.md"},
      {"name": "maintainer-responsive", "grade": "pass", "evidence": "collaborator tentoumushii commented same minute the issue was opened"}
    ],
    "verdict": "accept"
  }
]
```

---

## Scan 2: 2026-10-25 (`issue-scout: run a scan`, after rubric and strategy changes)

Search and ranking are finished: 1,344 unique results narrowed to a top 5. Next I'm grading those five against the rubric, starting with the issue threads and repo facts.

Two of the five candidates are accepted, mloda-registry #1333 and rcv-simulator-va #16. I'd take #1333 first.

The scan ran all 15 strategy queries and returned 1,344 unique issues. The filters cut that to 1,104: 54 had 10 or more comments, 118 were hacktoberfest filler and 68 were docs-only. The assignee and 90-day filters removed nothing, because the queries already ask for --no-assignee and sort by recent updates. After the two-per-repo cap, I graded the top 5.

Accepted, in fit order

1. mloda-ai/mloda-registry #1333: remove the deprecated RejectionReasonMixin and input_columns_and_framework aliases, plus their two pin tests.
   - Fit: It's a Python code change with exact file pointers and a written definition of done (tox passes). It's well inside a weekend.
   - Checks: All required checks pass.
     - The last 5 default-branch commits are all human and under 1 day old.
     - Latest release is 2026-10-25.
     - There are no assignees. The only open PR (#1332) is unrelated.
     - CONTRIBUTING.md has no AI ban, and the repo has an AGENTS.md written for AI agents.
   - Surfaced by: query 1 (Python good first issue). It ranked 2nd on newest update, with 0 comments.
   - Caveats: The repo is tiny (6 stars). I didn't sample first-response times, so the preferred check maintainer-responsive is ungraded.
2. jerseycheese/rcv-simulator-va #16: bump the rank <select> to about 44px on mobile.
   - Fit: It's a TypeScript/CSS change in one named file, Simulator.tsx plus globals.css, with a clear scope and out-of-scope list.
   - Checks: All required checks pass.
     - The owner's commits are from today and 2026-10-16.
     - The last push was today.
     - There are no assignees or PRs.
     - There is no AI policy file.
   - Surfaced by: query 2 (TypeScript good first issue). It ranked 5th, with 0 comments.
   - Caveats: It's a solo project with 0 stars and no releases. The issue is four months old with no comments, so it's the weaker of the two.

Rejected

- Bees-bot/bees-desktop #283 (query 3, ranked 3rd) fails code-change. The task is to run the AppImage on another Linux distro and report back, and the repo doesn't take pull requests (CONTRIBUTING.md). A contributor has also already asked to take it and a maintainer said yes.
- projectbluefin/utah-packages #476 (query 12, ranked 4th) fails unclaimed and scope-fits. Open PRs #627 and #633 are working on it, and it's a 12-package tracking batch from an epic.
- mlcommons/chakra #232 (query 12, ranked 1st) fails scope-fits. It's four separate release-automation tasks, written as "and/or", with no maintainer engagement yet. The opener is a contributor, and the issue was opened under an hour ago.

Friction for scan-notes.md

- Missing filter: The ranking filters can't see the stage/040-covered-by-pr label that sank #476. A drop on labels containing covered-by-pr or in-progress would fix that.
- Fresh issues: Sorting newest-first puts brand-new issues, like #232 and #1333, at the top before anyone has reacted to them.
- Dead filters: Filters 1 and 2 removed nothing, as noted above.

```json
[
  {
    "item": "https://github.com/mloda-ai/mloda-registry/issues/1333",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Last 5 commits by human accounts TKaltofen and HarshRajSinghania, dated 2026-10-25 to 2026-10-26"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; pushed 2026-10-26; latest release 2026-10-25"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One deliverable: remove two aliases and their two pin tests; good first issue; opened by a contributor"},
      {"name": "code-change", "grade": "pass", "evidence": "Removes code in base.py and python_dict_helpers.py plus tests; no behavior-neutral docs-only fix"},
      {"name": "issue-quality", "grade": "pass", "evidence": "Code pointers to files and test names, definition of done: tox passes"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignees; only open PR #1332 is unrelated; no claim comments"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "CONTRIBUTING.md has no AI ban; AGENTS.md exists for AI coding agents"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "First-response times not sampled; issue is under 1 day old"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/jerseycheese/rcv-simulator-va/issues/16",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human owner jerseycheese committed 2026-10-26 and 2026-10-16"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; last push 2026-10-26 (no releases, push within 180 days)"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One bounded UI change; owner-written; good first issue; explicit out-of-scope"},
      {"name": "code-change", "grade": "pass", "evidence": "Resize .rcv-rank-select in Simulator.tsx / globals.css (UI behavior change)"},
      {"name": "issue-quality", "grade": "pass", "evidence": "Names file and selector, states the 44px target and <640px breakpoint"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignees, no comments, no PRs"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "No CONTRIBUTING or AI policy file found; silence passes"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "Issue has 0 comments after 4 months; no sample taken"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/Bees-bot/bees-desktop/issues/283",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human commits by vinayagg and kafle1 on 2026-10-24/25"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-25; release 2026-10-15"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One bounded task (test AppImage on one distro)"},
      {"name": "code-change", "grade": "fail", "evidence": "\"We don't take pull requests... the report is the whole task\""},
      {"name": "issue-quality", "grade": "pass", "evidence": "Clear steps and done criteria, but no code change involved"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignee or open PR; claim comment by MarcBasas was approved by maintainer vinayagg on 2026-10-26, but claim comments alone do not fail the check"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "No AI ban found in CONTRIBUTING.md"},
      {"name": "maintainer-responsive", "grade": "fail", "evidence": "Maintainer reply to the 2026-10-24 claim came about 31 hours later (within 14 days, so passes in rubric terms)"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/projectbluefin/utah-packages/issues/476",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human commits by hanthor on 2026-10-25"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; pushed 2026-10-26"},
      {"name": "scope-fits", "grade": "fail", "evidence": "Checklist of 12 package outputs from factory epic #308, several blocked on other recipes"},
      {"name": "code-change", "grade": "pass", "evidence": "Implements package recipes and source locks"},
      {"name": "issue-quality", "grade": "fail", "evidence": "Multi-package batch, well beyond 8-10 hours"},
      {"name": "unclaimed", "grade": "fail", "evidence": "Open PRs #627 and #633 reference this issue; label stage/040-covered-by-pr"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "AGENTS.md sets AI commit trailers (conditions, not a ban)"},
      {"name": "maintainer-responsive", "grade": "pass", "evidence": "Maintainer approved within 17 minutes of opening"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/mlcommons/chakra/issues/232",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human merges by winstonliu1111 on 2026-10-23 and tushar-krishna on 2026-07-27"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; pushed 2026-10-23"},
      {"name": "scope-fits", "grade": "fail", "evidence": "Four separate CI/release tasks written as \"and/or\", enhancement/feature labels, no maintainer engagement"},
      {"name": "code-change", "grade": "unclear", "evidence": "Fix is CI workflows and release process rather than source behavior"},
      {"name": "issue-quality", "grade": "fail", "evidence": "No expected behavior or file pointers; release design undecided"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignee, no comments, no PRs"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "CONTRIBUTING.md welcomes outside PRs and states no AI ban"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "No comments yet; not sampled"}
    ],
    "verdict": "reject"
  }
]
```

---

## Scan 3: 2026-10-26 (`issue-scout: run a scan`, after the three weak-spot fixes)

issue-scout scan, 2026-10-26

The 15 queries returned 1,500 results, which merged to 1,342 unique issues. The ranking filters dropped 595. Of those, 350 were created under 24 hours ago, 119 were hacktoberfest filler, 69 were docs-only, and 55 had 10 or more comments. That left 747. After the two-per-repo cap, I graded the top 5.

Accepted

1. jerseycheese/rcv-simulator-va#16 (https://github.com/jerseycheese/rcv-simulator-va/issues/16): bump the rank menu touch target to ~44px on mobile
- Surfaced by: q2 (TypeScript, good first issue). It ranked 5th by newest update, with 0 comments.
- Fit: it is a TypeScript/React UI change in a small, single-deliverable issue. The issue names Simulator.tsx and .rcv-rank-select, so it fits a weekend with no deep reading.
- maintainer-alive: the last 5 commits are by jerseycheese, the newest on 2026-10-26.
- repo-in-use: the repo is not archived and was pushed on 2026-10-26.
- ai-contribution-policy: there is no CONTRIBUTING.md and no AI policy. The repo has a CLAUDE.md, which signals the opposite of a ban.
- Caveats:
  - It is a 0-star, solo-maintainer repo, so a review is likely but not proven. Only 1 external PR (#6) exists in the history.
  - The fix is a CSS/sizing change. It passes code-change under the rubric's wording (it is not docs, rename or data), but it is the thinnest "code change" of the five. Consider tightening the rubric if you want logic changes.
  - maintainer-responsive is unclear. The sampled closed issues were all opened by the owner, so there is no external first-response data.

Rejected

Issue: Rekin226/aquascope#346 (https://github.com/Rekin226/aquascope/issues/346): Brazil RNQA water-quality collector
Surfaced by / ranking signal: q12; updated 2026-10-26
Sunk by: unclaimed: the owner told adjenk "it's yours" on 10-17, and adjenk posted work on 10-24. Also a research-first task with an undecided deliverable.

Issue: luizomf/omxterm#223 (https://github.com/luizomf/omxterm/issues/223): Linux x64 AppImage
Surfaced by / ranking signal: q13; updated 2026-10-26
Sunk by: scope-fits: an open invitation for many contributors. The maintainer already merged the packaging and shipped v0.22.0. unclaimed also fails (a 10-22 plan and a maintainer "preserving that implementation lane").

Issue: run-llama/llama_index#23667 (https://github.com/run-llama/llama_index/issues/23667): infer_torch_device() missing XPU
Surfaced by / ranking signal: q1 and q10 (both queries); updated 2026-10-26
Sunk by: unclaimed: the issue body cites PR #22407, which is open and not draft, updated 10-14, with the contributor repeatedly asking for review. The repo is otherwise healthy, and its AI policy is conditions-only, so that check passes.

Issue: Bees-bot/bees-desktop#283 (https://github.com/Bees-bot/bees-desktop/issues/283): run the AppImage on non-Ubuntu distros
Surfaced by / ranking signal: q3; updated 2026-10-26
Sunk by: code-change: "We don't take pull requests… the report is the whole task." unclaimed also fails, since the maintainer told MarcBasas to take it.

Friction for scan-notes.md

- Query 1 and query 10 overlap heavily. Both surfaced llama_index#23667. The same issue also appears across good first issue and bug queries, so the merge step does real work.
- -linked:pr missed the PR mention in the issue body. llama_index#23667 reached the top 5 because PR #22407 was mentioned in the text rather than formally linked. The rubric caught it, but a ranking filter on this would need body text.
- "Good first issue" and "help wanted" don't mean free. Three of the five top results were claimed or already in progress. That fits a "newest update first" ordering: fresh activity on an issue often means someone is working on it. Consider a comments-in-last-14-days filter, or a minimum of 0 comments.
- No search-time filter exists for the report-only pattern ("we don't take pull requests"). The rubric handles it, but it cost a grading slot.

```json
[
  {
    "item": "https://github.com/jerseycheese/rcv-simulator-va/issues/16",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Last 5 commits all by human jerseycheese, newest 2026-10-26"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "archived=false, last push 2026-10-26 (no releases, but push within 180 days)"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One bounded UI fix: 'Give the rank menu a larger hit area at the <640px breakpoint'; opener is repo owner"},
      {"name": "code-change", "grade": "pass", "evidence": "Fix changes `.rcv-rank-select` sizing in src/components/Simulator.tsx / globals.css; not docs, rename or data"},
      {"name": "issue-quality", "grade": "pass", "evidence": "Names file and selector, states ~44px expected target, in/out of scope listed; well under 8-10 hours"},
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees empty, 0 comments, no linked or mentioned PR"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "No CONTRIBUTING.md or AI policy file (404); CLAUDE.md present"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "Sampled closed issues #15, #11, #10 were owner-opened; no external first-response data"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/Rekin226/aquascope/issues/346",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Owner Rekin226 merged PR #642 on 2026-10-25"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived, pushed 2026-10-25, release 2026-10-11"},
      {"name": "scope-fits", "grade": "unclear", "evidence": "Research-first: 'finding out whether machine-readable access exists at all'; deliverable depends on the outcome"},
      {"name": "code-change", "grade": "unclear", "evidence": "'closing this with what was found is a perfectly good outcome', so a code change is not guaranteed"},
      {"name": "issue-quality", "grade": "fail", "evidence": "No confirmed endpoint; the work is exploratory"},
      {"name": "unclaimed", "grade": "fail", "evidence": "Owner on 2026-10-17: 'Yes, it's yours @adjenk'; adjenk posted progress 2026-10-24"},
      {"name": "ai-contribution-policy", "grade": "unclear", "evidence": "Not checked; the issue was already sunk by unclaimed"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "Not sampled; owner replied to this thread after about 4 weeks"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/luizomf/omxterm/issues/223",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human luizomf commits through 2026-10-26"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-26, release v0.22.0 on 2026-10-25"},
      {"name": "scope-fits", "grade": "fail", "evidence": "'Help bring OMXTerm to Linux x64' is an open invitation; maintainer packaging merged in #681/#684 and AppImage shipped"},
      {"name": "code-change", "grade": "unclear", "evidence": "Remaining work is native testing and reports; the packaging code is already merged"},
      {"name": "issue-quality", "grade": "fail", "evidence": "Deliverable is no longer defined; maintainers say native testing is not a prerequisite"},
      {"name": "unclaimed", "grade": "fail", "evidence": "Gaalbu gave a plan 2026-10-22; maintainer 2026-10-24: 'preserving that implementation lane'"},
      {"name": "ai-contribution-policy", "grade": "unclear", "evidence": "Not checked; issue already rejected. The maintainer replies with AI-generated text."},
      {"name": "maintainer-responsive", "grade": "pass", "evidence": "Owner replied to Gaalbu the same day (2026-10-22)"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/run-llama/llama_index/issues/23667",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human commits on 2026-10-14 (gabbyong, mattref, ranst91)"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-23, release 2026-09-21"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One bounded bug: add XPU detection to infer_torch_device()"},
      {"name": "code-change", "grade": "pass", "evidence": "Bug: returns 'cpu' where 'xpu' is expected"},
      {"name": "issue-quality", "grade": "pass", "evidence": "Names function, file lines and a repro script, with expected 'xpu'"},
      {"name": "unclaimed", "grade": "fail", "evidence": "Issue cites PR #22407, which is open and not draft (updated 2026-10-14) with the author requesting review"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "CONTRIBUTING.md: 'We welcome AI-assisted contributions' with transparency and quality conditions"},
      {"name": "maintainer-responsive", "grade": "fail", "evidence": "PR #22407 open since 2026-07-20 with repeated unanswered review pings; issue comment sample not otherwise gathered"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/Bees-bot/bees-desktop/issues/283",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human merges by vinayagg on 2026-10-25"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-25, release 2026-10-15"},
      {"name": "scope-fits", "grade": "pass", "evidence": "Single bounded task: run the AppImage on a distro and report"},
      {"name": "code-change", "grade": "fail", "evidence": "'We don't take pull requests (see CONTRIBUTING.md), so the report is the whole task.'"},
      {"name": "issue-quality", "grade": "fail", "evidence": "The deliverable is a comment, not a change"},
      {"name": "unclaimed", "grade": "fail", "evidence": "Maintainer told MarcBasas 'Please take it' on 2026-10-26"},
      {"name": "ai-contribution-policy", "grade": "unclear", "evidence": "Not checked; the repo takes no PRs"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "Not sampled"}
    ],
    "verdict": "reject"
  }
]
```

---

## Scan 4: 2026-10-26 (`issue-scout: run a scan`, after the scan 3 fixes)

The scan found one acceptable issue out of the five graded: allenporter/supernote #234. The other four were rejected.

The funnel went from 1,500 raw results to 1,340 unique, then to 371 after the ranking filters and the 2-per-repo cap. I graded the top 5 by fewest comments, then newest update. The scan date was 2026-10-25.

Accepted

1. supernote #234, "Attach tags to generated transcripts and AI summaries" (https://github.com/allenporter/supernote/issues/234)
   - Surfaced by: query 1 (Python, good first issue). It had 0 comments, was updated 2026-10-25, and was the second supernote result kept.
   - Why it fits: SummaryModule currently sets tags=None, and the fix is to add default tags on creation. The maintainer wrote the issue and labelled it good first issue. The repo is active: the maintainer's last 5 commits are all from today, and the latest release is 2026-09-12.
   - maintainer-responsive (preferred): not sampled. Every closed issue I looked at was opened by the owner, so the rubric says to sample PRs from other people, which I did not do.
   - Check before you claim: the "Ensure tag records exist in SummaryTagDO if needed" line is vague.

Rejected, in rank order

2. llama_index #23667 (query 1 and 10; 0 comments, updated 2026-10-26) failed unclaimed. The issue body cites PR #22407, which is still open. An earlier PR, #22381, was closed. Everything else passed, including the AI policy, which only sets conditions. The preferred maintainer-responsive check also looks weak: the last 3 closed issues had no comments.
3. rcv-simulator-va #16 (query 2) failed code-change. The whole fix is resizing a select to 44px, which is styling.
4. orazaka #29 (query 3) failed code-change. It is a chore to delete issue templates across repos, with no behavior change.
5. supernote #122 (query 1) failed code-change, graded unclear. It is a refactor to stop passing url through function signatures. The rubric requires a change to logic or behavior, and a pure refactor doesn't clearly meet that.

Friction for scan-notes.md
- Two of the five (#16 and #29) were non-code issues that the ranking filters can't see. Adding chore, ui, css and styling to the drop-label list (filter 6) might help.
- The rubric doesn't say whether a pure refactor counts as a code change. That is why #122 landed on unclear.
- Filter 8 (drop issues created under 24 hours ago) removed about half of the results (1,014 down to 557), which is unusually heavy for a 24-hour rule. That may deserve a look.

```json
[
  {
    "item": "https://github.com/allenporter/supernote/issues/234",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Last 5 commits all by allenporter, 2026-10-26"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; pushed 2026-10-26; release 2026-09-12"},
      {"name": "scope-fits", "grade": "pass", "evidence": "Maintainer-opened, good first issue; one deliverable: default tags in SummaryModule"},
      {"name": "code-change", "grade": "pass", "evidence": "Adds tags='Transcript,OCR' / 'AI Summary,Gemini' on item creation (behavior change)"},
      {"name": "issue-quality", "grade": "pass", "evidence": "States current (tags=None) vs expected tags and names SummaryModule; the SummaryTagDO step is vague"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignee, no linked PRs, 0 comments"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "No CONTRIBUTING/AI policy file found; silence passes"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "Last 3 closed issues all opened by owner; outside-PR sample not taken"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/run-llama/llama_index/issues/23667",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human commits 2026-10-12 to 10-14"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-23; release 2026-09-21"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One bounded fix in infer_torch_device() with repro"},
      {"name": "code-change", "grade": "pass", "evidence": "Add XPU device detection"},
      {"name": "issue-quality", "grade": "pass", "evidence": "Names function and file, gives repro script"},
      {"name": "unclaimed", "grade": "fail", "evidence": "Body cites PR #22407 (Intel XPU support), state OPEN"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "CONTRIBUTING.md: 'We welcome AI-assisted contributions' with disclosure and review conditions"},
      {"name": "maintainer-responsive", "grade": "fail", "evidence": "Last 3 closed issues (#23601, #23583, #23404) show no comments"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/jerseycheese/rcv-simulator-va/issues/16",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Owner commits 2026-10-26 and 2026-10-16"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-26, not archived (no releases)"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One bounded change with scope listed"},
      {"name": "code-change", "grade": "fail", "evidence": "Only resizes a select to ~44px on mobile (styling)"},
      {"name": "issue-quality", "grade": "pass", "evidence": "Names Simulator.tsx and .rcv-rank-select"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignee, no linked PRs, 0 comments"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "No policy found"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "All sampled issues opened by owner"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/krizaka/orazaka/issues/29",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human commits by oussamaABID 2026-10-26"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-26, not archived (no releases)"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One deliverable: remove or update the old issue templates"},
      {"name": "code-change", "grade": "fail", "evidence": "Delete or update .github/ISSUE_TEMPLATE files; chore, no behavior change"},
      {"name": "issue-quality", "grade": "fail", "evidence": "Touches 18 repos; some may not be public"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignee, no linked PRs, 0 comments"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "AGENTS.md present (agent-friendly); no ban"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "Sampled issues opened by bots"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/allenporter/supernote/issues/122",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Last 5 commits by allenporter, 2026-10-26"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-26; release 2026-09-12"},
      {"name": "scope-fits", "grade": "pass", "evidence": "Maintainer-opened, good first issue, one refactor"},
      {"name": "code-change", "grade": "unclear", "evidence": "Pure refactor of url-passing boilerplate in admin.py; no behavior change shown (counts as fail)"},
      {"name": "issue-quality", "grade": "fail", "evidence": "Design is open ('perhaps by...'); no repro"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignee, no linked PRs, 0 comments"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "No policy found"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "Sampled issues opened by owner"}
    ],
    "verdict": "reject"
  }
]
```

---

## Scan 5: 2026-10-26 (`issue-scout: run a scan`, after the rubric changes: `issue-quality` removed, 14-day window)

The scan produced one accepted issue out of five graded: baipix/baipix #530. The other four fail a required check.

Scan: 15 queries returned 1,340 unique issues. The ranking filters cut that to 674, and I took the top 5 by fewest comments, then newest update. Query numbers below are the order in search-strategy.md.

Accepted
1. baipix/baipix #530: "Preview the brush when the Apple Pencil hovers."
   - Surfaced by: query 2 (TypeScript, good first issue). It had 0 comments and was updated 2026-10-26.
   - Fit: it's a TypeScript change to pointer-event handling, a small feature the owner wrote up himself. CONTRIBUTING.md is explicit about conventions and tests, and the owner merges outside PRs within about a day.
   - Caveat: testing needs pen-hover input, probably an iPad, and the repo has 5 stars. Both are in the issue's own text, not rubric failures.

Rejected
2. run-llama/llama_index #23667 (queries 1 and 10) fails unclaimed. The thread names PR #22407, which is still open and was last updated 2026-10-14. This is a good bug in a healthy repo with a policy that welcomes AI-assisted work, but someone is already on it.
3. Grit-77/dotline #2 (query 12) fails code-change. It asks for a manual verification report on a Claude Code channel round trip, not a code change.
4. jerseycheese/rcv-simulator-va #16 (query 2) fails code-change. The fix is CSS touch-target sizing only.
5. krizaka/orazaka #29 (query 3) fails code-change, and likely scope as well. The fix is deleting issue-template files across about 19 repos.

Strategy friction for scan-notes.md
- Filter 8 (drop issues under 24 hours old) removed 337 results. The system clock seems to be about a day ahead of the stated date, so some of those may be older than they look.
- The rubric lets styling-only and config-only issues through the ranking, and they take top-5 slots before grading. Four of the five slots went to issues the rubric rejects. A drop filter on labels like enhancement alone would help only a little, so this probably belongs in the strategy.

```json
[
  {
    "item": "https://github.com/baipix/baipix/issues/530",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Last 5 commits 2026-10-24 to 10-26, by human authors Todo-bai and mykola-lp"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; pushed 2026-10-26; release 2026-10-24"},
      {"name": "scope-fits", "grade": "pass", "evidence": "Owner-opened, one deliverable: show brush preview on pen hover (pointerType pen, no buttons)"},
      {"name": "code-change", "grade": "pass", "evidence": "Needs new pointer-event handling logic for a missing feature"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignees, 0 comments, no linked PR; open PR #551 is an unrelated Ukrainian translation"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "CONTRIBUTING.md states no AI policy"},
      {"name": "maintainer-responsive", "grade": "pass", "evidence": "Sampled closed issues had no comments; owner merged outside PRs #544 and #545 within a day"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/run-llama/llama_index/issues/23667",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human commits 2026-10-14"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-23; release 2026-09-21"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One bug: infer_torch_device() never returns xpu"},
      {"name": "code-change", "grade": "pass", "evidence": "Device-detection logic bug"},
      {"name": "unclaimed", "grade": "fail", "evidence": "Issue body: PR #22407 fixes this; it is OPEN (updated 2026-10-14)"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "CONTRIBUTING.md: 'We welcome AI-assisted contributions' with a disclosure condition"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "Sampled closed issues had no comments to measure first response"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/Grit-77/dotline/issues/2",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human commits by Grit-77 on 2026-10-26"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-26; release 2026-10-26"},
      {"name": "scope-fits", "grade": "pass", "evidence": "Bounded trial with stated acceptance criteria"},
      {"name": "code-change", "grade": "fail", "evidence": "Deliverable is a verification report of a native Claude Code round trip, not a code change"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignees, no comments, no linked PR"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "CONTRIBUTING.md mentions Claude Code hooks only, no ban"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "All sampled PRs are the owner's own"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/jerseycheese/rcv-simulator-va/issues/16",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human commits 2026-10-26 and 10-16"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-26"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One bounded CSS change"},
      {"name": "code-change", "grade": "fail", "evidence": "Only sizing of .rcv-rank-select to about 44px; styling with no behavior change"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignees, 0 comments"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "No CONTRIBUTING.md found"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "All sampled PRs are the owner's own"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/krizaka/orazaka/issues/29",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Human commits by oussamaABID on 2026-10-26"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Pushed 2026-10-26"},
      {"name": "scope-fits", "grade": "fail", "evidence": "Spans about 19 repositories (18 orazaka repos plus orochia)"},
      {"name": "code-change", "grade": "fail", "evidence": "Deleting or updating .github/ISSUE_TEMPLATE files is configuration, not program logic"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignees, 0 comments"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "No CONTRIBUTING.md found"},
      {"name": "maintainer-responsive", "grade": "unclear", "evidence": "Sampled PRs are all bot-authored"}
    ],
    "verdict": "reject"
  }
]
```

---

## Graded pick 1: 2026-10-26 (`issue-scout: grade`, direct mode, from the Issue Selection site)

issue-scout, direct mode: dismech#10458 is an accept. It passes all six required checks.

The issue is "preflight-dr OMIM extractor misses bare-sigil and markdown-emphasis forms". It is open, labeled bug, good first issue, tooling and low-priority, and was opened 2026-09-02. Query: direct. Ranking signals: direct, so none.

| Check | Grade | Evidence |
|---|---|---|
| maintainer-alive | pass | The last 5 commits on main are dated 2026-10-26. They are by human accounts (gingin77, cmungall, caufieldjh). |
| repo-in-use | pass | The repo is not archived. The last push was 2026-10-26, and v0.1.45 was released 2026-10-23. |
| scope-fits | pass | The fix is one deliverable. It changes OMIM_RE in src/dismech/preflight_dr.py and adds tests in tests/test_preflight_dr.py. The numbered steps in the follow-up comment all belong to that one fix. |
| code-change | pass | It is a regex and extraction logic bug that causes false WARNs. It also needs unit tests. |
| unclaimed | pass | There are no assignees and no PR is linked or mentioned. A search for PRs naming 10458 or the OMIM extractor found none. The only comment (github-actions, 2026-09-02) asks @dragon-ai-agent to fix it. That is more than 14 days old and no PR followed. |
| ai-contribution-policy | pass | CONTRIBUTING.md says the repo runs in "heavily agent-forward mode". It has an AGENTS.md and no AI ban. |
| maintainer-responsive (preferred) | fail | I sampled the 3 most recently closed issues (#15614 to #15616), all opened by one user (bpow). The only first replies were from a github-actions bot, which GitHub tags as CONTRIBUTOR, not owner, member or collaborator. The sample is thin, because I looked only at the comment authors. |

Reasons to take it
- The issue names the exact file and line (preflight_dr.py:103) and gives failing inputs.
- The follow-up comment adds test cases to cover and a design hazard to avoid. Gene MIMs (*, +) must stay out of the phenotype comparison, or they produce new false WARNs.
- It fits the weekend budget and the Python/tooling profile, and it is a code change, not docs.

Friction to log in scan-notes.md
- Forks: CONTRIBUTING.md says PRs must come from branches in the main repo, not forks, because the close-fork-prs workflow closes fork PRs. A non-member may not be able to open a PR at all. The rubric has no check for this, so it did not affect the verdict. It could sink the contribution in practice, so confirm push access, for example by asking on the issue, before committing. Consider adding a "can an outsider open a PR" check to the rubric.
- Responsiveness: the maintainer-responsive sample is dominated by bot replies. Consider counting only non-bot replies, or sampling issues opened by other people.
- Claim: if you commit, claim it upstream on the issue first, as scope.md requires.

```json
[
  {
    "item": "https://github.com/monarch-initiative/dismech/issues/10458",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Last 5 main commits dated 2026-10-26 by humans gingin77, cmungall, caufieldjh"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; last push 2026-10-26; v0.1.45 released 2026-10-23"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One deliverable: fix OMIM_RE in preflight_dr.py plus tests; labeled good first issue; numbered steps belong to a single fix"},
      {"name": "code-change", "grade": "pass", "evidence": "Regex/extraction logic bug causing false WARNs; needs behavior change and unit tests"},
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees empty; no PR linked or mentioned; only comment (2026-09-02) is a bot asking @dragon-ai-agent to fix, with no PR since"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "CONTRIBUTING.md: 'heavily agent-forward mode'; AGENTS.md present; no ban"},
      {"name": "maintainer-responsive", "grade": "fail", "evidence": "3 sampled closed issues (#15614-#15616) got first replies only from github-actions bot (CONTRIBUTOR), not owner/member/collaborator; thin sample"}
    ],
    "verdict": "accept"
  }
]
```

---

## Graded picks 2 and 3: 2026-10-26 (`issue-scout: grade`, direct mode)

Both issues are accepted. supernote#234 ranks first for fit, and baipix#530 second.

Both URLs were hand-fed, so I skipped search and ranking and graded each one on its own. I gathered the evidence with gh, measured against today's date.

1. allenporter/supernote #234: attach tags to generated transcripts and AI summaries (accept)
- maintainer-alive: pass. The last 5 commits are all from allenporter, all on 2026-10-26.
- repo-in-use: pass. The repo is not archived, the latest release is 0.23.0 (2026-09-12), and the last push was 2026-10-26.
- scope-fits: pass. The maintainer opened it, it carries the good first issue label, and it asks for one deliverable: default tags in SummaryModule.
- code-change: pass. SummaryModule currently leaves tags=None, so the fix changes logic.
- unclaimed: pass. There is no assignee, no comments and no linked or mentioned PR.
- ai-contribution-policy: pass. docs/CONTRIBUTING.md has no ban and points to "AI Skills & Agentic Coding" under .agent/skills.
- maintainer-responsive (preferred): pass. The 3 latest closed issues were all opened by the owner, so I sampled PRs from other people. The first review came about 11 minutes after #464 was opened, about 47 minutes after #459 and about 35 minutes after #454.

2. baipix/baipix #530: preview the brush when the Apple Pencil hovers (accept)
- maintainer-alive: pass. Recent commits come from Todo-bai and mykola-lp, both human, dated 2026-10-24 to 10-26.
- repo-in-use: pass. The repo is not archived, the latest release is v0.7.6 (2026-10-24), and the last push was 2026-10-26.
- scope-fits: pass. The owner opened it, it carries good first issue and size: small ("A few hours"), and it asks for one deliverable: a hover preview for pointerType pen.
- code-change: pass. It adds a new pointer-event behavior.
- unclaimed: pass. There is no assignee, no comments, and the only open PR (#551, a Ukrainian translation) is unrelated.
- ai-contribution-policy: pass. CONTRIBUTING.md says nothing about AI.
- maintainer-responsive (preferred): pass. The 3 latest closed issues were all opened by the owner, so I sampled PRs from other people. The owner replied on #551 about 32 minutes after it was opened and merged #544 about 80 minutes after it was opened.

Ranking by your fit profile
1. supernote#234:
   - It is Python backend work on an AI tool, and it touches a database model (SummaryTagDO), which matches your stack.
   - The issue names the module and the exact behavior, and the maintainer reviews outside PRs within the hour.
   - The repo is bigger (82 stars, many open PRs), so you will need to read a bit of the codebase.
2. baipix#530:
   - It is a small TypeScript task with a clear contributor guide, and the issue labels it "a few hours".
   - It names no file, only the pointerType condition.
   - Testing it needs a real Apple Pencil on an iPad, or simulated pointer events. The guide also requires French and English strings, a changelog line and tests, so it may run longer than "a few hours".

Neither rubric result felt wrong, so there is nothing to log in scan-notes.md. If you take one, the scope rules say to claim it on the issue right away.

```json
[
  {
    "item": "https://github.com/allenporter/supernote/issues/234",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Last 5 commits all by human allenporter, dated 2026-10-26"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; release 0.23.0 on 2026-09-12; last push 2026-10-26"},
      {"name": "scope-fits", "grade": "pass", "evidence": "Maintainer-opened, 'good first issue', one deliverable: default tags in SummaryModule"},
      {"name": "code-change", "grade": "pass", "evidence": "SummaryModule currently leaves tags=None; fix changes logic"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignees, no comments, no linked or mentioned PRs"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "docs/CONTRIBUTING.md has no ban; references AI Skills & Agentic Coding"},
      {"name": "maintainer-responsive", "grade": "pass", "evidence": "Closed issues owner-only; outside PRs #464/#459/#454 got allenporter review within ~11-47 min"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/baipix/baipix/issues/530",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Last 5 commits by human Todo-bai and mykola-lp, 2026-10-24 to 10-26"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; release v0.7.6 on 2026-10-24; last push 2026-10-26"},
      {"name": "scope-fits", "grade": "pass", "evidence": "Owner-opened, 'good first issue' + 'size: small' (A few hours); one deliverable: pen hover brush preview"},
      {"name": "code-change", "grade": "pass", "evidence": "Adds pointer-event hover preview behavior for pointerType pen"},
      {"name": "unclaimed", "grade": "pass", "evidence": "No assignees, no comments; only open PR #551 is an unrelated translation"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "CONTRIBUTING.md has no AI mention; silence passes"},
      {"name": "maintainer-responsive", "grade": "pass", "evidence": "Closed issues owner-only; outside PRs #551 and #544 got owner comment within ~32-80 min"}
    ],
    "verdict": "accept"
  }
]
```

Added by me after the grade: this read-out has no `outsider-pr` check, because it ran before I added that rule. I checked it by hand with `gh` (read-only). Neither `allenporter/supernote` nor `baipix/baipix` has a fork-blocking workflow, neither `CONTRIBUTING.md` limits PRs to members, and both repos allow forking. Both pass `outsider-pr`.

---

## Graded picks 4 to 6: 2026-10-26 (`issue-scout: grade`, direct mode, from the full site scan)

I graded all three issues against the rubric, and all three are accepted. I ranked them by fit: #1659, then #1234, then #4314. I checked each live with gh, so the dates below are measured against today (2026-10-25).

Ranked read-out (all three came in as direct URLs, so there was no search query or ranking filter)

1. music21 #1659 (percussion pitch lost on MIDI import) is the best fit.
   - It's Python and a good-first-issue. The percussion label and a member's comment give a concrete fix: store the MIDI pitch number in storedInstrument.percMapPitch, which is currently None.
   - It has a clear repro and no assignee. The only cross-reference is from a different repo (notation-hero), so nothing is claimed.
   - The last comment is from 2023, so nobody is active on it.
2. music21 #1234 (support MusicXML attack/release attributes) comes second.
   - It's Python, with example XML and expected output images. The body points at the existing TODOs in xmlToM21.py and m21ToXml.py.
   - The maintainer added the good-first-issue label in April 2022. The opener ticked "I plan on implementing this myself" in 2022, but there is no PR or assignee, so I don't count it as a claim.
   - It's a feature that touches both converters, so it's larger and less certain than #1659.
3. ImprovedTube #4314 (settings restore doesn't persist) is last.
   - It's JavaScript, labeled good first issue and up-for-grabs.
   - Someone already tried to fix it in PR #4319 ("Fix settings restore persistence race"), which was closed unmerged on 2026-10-03. That doesn't fail the unclaimed check, since no PR is open, but it's a warning sign.
   - The report is vague, the thread has no comments, and the repo's first-reply rate is worse than music21's.

Checks that apply to every issue
- Maintainer alive: passes for both repos. Music21's last five commits are from mscuthbert today. ImprovedTube's are human-authored and merged PRs from today.
- Repo in use: passes for both. Neither is archived, both were pushed to today, and their latest releases are 2026-10-22 (music21) and 2026-05-30 (ImprovedTube).
- Outsider PR: passes for both, since there's no fork restriction. Music21's workflows are maincheck and profile_contributors. ImprovedTube's CONTRIBUTING.md just links to its wiki, which I didn't read.
- AI policy: passes for both.
  - Music21 only sets conditions: AI use must be declared in the title, and in 2026 "AI-Assisted contributions" are welcome if you take responsibility for them.
  - ImprovedTube's CONTRIBUTING.md is silent.
- Maintainer responsiveness (preferred, so it only affects ranking): it fails for both. Music21's three most recent closed issues got a first member or owner reply on 1 of 3, and ImprovedTube's on 0 of 3. This counts only comments, so a maintainer closing an issue without a comment shows as no reply. That rule is a likely source of friction worth logging in scan-notes.md.

Per the scope rules, if you take one of these you should comment on the issue to claim it right away.

```json
[
  {
    "item": "https://github.com/cuthbertLab/music21/issues/1659",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Last 5 commits by mscuthbert, newest 2026-10-25"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; pushed 2026-10-25; release 2026-10-22"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One deliverable, labeled good first issue; member comment: preserve MIDI pitch in storedInstrument.percMapPitch (currently None)"},
      {"name": "code-change", "grade": "pass", "evidence": "Lossy MIDI import of percussion pitch is a behavior bug"},
      {"name": "unclaimed", "grade": "pass", "evidence": "Assignees empty; no PR in the Development box; the only cross-reference is a PR in another repo (notation-hero); last comment 2023-12-10"},
      {"name": "outsider-pr", "grade": "pass", "evidence": "No fork restriction in CONTRIBUTING.md or workflows (maincheck.yml, profile_contributors.yml)"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "Conditions only: declare AI use in the title; 'In 2026 we welcome AI-Assisted contributions'"},
      {"name": "maintainer-responsive", "grade": "fail", "evidence": "1 of 3 recent closed issues (#2096, #2083, #2082) has a member/owner comment (#2096, about 4 hours)"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/cuthbertLab/music21/issues/1234",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Last 5 commits by mscuthbert, newest 2026-10-25"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; pushed 2026-10-25; release 2026-10-22"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One feature (attack/release to MIDI); good first issue label added 2022-04-03; body points to the existing TODOs in xmlToM21.py and m21ToXml.py"},
      {"name": "code-change", "grade": "pass", "evidence": "Feature changing MusicXML-to-MIDI output timing"},
      {"name": "unclaimed", "grade": "pass", "evidence": "Assignees empty; no linked or mentioned PRs; no comments; the opener's 2022 'I plan on implementing this myself' checkbox has no PR behind it"},
      {"name": "outsider-pr", "grade": "pass", "evidence": "No fork restriction in CONTRIBUTING.md or workflows"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "Conditions only: declare AI use in the title; AI-assisted welcome in 2026"},
      {"name": "maintainer-responsive", "grade": "fail", "evidence": "1 of 3 recent closed issues has a member/owner comment"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/code-charity/youtube/issues/4314",
    "checks": [
      {"name": "maintainer-alive", "grade": "pass", "evidence": "Merge of PR #4417 by hkzo on 2026-10-25; ImprovedTube2 merging human-opened PRs 2026-10-24"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "Not archived; pushed 2026-10-25; release 2026-05-30"},
      {"name": "scope-fits", "grade": "pass", "evidence": "One bug (restored settings don't take effect), labeled good first issue / help wanted / up-for-grabs; no history of repeated claim/abandon cycles (one closed PR in about 7 weeks)"},
      {"name": "code-change", "grade": "pass", "evidence": "Backup import does not apply the settings; a behavior bug"},
      {"name": "unclaimed", "grade": "pass", "evidence": "Assignees empty; the only linked PR (#4319) is CLOSED, not merged, 2026-10-03; no comments"},
      {"name": "outsider-pr", "grade": "pass", "evidence": "CONTRIBUTING.md only links to a wiki; workflows are build/lint only; PRs from outside contributors are being merged"},
      {"name": "ai-contribution-policy", "grade": "pass", "evidence": "CONTRIBUTING.md is silent on AI (wiki not read)"},
      {"name": "maintainer-responsive", "grade": "fail", "evidence": "0 of 3 recent closed issues (#4418, #4407, #4400) have a maintainer comment"}
    ],
    "verdict": "accept"
  }
]
```
