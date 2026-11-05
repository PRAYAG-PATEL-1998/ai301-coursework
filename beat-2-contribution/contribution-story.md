# Contribution: Update document.title to use Helmet (openedx/frontend-app-authoring#897)

Path: `beat-2-contribution/contribution-story.md`

This file is Assignment 5, and it is graded at the path above; a copy kept anywhere else in
the repository is not read. **Keep every section header below under its exact name** — the
format criteria grade exactly that. Your course repo link is the whole submission: no tool
files and no evidence uploads are part of Assignment 5.

**Contribution Number:** [1]
**Student:** Prayag Patel
**GitHub Username:** PRAYAG-PATEL-1998
**Issue:** https://github.com/openedx/frontend-app-authoring/issues/897
**Pull Request:** https://github.com/openedx/frontend-app-authoring/pull/3345

One repository, built across units 5 to 8, telling the whole story of your real
contribution. Fill it as you work, not at the end — the sections below ask for evidence that
is far easier to write down as it happens than to reconstruct in the last weekend.

Contribution Number stays `[1]` unless you make more than one contribution this term; it
just numbers them.

---

## Toolkit

Every story section below, from Why I Chose This Issue through Pull
Request, ends with a Toolkit block: which tool did that phase's work
and how you used it, what it produced, what difficulties or
shortcomings it presented, and what you changed or would change
because of them. Together the blocks are the thread the rubric's
Toolkit points read, and they are the raw material for your unit-9
portfolio, so keep them current as you work rather than
reconstructing them later.

A Toolkit block looks like this (copy it into each story section and
fill it there):

```text
**Toolkit**

- Tool: [which tool did this phase's work, and how you used it]
- What it produced: [described in a sentence or a short excerpt]
- Difficulties: [what fought you or fell short, or "none met"]
- What changed: [the patch, revision, or workaround, what you would
  update, or "nothing"]
```

This section also keeps one short dated entry per week of tool work,
starting below: what you built or changed that week, what broke, and
what you changed because of it. The blocks tell the story where it
happened; these entries are the toolkit's own timeline.

All four entries are graded. Keep every heading below, and fill each
one in the week it belongs to.

**Unit 5: Installed the issue-scout and patched its rubric and search strategy after five scans**

I installed the issue-scout over my unit 1 skill (inside my course repo), wrote a 15-query search strategy and ranking rules from my fit profile, ran five scans, and graded six issues directly. The first scan accepted five issues that were documentation-only, filler, or already claimed, so I added a `code-change` check and a tighter `unclaimed` rule. Later scans kept grading the same rejected issues and missed that `dismech` auto-closes fork PRs, so I added an `outsider-pr` check and a rejected-URL list. It still falls short: the ranking cannot see a PR named only in an issue's text or a repo's AI policy (`beets` bans AI on good first issues), and `maintainer-responsive` wrongly failed `music21` by counting only comments on closed issues, although its outside PRs get a first reply in about 12 minutes. I did not re-run a scan after the last fixes, so they are untested.

**Unit 6: Installed the voice guard, wrote my voice guide and the repo-memory file, and found a Windows bug in the guard**

I wrote a voice guide of twelve rules plus an "Upstream" section, installed the voice guard as a Claude Code hook, and wrote `CLAUDE.local.md` for the openedx clone after reading the repo's `AGENTS.md`, its PR template and the org-level AI policy. My wiring test only tried a `gh issue comment --help` command, which the guard stops before it calls `claude`, so it never ran a real voice check. When I later ran the ship-gate, I found that both scripts start `claude` by its bare name, which fails on Windows because the npm install is a `.cmd` file. I patched both to use `shutil.which("claude")`. On 2026-11-02 the voice guard ran its first real check, on my progress comment for the issue. It stopped the comment because the comment had no AI disclosure line. I added the line, the guard passed the comment, and I posted it.

**Unit 7: Ran the ship-gate on my real branch and fixed what stopped it**

