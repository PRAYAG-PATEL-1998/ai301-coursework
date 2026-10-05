# Plan: issue #32, `DELETE /profiles/{profile_id}` leaves the profile's embeddings in the vector store

Issue: https://github.com/codepath/pathreview-ai301-fa26-s1/issues/32 | Repo: codepath/pathreview-ai301-fa26-s1 | Base commit: `f89c06f` (main)

## Repro evidence I rely on

From my posted repro (https://github.com/codepath/pathreview-ai301-fa26-s1/issues/32#issuecomment-5860905903), run on commit `f89c06f` against the real, unmodified `delete_profile()` and the real ChromaDB `VectorStore`, with the database session mocked:

- `[before delete] chunks in vector store for source_id=resume_<uuid>_abc123: 2`
- `[delete_profile] returned: True`
- `[after delete]  chunks in vector store for source_id=resume_<uuid>_abc123: 2`
- `RESULT: BUG CONFIRMED - 2 chunk(s) for the deleted profile are still retrievable from the vector store after delete_profile() returned True.`
- `grep -rn "delete_by_source_id"` shows the method is defined in `rag/retriever/vector_store.py` and called nowhere in the repo.

A second contributor (Lizyum) reproduced the same result against Postgres and a collection named `profile_<id>`: "Chunks after delete: 1".

**Correction to my own repro.** My script stored its chunks in a collection named `profile_chunks` and gave the mocked `IngestedSource` row a `source_id`. Reading the code afterwards: retrieval reads the per-profile collection `profile_{profile_id}` (`rag/retriever/hybrid.py:54`), and the `IngestedSource` model and migration `001_initial_schema.py` have no `source_id` column. The bug conclusion stands (nothing in `delete_profile` touches the vector store), but the test below uses the real collection name, and the fix does not rely on `source_id` rows.

## 1. Diagnosis

`delete_profile()` in `core/services/profile_service.py` deletes `Review`, `IngestedSource` and `Profile` rows and commits, and never calls the vector store, so the profile's chunks stay in ChromaDB and `HybridRetriever` can still return them (it queries `profile_{profile_id}`). The existing cleanup method `VectorStore.delete_by_source_id` cannot be used to fix this: it needs source ids, and the `ingested_sources` table does not store them. Nothing else in the repro contradicts this: the repro shows the SQL side working and the vector side untouched.

## 2. Scope

- **In:** make deleting a profile also remove that profile's retrieval collection `profile_{profile_id}` from the vector store.
- **Not in:** adding a `source_id` column or a migration to `IngestedSource`; changing how `ingestion/pipeline.py` or the batch processor write chunks (they pass a `vector_db` object and write `profile_id` into chunk metadata, a separate path I am not touching); renaming or unifying collection names; a retry queue for failed cleanups; ChromaDB server or docker settings; any other endpoint; the Reviews or other seeded bugs.

## 3. Files I will touch

- `rag/retriever/vector_store.py`: add `VectorStore.delete_collection(collection_name)`.
- `core/services/profile_service.py`: `delete_profile` takes an optional `vector_store` and calls it after the database commit.
- `api/routes/profiles.py`: `delete_profile_endpoint` passes a `VectorStore()` to `delete_profile`.
- `tests/unit/test_profile_service.py` (new) and one test for `delete_collection` (new file or the existing vector-store test module, whichever exists when I start).

## 4. Approach

1. `VectorStore.delete_collection(name)` calls `self.client.delete_collection(name)` and treats "collection does not exist" as success, with a log line.
2. `delete_profile(db, profile_id, user_id, vector_store=None)`: after `await db.commit()` succeeds, if `vector_store` is given, call `vector_store.delete_collection(f"profile_{profile_id}")`. If that call raises, log `profile_vector_cleanup_failed` with the profile id and do not raise, because the profile is already deleted. Not-found profiles return `False` before any vector call, as today.
3. The endpoint builds `VectorStore()` and passes it in, so the real DELETE path is fixed. Existing callers that do not pass `vector_store` behave exactly as before.

## 5. Test plan

Before and after use the same script, my Unit 2 repro updated to the real collection name `profile_<id>` (it passes `vector_store` only when `delete_profile` accepts it, so the identical file runs on both sides):

- **Before the fix (today):** `python _repro_issue_32.py` prints 2 chunks before and **2 chunks after** `delete_profile` returns `True`, and `RESULT: BUG CONFIRMED`.
- **After the fix, expected:** the same command prints 2 chunks before and **0 chunks after**, and `RESULT: FIXED`.
- New unit tests: the profile's chunks are gone after `delete_profile`; a second profile's collection is untouched; a not-found profile makes no vector call; a vector-store failure is logged and `delete_profile` still returns `True`.
- `make lint`, `make typecheck` and `make test-unit` pass.

## 6. Risks and unknowns

- I have not confirmed where production ingestion writes chunks. The pipeline takes an injected `vector_db` and `review_service` has only placeholder ingestion, so nothing in the repo wires the two together. I am targeting the collection that retrieval reads (`profile_{profile_id}`), which is where Lizyum's repro also found the leftover chunk. If the real write path later uses a different collection, this fix would not cover it.
- If the vector cleanup fails after the database commit, the profile row is gone while its chunks remain. I chose to log and not fail the request; a retry mechanism is left out of scope.
- The issue text says the pipeline stores `profile_id` with every chunk; `VectorStore.add_chunks` only stores `source_id`, `chunk_index` and `section`. This does not change the plan because I delete the whole per-profile collection.

## Deviations

The build followed the plan with three small differences, none of which changes what the posted plan comment promised:

1. **Tests live in one new file.** I put the `VectorStore.delete_collection` test (missing collection is a no-op) in the new `tests/unit/test_profile_service.py` instead of a separate vector-store test module, because no such module exists. Result: 6 new tests in one file (removes the profile's chunks, leaves another profile's chunks, not-found makes no vector call, a cleanup failure is logged and `delete_profile` still returns `True`, no `vector_store` argument skips cleanup, missing collection is a no-op).
2. **`delete_profile` restructured slightly.** To run the vector cleanup after the database commit, I moved `return True` out of the `try` block and added the cleanup after it; the existing rollback-and-raise handling for database errors is unchanged.
3. **The endpoint builds `VectorStore()` for every delete request, including ones that end in 404.** The constructor opens the Chroma client but makes no delete call when the profile is not found, so behavior is as planned, but it does touch the `.chromadb` directory on a 404. I left it that way to keep the endpoint change to one line.

Checks I ran: `ruff check .` clean; `mypy api/ core/ ingestion/ rag/ agent/ safety/` clean (also clean without my change); `pytest tests/unit` gave 381 passed and 53 xfailed. The xfails are the repo's planted bugs, and issue #32 has no xfail marker to remove. Before/after of the repro script: 2 chunks before and 2 after on `f89c06f`; 2 before and 0 after on this branch, with the second profile's collection untouched.
