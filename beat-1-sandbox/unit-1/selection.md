# Unit 1 — Issue Selection

Path: `beat-1-sandbox/unit-1/selection.md`

Record of the issue carried into Unit 2, and of the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in
the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the
wrong label is not graded.

---

## Selected issue

**Issue link**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/32

**Verdict output**

Command run:

```
claude "issue-select: grade these candidate first issues: https://github.com/codepath/pathreview-ai301-fa26-s1/issues/72 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/61 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/62 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/36 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/37 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/32 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/1 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/7 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/51 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/12 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/22 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/13 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/50 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/42 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/40 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/39 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/41 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/59 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/60 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/68 https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69"
```

Output:

```
Repo-level facts (apply to all 21 candidates)

- maintainer-alive: pass — last 5 default-branch commits (2026-09-10 → 2026-09-16) all authored by human Aburke225, most recent 4-5 days before capture.
- repo-in-use: pass — not archived, last push 2026-09-16 (4-5 days before capture), no releases needed since push is recent.
- ai-contribution-policy: pass — docs/CONTRIBUTING.md and the PR template are silent on AI use; no AI_POLICY.md/ban found.
- maintainer-responsive (preferred, ties across all 21): pass — sampled issues #52/#43 elsewhere in the repo got COLLABORATOR first replies within 6 days.
- unclaimed: pass for all 21 — gh issue view shows assignees: [] on every candidate, and gh pr list --state all returns zero PRs repo-wide.

All 21 pass every required check — none is a tracking/umbrella issue, support question, unresolved design dispute, undecided-TBD feature, maintainer-declared deep-internals issue, or has an abandon-cycle history. Verdict: accept, all 21.

Relevant entry for issue #32:

6. #32 – Deleted profile leaves vector-store embeddings: 3-file Python fix, 4–6h.

[
  {"item":"https://github.com/codepath/pathreview-ai301-fa26-s1/issues/32","checks":[{"name":"maintainer-alive","grade":"pass","evidence":"Same repo-level commit evidence"},{"name":"repo-in-use","grade":"pass","evidence":"Same repo-level push evidence"},{"name":"scope-fits","grade":"pass","evidence":"One deliverable (clear embeddings on delete) across 3 named files, 4-6h estimate, opener is repo maintainer"},{"name":"unclaimed","grade":"pass","evidence":"assignees: []; no PRs in repo; 0 comments"},{"name":"ai-contribution-policy","grade":"pass","evidence":"Repo-level: no AI ban found"},{"name":"maintainer-responsive","grade":"pass","evidence":"Repo-level sample within 14 days"}],"verdict":"accept"}
]
```

---

## Eval iterations

**Run history**

1. Smoke run (3 issues): 2/3 — issue-01 failed on `scope-fits`
2. Smoke run (3 issues), after fixing `scope-fits`'s umbrella-issue wording: 3/3
3. Expanded run (10 issues): 9/10 — issue-04 failed on `scope-fits` (terse maintainer-filed bug misread as unscoped)
4. Expanded run (10 issues), after adding a terseness/maintainer carve-out to `scope-fits`: 10/10
5. Full run (20 issues): 17/20 — issues 09, 15, 19, 20 disagreed; `scope` category at 2/4
6. Full run (20 issues), after fixing `maintainer-alive` (bot-commit authorship), `scope-fits` (core-internals trigger, numbered-single-bug vs. umbrella distinction, abandoned-claim-cycle history, unvetted-TBD-feature trigger), and `unclaimed` (comment-thread PR mentions): 19/20 — PASS (bar 18/20; categories: claimed 4/4, clear-accept 7/8, dead-repo 3/3, policy 1/1, scope 4/4)
7. Confirming run (`--save-run eval-run.txt`), same rubric: **19/20 — PASS** (identical result to run 6; categories unchanged; committed as `eval-run.txt`)

**Issue analysis**

`issue-19` (zxcalc/zxlive#517): gold label is `accept`; my rubric's final verdict is also `accept`. During development, an earlier version of my `scope-fits` check rejected this one incorrectly. The issue is a maintainer-filed performance bug ("Selecting large subgraphs in proof mode freezes the UI") written as two numbered lists — "two potential causes" and "three additional suggestions." My check's umbrella-issue fail trigger was watching for "a list of many sub-items," and a 5-item numbered breakdown pattern-matched that, even though it's really one bug's diagnosis and implementation notes for one contributor in one PR, not a tracking list meant to be split across many people. I revised the check to explicitly say a numbered breakdown of root causes/implementation notes for a single deliverable doesn't count as "many sub-items" — only a literal list of separate linked issue numbers, or explicit multi-contributor language, does. After that fix, the check correctly passes this issue.

**Check rationale**

From `rubric.md`, the `ai-contribution-policy` check's pass condition, quoted as written:

> "Fail only if the policy states an outright ban on AI-generated contributions with no carve-out for assistive/human-reviewed AI use (e.g., "we do not accept AI-generated code"). Conditions (disclosure, human review, testing requirements) pass. A policy banning only fully-autonomous AI generation while allowing assistive use passes. Silence/no stated policy passes."

I wrote it this way because an issue can pass every liveness/scope/claim check from the four lecture families and still be a dead end if the repo's contribution rules reject an AI-assisted workflow outright — the fifth surface `evidence-guide.md` names separately. I calibrated the exact wording against two real examples: `bookwyrm-social/bookwyrm`'s CONTRIBUTING.md states "We do not accept AI-generated code or documentation" with no carve-out — a clean outright ban that must fail regardless of how good the issue looks (gold: reject, category `policy`). By contrast, `processing/p5.js`'s policy bans only "fully AI-generated" contributions while explicitly allowing assistive AI use — a condition, not a ban, so it must pass (gold: accept). The distinction between those two determined the check's exact language.

**Trade-offs**

This check only reads the single "contribution policy" line in the repo-facts block (or `CONTRIBUTING.md`/`AI_POLICY.md` in live mode) — it doesn't separately check PR/issue templates for an AI-disclosure checkbox, or look for a dedicated `AGENTS.md` file, both of which `evidence-guide.md` lists as additional places this signal can live. This never changed a verdict across all 20 scored issues (the `policy` category still went 1/1 correct), so I accepted the narrower evidence source rather than adding complexity with no evidence it would catch a real case in this set.

---

## Selection rationale

Graded on whether all three are answered, in your own words. Not on how good the
reasoning is, and not on length — a short honest answer to each earns the full marks.
This is also the basis for the claim comment you write in Unit 2.

**Selection rationale**

1. This issue touches both the API layer (the `DELETE /profiles/{profile_id}` route) and the vector-store cleanup logic behind it, which matches my full-stack background including SQL/NoSQL databases. Its 4-6 hour estimate fits comfortably alongside the rest of this unit's work.
2. The skill's verdict correctly confirmed the issue is fully unclaimed (no assignee, no linked PR, zero comments) and that the repo is genuinely active (daily human commits). What I weighed myself, beyond the rubric: this issue was filed directly by the repo's maintainer rather than a bot or another student, which gives me more confidence the diagnosis is accurate, and fixing it across three files should teach me more about how the API and storage layers interact than a single-file bug would.
3. I expect low-to-moderate difficulty claiming it — the fix spans three named files rather than one, so I'll need to trace how the delete endpoint currently calls into the embedding-store layer before adding the missing cleanup call. The root cause is already clearly diagnosed in the issue itself, so I don't expect to spend time reproducing it from scratch.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/issue-select/`.