My manifest runs `oxlint`, `npm run types` and the Jest suites for the seven pages; `make` is not installed here and `dprint` flags every CRLF file, so the full lint and `make validate` sit in the excluded table with dated reasons. The first gate run passed all three repo checks and then stopped on the missing `claude` path. After my fix the second run ended with PASS, and `pr-precheck` passed nine checks. It also asked for proof behind "no other title writes remain", which I added to the PR description. I changed the PR text after that, so the pass was void. The gate ran again on `gh pr create` on 2026-11-04. The three repo checks passed, but `pr-precheck` rejected the first try: the description said I had checked the tab titles in a running Studio, and my `test_evidence.md` still said "not tested". I recorded my own Studio check in the evidence file and ran the command again. The gate then let the PR open.

**Unit 8: Read my PR's state with the app's PR monitor and drafted the replies I need while the agreement is pending**

After I opened PR 3345 on 2026-11-04, I read its state with the desktop app's PR status instead of polling `gh pr checks`. It showed the PR open and mergeable, review required, and no CI checks started. I pasted the `openedx-webhooks` bot comment into Claude Code. It explained each step in the bot's checklist and drafted a short message for the agreement contact, and I read the draft before I used it. I then wrote a playbook (`tools/pr-monitor/playbook.md`): nine fixed rules (the monitor is read-only, I decide every post, the voice guard always runs, I do not tag the maintainer before the agreement and CI are green) and a table of eleven events with the draft and my decision rule for each. I ran it once as a dry run on the bot comment; it told me to send the contact message and post nothing on the PR. Gap: no reviewer has replied yet, so the review rows are untested, and the wait times in the table are starting guesses.

---

## Why I Chose This Issue

I wanted a real code change, not a docs fix, in an active project, using JavaScript, TypeScript and React, which is my stack. I also wanted a task with a small, clear scope that I could finish and test myself. Issue #897 in `openedx/frontend-app-authoring` ("Update document.title to use Helmet") fits that. The scope is one pattern in seven named files, and the issue points to a page that already uses it (`CourseExportPage`). I know which files change, what the change is in each one, and how to test it, so one PR can finish the job. The repo is active (a human commit on 2026-10-28), it accepts pull requests from forks, it has a PR template and an `AGENTS.md`, and the Open edX AI policy allows Claude with disclosure. The maintainer answered my claim the same day and asked for one PR for all seven pages, so the scope was agreed before I wrote code. I wrote a search strategy and a fit profile for my issue-scout, ran five scans and graded the best picks. Six of the seven required checks passed for this issue.

The scout's verdict on this issue was `reject`, and I chose it anyway. The reason: the failed check was `unclaimed`, and its only evidence was my own claim comment, so the scout counted my claim as someone else's. That is a flaw in my scout, and I logged it in `scan-notes.md`. The preferred `maintainer-responsive` check also failed because the three most recent closed issues had no comments, but the maintainer on this issue replied the same day I claimed it. I read the whole thread and the AI policy myself before I went on. What I hope to learn: how a large project like Open edX wants a contribution shaped and disclosed, and how to write tests that fail first.

An honest read of the tool: the scout found this issue, but it cannot tell a stranger's claim from my own, it cannot read gatekeeping in a thread, and its responsiveness sample misses issues whose maintainers reply in other places. I would ignore comments by the contributor themselves in `unclaimed`, and sample recent pull requests for `maintainer-responsive`.

**Claim comment:** https://github.com/openedx/frontend-app-authoring/issues/897#issuecomment-6407952859 (posted 2026-10-26). A maintainer, bradenmacdonald, answered the same day: "Please open one PR for all seven and anything else related to the titles."

