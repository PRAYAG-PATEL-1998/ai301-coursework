# Unit 3 — Plan and Build

Path: `beat-1-sandbox/unit-3/plan-and-implement.md`

Record of your plan, the branch you built it on, and the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in the
repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Posted upstream

**GitHub username**

PRAYAG-PATEL-1998

**Plan comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/32#issuecomment-5986037807

> Plan for #32, following my repro above (commit `f89c06f`: after `delete_profile()` returns `True`, the chunks are still in the vector store).
>
> **What I found:** `delete_profile()` in `core/services/profile_service.py` deletes the Review, IngestedSource and Profile rows and never calls the vector store. `HybridRetriever` reads the per-profile collection `profile_{profile_id}` (`rag/retriever/hybrid.py:54`), so those chunks stay retrievable. `VectorStore.delete_by_source_id` can't fix it on its own: the `ingested_sources` table has no `source_id` column to drive it. One correction to my repro: it used a `profile_chunks` collection and a mocked `source_id`, so I'm re-running it against `profile_<id>`. The bug itself is unchanged, and it matches what Lizyum found in the thread.
>
> **What I'll do:** a small change in the three files you listed.
> - add `VectorStore.delete_collection(name)` in `rag/retriever/vector_store.py`
> - have `delete_profile()` call it for `profile_{profile_id}` after the DB commit, logging (not raising) if the cleanup fails
> - pass a `VectorStore()` from `api/routes/profiles.py`
>
> I'm not touching the `IngestedSource` model or migrations, the ingestion pipeline's write path, or collection naming.
>
> **How I'll prove it:** the same repro with the real collection name: today it prints 2 chunks before and 2 after; after the fix it should print 2 before and 0 after. I'll add unit tests for that case, for a second profile's collection staying untouched, and for the not-found and cleanup-failure paths, and run `make lint`, `make typecheck` and `make test-unit`.
>
> One open question: nothing in the repo wires the ingestion pipeline to a specific collection yet, so I'm targeting the one retrieval reads. If the intended write path is a different collection, tell me and I'll adjust the plan before building.

---

## Your branch

**Branch**

fix/32-delete-profile-vector-cleanup

**Evidence**

Same repro script both times, `_repro_issue_32.py` (my Unit 2 repro, updated to store chunks in the collection retrieval reads, `profile_<id>`; it passes `vector_store` to `delete_profile` only when the function accepts it). Command, run from the fork's top folder:

```
./.venv/Scripts/python.exe _repro_issue_32.py
```

**Before** (on `main` at `f89c06f`, unmodified code):

```
[env] ChromaDB persist dir: C:\Users\praya\AppData\Local\Temp\pathreview_repro_slovr3l1
[before delete] chunks in collection profile_9b6fc3d9-c212-499d-9931-5f5ced77619f: 2
[delete_profile] returned: True (vector_store passed: False)
[after delete]  chunks in collection profile_9b6fc3d9-c212-499d-9931-5f5ced77619f: 2
[after delete]  other profile's chunks untouched: 1
RESULT: BUG CONFIRMED - 2 chunk(s) for the deleted profile are still retrievable from the vector store after delete_profile() returned True.
```

**After** (on branch `fix/32-delete-profile-vector-cleanup`, commit `2ab27ac`):

```
[env] ChromaDB persist dir: C:\Users\praya\AppData\Local\Temp\pathreview_repro_uubtqcv4
[before delete] chunks in collection profile_e1e90120-d4d5-4e2b-bd77-0a9200b245e9: 2
[delete_profile] returned: True (vector_store passed: True)
[after delete]  chunks in collection profile_e1e90120-d4d5-4e2b-bd77-0a9200b245e9: 0
[after delete]  other profile's chunks untouched: 1
RESULT: FIXED - the deleted profile's chunks are gone from the vector store.
```

Also on the branch: `pytest tests/unit` gives 381 passed, 53 xfailed (planted bugs); `ruff check .` and `mypy api/ core/ ingestion/ rag/ agent/ safety/` are clean; 6 new tests in `tests/unit/test_profile_service.py`.

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

