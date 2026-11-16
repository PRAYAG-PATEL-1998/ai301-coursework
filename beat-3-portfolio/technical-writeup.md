# Moving seven Open edX pages to one way of setting the tab title, and the pre-PR gate that caught my own description

## Overview

Open edX Studio is the web app that course authors use to build courses, and its front end lives in `openedx/frontend-app-authoring`. Issue #897 says the app sets the browser tab title in two ways: about 30 pages declare it with `react-helmet`, and seven pages still assign `document.title` by hand. I moved those seven pages to `<Helmet>`, added one test per page, and opened [PR #3345](https://github.com/openedx/frontend-app-authoring/pull/3345) on 2026-11-04 (14 files, +99 −17). I directed the change and Claude Code wrote the code, as the PR discloses; I chose the test approach, ran the tests myself, and read the full diff. Before the PR could open, it had to pass my ship-gate, a Claude Code hook that runs the repo's own checks and then grades the PR text against the diff. The gate script came with the course. The parts I wrote are the `ship-manifest.md` that tells it which checks to run for this repo, the `pr-precheck` rubric it grades with, and a one-line fix that made it run on Windows. Today the PR is open. The contributor agreement check turned green on 2026-11-16. No maintainer has reviewed the code yet, and CI has not run.

## What happened

### The claim and the scope (2026-10-26)

I claimed the issue and listed the seven files I had found. The maintainer, bradenmacdonald, answered the same day:

> Please open one PR for all seven and anything else related to the titles.

That set the scope before I wrote code. It also gave me a second job: prove that nothing else "related to the titles" was left.

### A failing test for each page (2026-10-30)

The issue names a code pattern, not a visible bug. The tab title text is already right. So I needed a test that fails on the old code for the right reason. `CourseExportPage.test.tsx` reads the title with `Helmet.peek().title`, and I used the same call. This is the test for `CourseTeam`:

```tsx
it('sets the page title through Helmet', async () => {
  axiosMock
    .onGet(getCourseTeamApiUrl(courseId))
    .reply(200, courseTeamMock);

  render();

  await waitFor(() => {
    expect(Helmet.peek().title).toEqual(`${messages.headingTitle.defaultMessage} | ${process.env.SITE_NAME}`);
  });
});
```

On the old source, six of the seven new tests failed with the same line, because those pages mount no `<Helmet>`:

```
TypeError: Cannot read properties of undefined (reading 'title')
```

Two of my first tests were wrong, and I changed both. My `CourseUnit` test used `findByText`, which matched two elements, so it failed for the wrong reason. I switched it to `findByTestId('unit-header-title')`, as the test next to it does. My `GroupConfigurations` test checked the permission-denied path. It failed before the fix, but the pages the maintainers had already migrated set the title only in the main return, so that test asked for behavior the repo does not have. I moved it to the normal render. That version passes before and after, because the page already had a `<Helmet>` next to its `document.title` line. The PR says so: "It guards the title but does not prove the fix."

### The fix

Five pages got the same change. `CourseUnit` was different: it set the title in a `useEffect`, so the effect and its import went away.

```diff
-import { useEffect } from 'react';
 import { useParams } from 'react-router-dom';
+import { Helmet } from 'react-helmet';
@@ const CourseUnit = () => {
-  useEffect(() => {
-    document.title = getPageHeadTitle('', unitTitle);
-  }, [unitTitle]);
-
   useScrollToLastPosition();
@@
     <UnitSidebarProvider readOnly={readOnly}>
       <UnitSidebarPagesProvider>
+        <Helmet>
+          <title>{getPageHeadTitle('', unitTitle)}</title>
+        </Helmet>
```

After the change, the Jest run on the seven page folders gave 48 suites and 435 tests passed. For the maintainer's "anything else", I searched for other title writes and put the output in the PR:

```
$ git grep -n -E "document\.title|querySelector\('title'\)" -- src plugins ':!*.test.*'
$ echo $?
1
```

### The gate would not start on Windows (2026-10-30)

My manifest lists three checks for this repo: `oxlint`, `npm run types`, and Jest on the seven pages. The first gate run passed all three and then stopped:

```
- verdict: BLOCK (block)
- reasons quoted:
  - the claude CLI is not on PATH, so your pr-precheck can't run, and the ship-gate stops the PR until it can.
```

`claude` was on my PATH. On Windows the npm install is a `.cmd` file, and Python's `subprocess` cannot start it by its bare name. I changed one line in the gate and the same line in my voice guard:

```diff
-proc = subprocess.run(["claude", "-p", "--model", MODEL],
+proc = subprocess.run([shutil.which("claude") or "claude", "-p", "--model", MODEL],
```

Five minutes later the second run ended with `verdict: PASS` and nine rubric checks passed.

### The gate rejected my PR text (2026-11-04)

I edited the description after that pass, so the pass no longer counted. When I ran `gh pr create`, the gate ran again. The repo checks passed, and my own rubric rejected the PR:

```
- description-true-to-diff [fail]: Description says "I checked the tab titles
  in a running Studio" but test_evidence.md says "A running Studio: not tested";
  no Studio or Docker available.
```

I had checked the titles by hand that day. But my evidence file was written on 2026-10-30 and still said "not tested", so the PR claimed something my own record did not back. I did not bypass the gate. I updated `test_evidence.md` to say who ran the Studio check, when, and that Claude Code did not see it. The next run, three minutes later:

```
2026-11-04 21:33 [hook] openedx/frontend-app-authoring @ fix/897-helmet-document-title (base master)
- verdict: PASS
  - description-true-to-diff [pass]: ... 'this PR adds no messages' matches the diff (no messages.ts changed)
```

The PR opened as #3345 on that run.

### What landed

The PR is open and mergeable. On 2026-11-13 the maintainer wrote on it: "thanks for this contribution! Do you mind signing the CLA? I can't review the PR without a CLA signed." I had signed, but the check had not picked up my username. On 2026-11-16 the `openedx/cla` check passed with "The author is authorized to contribute". The PR has not merged, no code review has happened, and it still carries the `needs test run` label, so the project's CI has not run on my branch.

## Limitations and what's next

The work is not merged, and I do not yet know what review will ask for. The PR asks one open question: the old code also set the title on the loading and permission-denied returns, and my change sets it only in the main return, like the already migrated pages. If the maintainers want a title there too, that is a second commit.

My evidence has gaps. I ran only the seven page folders, not the full Jest suite, the full lint, or `make validate`, because `make` is not installed on my PC and `dprint` flags about 2,000 files for Windows line endings. My Studio check is recorded as one sentence. The gate caught that the record was missing, but what I wrote back does not list the pages I opened or the titles I saw. One gate run that week also failed two `CourseUnit` tests on a `waitFor` timeout, and the next run on the same branch passed. I suspect my slow PC and have not proven it.

The gate has its own limit: it reads the folder where the Claude Code session started, not my clone, and it cannot expand a shell variable in `--body-file`. Four runs on 2026-11-04 stopped on setup errors before any check ran.

Next, I will tag the maintainer now that the agreement check is green, and answer review with my PR playbook, whose review rows are still untested. For the tools, I will add a required "manual checks" table to my evidence template (page, title seen, date) so a hand check is recorded when I do it, and I will make the gate take the clone path as an argument.