**Other claims:** I also claimed `MudBlazor/MudBlazor#13128` (https://github.com/MudBlazor/MudBlazor/issues/13128#issuecomment-6407937699) and `nusmods/nusmods#3060` before I chose this issue. I chose openedx#897 because it met six of the seven required checks in my issue-scout rubric, and the maintainer answered my claim the same day with a clear scope. I am not working on the other two now, and I have not changed my claim comments on them.

**Earlier claim, stepped back:** I first claimed `cuthbertLab/music21#1659` (https://github.com/cuthbertLab/music21/issues/1659#issuecomment-6407296177). A maintainer answered that they would decline help from someone without music or MIDI percussion experience, so I stepped back (https://github.com/cuthbertLab/music21/issues/1659#issuecomment-6407356079) and chose this issue instead. The scout could not see that kind of gatekeeping before the claim.

**Toolkit**

- Tool: issue-scout, with my 15-query search strategy and my rubric. I ran five scans and then graded this issue directly.
- What it produced: a `reject` verdict, from `unclaimed` (unclear) and the preferred `maintainer-responsive` (fail). The other six required checks passed.
- Difficulties: `unclaimed` counted my own claim comment as a claim, and `maintainer-responsive` sampled closed issues with no comments.
- What changed: I logged both as scout flaws in `scan-notes.md`. I did not yet patch the rubric. The fix I would make is to ignore the contributor's own comments in `unclaimed`.

---

## Understanding the Issue

**Problem Description**

Issue #897 says that the Studio authoring app sets the browser tab title in two different ways. Most pages use the `react-helmet` component, which declares the title in the page's JSX. Seven pages still assign `document.title` by hand during render (or in an effect). Course Authors see the same tab title either way, so nothing is visibly broken. The problem is in the code: two ways to do one job make the code inconsistent and harder to read and control. The issue asks to move those seven pages to `<Helmet><title>…</title></Helmet>`, as `CourseExportPage` does, so every page sets its title the same way.

**Expected Behavior**

Each page renders `<Helmet><title>…</title></Helmet>`, as `CourseExportPage` does, and the tab title text stays the same.

**Current Behavior**

The seven pages write `document.title` directly: `PagesAndResources`, `CustomPages`, `FilesPage`, `ScheduleAndDetails`, `CourseTeam`, `CourseUnit` and `GroupConfigurations`. The tab already shows the right text, so nothing is visibly broken. In a test, `Helmet.peek()` is `undefined` on six of the seven pages.

**Affected Components**

`src/pages-and-resources/PagesAndResources.tsx`, `src/custom-pages/CustomPages.tsx`, `src/files-and-videos/files-page/FilesPage.jsx`, `src/schedule-and-details/index.tsx`, `src/course-team/CourseTeam.tsx`, `src/course-unit/CourseUnit.tsx`, `src/group-configurations/index.tsx`. The helper `getPageHeadTitle` in `src/generic/utils.js` stays as it is.

**Toolkit**

- Tool: Claude Code with the repo's `AGENTS.md` and my `CLAUDE.local.md`; `gh issue view` for the thread.
- What it produced: the list of the seven files from a search for `document.title`, and a map of which pages already use Helmet.
- Difficulties: the issue text says "add intl for the page name", but all seven pages already use `intl`. I only found this by reading the code, and I corrected my claim comment's promise of new messages in the plan.
- What changed: the plan adds no new messages.

---

## Reproduction Process

**Environment Setup**

Windows 11 Home, Node v24.22.2 (the repo's `.nvmrc` says 24; I installed it with fnm next to Node 22), npm 11.6.2, upstream `master` at `a3a7e085`. I forked `openedx/frontend-app-authoring`, cloned my fork to `C:\Users\praya\Desktop\frontend-app-authoring`, added an `upstream` remote and ran `npm ci`. I did not run Studio or Docker or Tutor for the reproduction, so it is at code and test level only. I checked the result in a running Studio by hand later (see Testing Strategy). Challenges: `npm ci` and the first test run are slow on this PC (9 suites took 7.5 minutes), and `make` is not installed, so I run the parts of `make validate` by hand.

**Steps to Reproduce**

1. `git clone` my fork and `git checkout a3a7e085`, then `npm ci`.
2. `git grep -n "document.title" -- src` finds 7 direct writes, the 7 files in the issue.
3. Add one test per page that reads `Helmet.peek().title` (the call `CourseExportPage.test.tsx` uses).
4. `TZ=UTC npx fedx-scripts jest --silent -t "sets the page title through Helmet" <the 7 test files>`
5. Observed: six tests fail with `TypeError: Cannot read properties of undefined (reading 'title')`. The seventh, for `GroupConfigurations`, passes because that page already renders a `<Helmet>`.

**Reproduction Evidence**

- **Commit showing reproduction:** my fork branch `fix/897-helmet-document-title`: https://github.com/PRAYAG-PATEL-1998/frontend-app-authoring/tree/fix/897-helmet-document-title. Each commit holds a page's new test and its fix together, so to see a test fail, run the new test files against the base commit `a3a7e085`.
- **Screenshots/logs:** the failing output is in my local `test_evidence.md`; the same lines are in the PR description.
- **My findings:** the pattern issue reproduces in code and in tests. There is no visible bug: the tab title text is already correct. I could not look at the tab in a running Studio during the reproduction. I did that check by hand after the fix, and the titles were correct.

**Toolkit**

- Tool: `repro-check` (my skill), plus Claude Code to run `git grep` and Jest.
- What it produced: a repro report in `repro-draft.md`. `repro-check` first rejected it for three reasons (steps with no file names, output described but not pasted, no AI disclosure line). After I fixed those it graded all six checks pass and `accept`.
- Difficulties: the issue names a code pattern, not a failure message, so the "behavior matches" check needed pasted `git grep` output and the exact `TypeError`.
- What changed: the report now pastes the real output and names the test files.

---

## Solution Approach

**Analysis**

These seven pages were written before the Helmet pattern spread. Six set `document.title = getPageHeadTitle(...)` during render and `CourseUnit` sets it in a `useEffect`. `GroupConfigurations` does both: it writes `document.title` and also renders a `<Helmet>`. About 30 other pages already use `<Helmet><title>`. I confirmed the cause in the code and with the failing tests.

**Proposed Solution**

In each page's main return, render `<Helmet><title>{getPageHeadTitle(name, intl.formatMessage(messages.x))}</title></Helmet>` and delete the `document.title` line. In `CourseUnit` delete the title `useEffect` and its unused import. In `GroupConfigurations` delete only the duplicate line. Not changing: `getPageHeadTitle`, any messages, other pages, and the loading and permission-denied returns (the three already migrated pages do not have a Helmet there either; I ask the maintainers in the PR).

**Implementation Plan**

1. Add one test per page in its existing test file, and see it fail on the old source.
2. Replace `document.title` with `<Helmet>` in `PagesAndResources`, `CustomPages`, `FilesPage`, `ScheduleAndDetails`, `CourseTeam` and `CourseUnit`.
3. Remove the duplicate `document.title` in `GroupConfigurations`.
4. One commit per page (test and fix together), Conventional Commits with a `Co-Authored-By` trailer for Claude.

Deviations: my first plan tested `GroupConfigurations` on its permission-denied path, which would fail before the fix. I changed it to the normal render, because the repo's migrated pages set the title only in the main return. That test now passes before and after the fix, and the PR says so. My claim comment promised new messages; none were needed.

**Toolkit**

- Tool: `plan-check` (my skill).
- What it produced: `plan.md` and `plan-comment.md`. It first held back the plan comment because the maintainer's line had two parts ("one PR for all seven and anything else related to the titles") and the draft answered only the first. I searched `src` and `plugins` for other title writes, found none, and added that to the plan and the comment. All seven checks then passed.
- Difficulties: the course says the plan comment is never posted, so the maintainer question moves into the PR description.
- What changed: the plan now has a "Maintainer direction" section.

---

## Testing Strategy

Re-run of the reproduction steps. Before the fix, `TZ=UTC npx fedx-scripts jest --silent -t "sets the page title through Helmet" <the 7 test files>` gives 6 failures, each `TypeError: Cannot read properties of undefined (reading 'title')`. After the fix, `npx fedx-scripts jest --silent` on the seven page folders gives 48 suites and 435 tests passed. Baseline before any change: 9 suites, 192 tests passed. `npm run types` passes, `oxlint --type-aware --deny-warnings` reports 0 warnings and 0 errors, and `dprint check` on my 14 changed files exits 0.

Not run: the full `npm run lint` (dprint flags about 2,000 files for CRLF line endings on Windows), `make validate` and the full Jest suite. I checked the tab titles by hand in a running Studio on my branch, and they were correct; Claude Code did not see that check. The `GroupConfigurations` test passes before and after, so it guards the title but does not prove the fix.

**Toolkit**

- Tool: the ship-gate and `pr-precheck`.
- What it produced: on my real branch it ran lint, types and the tests, then `pr-precheck`, and ended with PASS (9 checks pass). It also gave four notes: add proof for "no other title writes remain", soften "no visible change expected", state that no new messages were needed, and explain the baseline suite count.
- Difficulties: the first run stopped with "the claude CLI is not on PATH". On Windows the npm install of `claude` is a `.cmd` file, and Python's `subprocess` cannot start it by the bare name. The voice guard has the same call.
- What changed: I changed both scripts to call `shutil.which("claude")`, kept backups, and mirrored the fix into the toolkit. I moved `npm run lint` to the manifest's excluded table and use `oxlint` as the lint check, with the reason written down.

---

## Implementation Notes

**2026-10-30**

Set up: Node 24 with fnm, fork, clone, `npm ci`, baseline tests (9 suites, 192 tests). Wrote one failing test per page. My first `CourseUnit` test used `findByText`, which matched two elements, so it failed for the wrong reason; I switched to `findByTestId('unit-header-title')`, as the nearby test does. Read how the migrated pages handle early returns, and chose to follow them (Helmet in the main return only). Made 7 local commits, one per page. Added the `Co-Authored-By` trailer after the Open edX AI policy asked for it. Ran the ship-gate by hand: it stopped on the Windows `claude` path problem, I fixed it, and the second run passed.

**2026-11-02**

My commits showed the author name `PrayagCodes`. I set a repo-local `user.name` and `user.email` to my GitHub identity, rewrote the history in the clone and in this course repo (backup branches kept), and checked through the GitHub API that every commit shows `PRAYAG-PATEL-1998`. I pushed the branch to my fork. The Open edX DocuSign email did not arrive after I filed the contributor form on 2026-10-30, so I posted a progress comment on the issue (https://github.com/openedx/frontend-app-authoring/issues/897#issuecomment-6583586480). The voice guard stopped my first draft because it had no AI disclosure line; I added one and the comment posted. The agreement contact asked if I contribute for my university, because my GitHub account uses my ASU email. I answered no, gave a personal email, and signed the agreement.

**2026-11-04**

I received the go-ahead to open the PR. I checked the tab titles by hand in a running Studio. I opened the PR (https://github.com/openedx/frontend-app-authoring/pull/3345) through Claude Code. The ship-gate ran on the command (see Unit 7).

**Toolkit**

- Tool: Claude Code with `CLAUDE.local.md`, and the ship-gate.
- What it produced: the seven commits and the gate PASS.
- Difficulties: slow tests on Windows, CRLF line-ending noise from dprint, and the `.cmd` path problem.
- What changed: the Windows fix in the gate and the voice guard, and a manifest that uses `oxlint` plus a dated excluded row for the full lint.

---

## Pull Request

**PR Link:** https://github.com/openedx/frontend-app-authoring/pull/3345 (opened 2026-11-04, branch `PRAYAG-PATEL-1998:fix/897-helmet-document-title`, base `master`)

**PR Description:** Title: "refactor: set the page title with Helmet on seven pages". It follows the repo's PR template. It says that seven pages move from `document.title =` to `<Helmet><title>…</title></Helmet>` with the same title text, lists the change for each page, and gives `git grep` output that shows no other direct title writes remain. It says no new messages were needed (a change from my first comment on the issue). The testing steps give the Jest command (48 suites, 435 tests) and the six tests that fail before the change. It says I checked the tab titles in a running Studio. It lists the checks I ran and the ones I did not, asks the maintainers one question (should the loading and permission-denied returns also set a title?), and ends with the AI-use paragraph and the checklist. `Closes #897`.

**Maintainer Feedback:**

- 2026-10-26: the maintainer bradenmacdonald answered my claim: "Please open one PR for all seven and anything else related to the titles." I searched `src` and `plugins` for other title writes, found none, and put the proof in the PR description.
- 2026-11-04: the `openedx-webhooks` bot replied on the PR. It lists four steps (product approval, context, signed agreement, green build). The `openedx/cla` check fails with "We need a signed Contributor Agreement", and four workflows wait for a maintainer to approve them. I asked the agreement contact to check that my username is recorded. I do not tag the maintainer until the agreement check is green.

**Status:** Awaiting review. The PR is blocked on the `openedx/cla` check and on approval of the first-time CI runs.

**Toolkit**

- Tool: the ship-gate hook with `pr-precheck`, run by Claude Code on `gh pr create`.
- What it produced: on the real command it ran `oxlint` (ok), `npm run types` (ok) and the Jest tests for the seven pages (ok, 103 s). Then `pr-precheck` rejected the first try on `description-true-to-diff`: the PR said "checked in a running Studio" but `test_evidence.md` said "not tested". After I recorded my Studio check, the second run passed and the PR opened as number 3345.
- Difficulties: the hook cannot expand a shell variable in the `--body-file` path, and it reads the folder where the session started, not my clone, so the first three attempts stopped with an error.
- What changed: I used a literal body-file path and moved the session into the clone. I did not bypass the gate. I updated the evidence file so it matches the PR text.

---

## Learnings and Reflections

**Technical Skills Gained**

- JavaScript, TypeScript and React: how `react-helmet` works and why it beats `document.title =`. The title is declared in JSX, Helmet applies it, and I removed a `useEffect` that only set the title in `CourseUnit`.
- Jest and React Testing Library: `initializeMocks`, the custom `render()` and `findByTestId` from `src/testUtils.tsx`, and `Helmet.peek().title` to read the title in a test.
- Unit testing and TDD: I wrote one test per page first and saw it fail on the old source for the right reason (`Helmet.peek()` was `undefined`). Then I made the change. I also found that the `GroupConfigurations` test passes before and after, and I said so in the PR.
- Node: managing Node 24 with fnm, `npm ci`, running Jest with `TZ=UTC`, and finding why the same tests can differ between my PC and CI.
- Code comprehension: I read `AGENTS.md`, the PR template and the org AI policy before I changed code. I followed patterns the maintainers already merged (`CourseOutline`, `VideosPage`), and I traced the early returns of those pages. That showed the duplicate `document.title` in `GroupConfigurations` and the title `useEffect` in `CourseUnit`.
- Open source practice: Conventional Commits and small commits, a clear AI-use disclosure, and a plain statement of what I did not test.

**Challenges Overcome**

- The tests are slow on Windows (9 suites took 7.5 minutes), so I ran only the folders I touched.
- `dprint` flagged about 2,000 files for CRLF line endings. I checked my own 14 files after converting them to LF and wrote the full lint into the manifest as a dated excluded check.
- My first `CourseUnit` test failed for the wrong reason (two matching elements). I fixed the query so it failed for the right reason, `Helmet.peek()` undefined.
- The ship-gate and the voice guard could not start `claude` on Windows. I patched both scripts and kept the fix in my toolkit.
- The issue said to add `intl` messages, but the pages already had them. I found that by reading the code and corrected my plan.
- My commits showed the author `PrayagCodes`, not my GitHub name. I set a repo-local identity, rewrote the history with backups, and checked the result through the GitHub API.
- The Open edX contributor agreement took several days. The DocuSign email did not arrive, and the agreement contact asked whether my ASU email meant I contribute for my university. I answered no, gave a personal email and signed. The `openedx/cla` check on the PR can still fail until the contact records my username.

**What I'd Do Differently Next Time**

I would claim one issue, not three. Claiming three at once left me with two public claims to clean up. I would read the thread and the AI policy before claiming, and I would check that my tools run on my operating system on day one, because the Windows `claude` path bug cost time late in the project. I would also fix the scout's `unclaimed` check to ignore my own comments before the next scan.

---

## Resources Used

- CodePath AI301 units 5 to 7 (the issue-scout, claim, voice guard, repo memory, plan, ship-gate and PR steps): https://courses.codepath.org/courses/ai301/unit/5, https://courses.codepath.org/courses/ai301/unit/6, https://courses.codepath.org/courses/ai301/unit/7
- The repo's `AGENTS.md` (setup, commands, conventions, testing rules): https://github.com/openedx/frontend-app-authoring/blob/master/AGENTS.md
- The Open edX AI Contribution Policy (disclosure and "understand what you submit"): https://github.com/openedx/.github/blob/master/AI_POLICY.md
- The repo's PR template and best-practices checklist: https://github.com/openedx/frontend-app-authoring/blob/master/.github/pull_request_template.md
- `CourseExportPage` and its test, the pattern I followed for `<Helmet>` and `Helmet.peek().title`: https://github.com/openedx/frontend-app-authoring/tree/master/src/export-page
- The issue thread, where bradenmacdonald asked for one PR for all seven pages: https://github.com/openedx/frontend-app-authoring/issues/897
- My pull request: https://github.com/openedx/frontend-app-authoring/pull/3345
- The Open edX contributor agreement (individual form): https://openedx.org/cla