Scores in order (each run's `agreement` line, scored packages only):

1. Smoke run, `--limit 3`: 3/3
2. `--only pkg-04..pkg-08`: 5/5
3. `--only pkg-09..pkg-13`: 5/5
4. `--only pkg-14..pkg-18`: 4/5 (pkg-14 rejected, failed `buildable-by-stranger`)
5. `--only pkg-14,pkg-10,pkg-17,pkg-18` after loosening `buildable-by-stranger`: 3/4 (pkg-14 now failed `diagnosis-grounded`)
6. `--only pkg-14,pkg-01,pkg-07,pkg-11,pkg-16` after loosening `diagnosis-grounded`: 5/5
7. Full run, all 20: 20/20 (bar: 18/20: PASS)

The last score, 20/20, matches the `agreement: 20/20 scored items  (bar: 18/20: PASS)` line in `eval-run.txt`.

**Package analysis**

**pkg-14** (zellij-org/zellij#5174, category clear-accept). Gold label: `accept`. My rubric first said `reject` (run 4, `failed: buildable-by-stranger`), then still `reject` after I loosened that check (run 5, `failed: diagnosis-grounded`), and `accept` in runs 6 and 7.

Why it read it that way. The plan says: "exact functions to be pinned in the PR after tracing the query issuance with debug logs". My first pass condition demanded "the specific file(s) or function(s)", so the deferred function name failed it, although the plan does name the area ("the client attach/reattach path in `zellij-server`") and picks an approach ("consuming or draining pending OSC query responses ... before pane input is wired"). After I changed that, the grader failed `diagnosis-grounded` instead, because my condition asked the cause to be shown by the repro. The repro evidence only has to not contradict it, and it does not: "the leak appeared on every re-attach, never on a fresh session create", clean on 0.44.1 over 5 cycles, and the cache control. I rewrote the condition so a failure needs a contradiction, which is why pkg-14 now accepts and why it is still correct to reject pkg-01, pkg-07, pkg-11 and pkg-16, whose own controls rule their causes out.

**Check rationale**

| buildable-by-stranger | The plan's Changes/Approach and Files sections. | Pass if a stranger could start work from the plan alone: it names a specific file, module, or code path where the change goes (naming the exact function may wait for tracing) and a chosen approach for each change. Fail if the location or the approach itself is left undecided ("somewhere", "whichever is easier", "investigate", "maybe also", "not sure which layer"), or if no file, module, or code path is named. A plan that picks its approach and location but says it will pin the exact function while tracing still passes. | required |

Why it reads that way. The first version read "Pass if a stranger could start work from the plan alone: it names the specific file(s) or function(s) to change and a chosen approach for each change. Fail if any real decision is left for build time". It rejected pkg-14 (gold `accept`) because that plan leaves the exact function to be pinned while tracing. I rewrote it so the location is a named file, module, or code path and the thing that must not be left open is the location or the approach itself. I rejected the other direction, dropping the check or accepting any named area, because pkg-10 ("profile-and-optimize with no files"), pkg-17 ("gocui? tcell? not sure") and pkg-18 ("`recover()` somewhere") must stay rejected.

**Trade-offs**

What `buildable-by-stranger` gives up: a plan that names a module and a chosen approach but guesses the wrong module still passes this check, because the check cannot know the right location. `diagnosis-grounded` and the thread check are what catch a wrong target, not this one.

What changed because of it: pkg-14 flipped from reject to accept. Canaries I re-ran with `--only` after loosening it: the three unbuildable rejects pkg-10, pkg-17 and pkg-18 (all still `reject`, run 5). After loosening `diagnosis-grounded` I re-ran the four wrong-cause rejects pkg-01, pkg-07, pkg-11 and pkg-16 together with pkg-14 (run 6, all five agreed). The final full run (20/20) confirmed nothing else flipped.

---

Related paths: `plan.md` and `eval-run.txt` in this directory; your skill's files in
`tools/plan-check/`.
