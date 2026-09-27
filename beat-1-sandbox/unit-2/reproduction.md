# Unit 2 — Claim and Reproduce

Path: `beat-1-sandbox/unit-2/reproduction.md`

Record of your claim and reproduction on the issue you chose in Unit 1, and of the
evaluation runs that produced `eval-run.txt`. This file is graded at the path above; a copy
kept anywhere else in the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Your identity upstream

**GitHub username**

PRAYAG-PATEL-1998

---

## Posted upstream

**Claim comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/32#issuecomment-5860905130

Picking this up: confirmed `delete_profile` in `core/services/profile_service.py` cascades the SQL rows (reviews, ingested sources, profile) but never calls the vector store's cleanup — `VectorStore.delete_by_source_id` in `rag/retriever/vector_store.py` exists but isn't invoked anywhere in the codebase, including here. Repro report on the way.

**Reproduction comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/32#issuecomment-5860905903

**Environment:** Python 3.11.9, Windows 11 (10.0.26200), chromadb 1.5.9, sqlalchemy 2.1.1, commit `f89c06f` (main).

**Steps** (from a fresh clone):

```
git clone https://github.com/PRAYAG-PATEL-1998/pathreview-ai301-fa26-s1.git pathreview
cd pathreview
git checkout f89c06f          # matches main at time of writing
python3.11 -m venv .venv
./.venv/Scripts/pip install -e ".[dev]"
./.venv/Scripts/python _repro_issue_32.py
```

`_repro_issue_32.py` (script below, no Docker/Postgres/API keys needed):

1. Creates a local, temp-dir `VectorStore` (ChromaDB) and adds 2 chunks tagged with a `source_id`, mirroring exactly what `ingestion/pipeline.py` stores per chunk for a resume.
2. Calls the real, unmodified `delete_profile()` from `core/services/profile_service.py`, with the database session mocked the same way this repo's own `tests/unit/test_review_service.py` mocks it (`AsyncMock`, no real Postgres) — the mock returns the fake profile and one fake `IngestedSource` row pointing at that same `source_id`.
3. Re-queries the vector store for that `source_id`.

**Expected:** after `delete_profile` returns `True`, the vector store no longer has any chunks for that `source_id`.

**Actual:** both chunks are still there.

```
[before delete] chunks in vector store for source_id=resume_<uuid>_abc123: 2 -> [...]
[delete_profile] returned: True
[after delete]  chunks in vector store for source_id=resume_<uuid>_abc123: 2 -> [...]

RESULT: BUG CONFIRMED — 2 chunk(s) for the deleted profile are still retrievable from the
vector store after delete_profile() returned True.
```

Also checked with `grep -rn "delete_by_source_id"` across the repo: that cleanup method is defined in `vector_store.py` but never called from anywhere, so there's currently no path that clears a profile's embeddings — not just a missed call in this one function.

Note on method: I mocked the DB session rather than running the full Docker/Postgres stack, since `delete_profile`'s SQL side isn't in question here — the issue is specifically that nothing calls the vector-store cleanup, which this isolates directly.

<details>
<summary><code>_repro_issue_32.py</code> (full script, save and run as-is)</summary>

```python
"""Reproduction script for issue #32: DELETE /profiles/{profile_id} leaves
the profile's embeddings in the vector store.

Exercises the real, unmodified `delete_profile` (core/services/profile_service.py)
and the real ChromaDB-backed `VectorStore` (rag/retriever/vector_store.py).
The database session is mocked the same way this repo's own test suite mocks
it (see tests/unit/test_review_service.py) so this needs no Docker/Postgres.

Run with:
    ./.venv/Scripts/python.exe _repro_issue_32.py
"""

import asyncio
import shutil
import tempfile
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock
from uuid import uuid4

from core.services.profile_service import delete_profile
from rag.retriever.vector_store import VectorStore

COLLECTION = "profile_chunks"


def make_chunk(source_id: str, chunk_index: int, text: str):
    return SimpleNamespace(
        id=f"{source_id}_chunk_{chunk_index}",
        source_id=source_id,
        chunk_index=chunk_index,
        section=None,
        text=text,
    )


async def main():
    tmp_dir = tempfile.mkdtemp(prefix="pathreview_repro_")
    print(f"[env] ChromaDB persist dir: {tmp_dir}")

    try:
        # --- 1. Simulate what ingestion left behind for this profile -------
        profile_id = str(uuid4())
        user_id = uuid4()
        source_id = f"resume_{profile_id}_abc123"

        store = VectorStore(persist_dir=tmp_dir)
        chunks = [
            (make_chunk(source_id, 0, "Jane Doe - Software Engineer"), [0.1, 0.2, 0.3]),
            (make_chunk(source_id, 1, "Experience: Built REST APIs with FastAPI"), [0.4, 0.5, 0.6]),
        ]
        store.add_chunks(chunks, COLLECTION)

        before = store.get_collection(COLLECTION).get(where={"source_id": {"$eq": source_id}})
        print(f"[before delete] chunks in vector store for source_id={source_id}: "
              f"{len(before['ids'])} -> {before['ids']}")
        assert len(before["ids"]) == 2, "setup failed: chunks were not stored"

        # --- 2. Call the real delete_profile() with a mocked DB session ----
        fake_profile = Mock(id=profile_id, user_id=user_id)
        fake_source = Mock(id=str(uuid4()), profile_id=profile_id, source_id=source_id)

        db = AsyncMock()
        get_profile_result = Mock()
        get_profile_result.scalars.return_value.first.return_value = fake_profile

        reviews_result = Mock()
        reviews_result.scalars.return_value.all.return_value = []

        sources_result = Mock()
        sources_result.scalars.return_value.all.return_value = [fake_source]

        db.execute = AsyncMock(side_effect=[get_profile_result, reviews_result, sources_result])
        db.delete = AsyncMock()
        db.commit = AsyncMock()

        deleted = await delete_profile(db=db, profile_id=profile_id, user_id=user_id)
        print(f"[delete_profile] returned: {deleted}")
        print(f"[delete_profile] db.delete() called {db.delete.await_count} time(s) "
              "(SQL rows only: the IngestedSource row + profile row)")

        # --- 3. Check whether the vector store was cleaned up --------------
        after = store.get_collection(COLLECTION).get(where={"source_id": {"$eq": source_id}})
        print(f"[after delete]  chunks in vector store for source_id={source_id}: "
              f"{len(after['ids'])} -> {after['ids']}")

        print()
        if after["ids"]:
            print(f"RESULT: BUG CONFIRMED — {len(after['ids'])} chunk(s) for the deleted "
                  f"profile are still retrievable from the vector store after delete_profile() "
                  f"returned {deleted}.")
        else:
            print("RESULT: NOT REPRODUCED — vector store was cleaned up.")

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    asyncio.run(main())
```

</details>

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

1. Smoke run (3 packages, `--limit 3`): 3/3
2. Expanded run (10 packages, `--limit 10`): 9/10 — `pkg-09` failed on `claim-specific` (the check required a literal version number in the claim comment; `pkg-09`'s issue applies to all versions, so its claim never cites one)
3. Canary re-run (`--only pkg-01,pkg-03,pkg-05,pkg-07,pkg-09,pkg-10`), after loosening `claim-specific` to require unambiguous specificity rather than a version number specifically: 6/6, including `pkg-09` now agreeing, and no previously-passing package flipped
4. Second batch (`--only pkg-11,pkg-12,pkg-13,pkg-14,pkg-15,pkg-16,pkg-17,pkg-18,pkg-19,pkg-20`): 10/10, including the `disclosure` category (1/1)
5. Full confirming run (`--save-run eval-run.txt`), same rubric: **19/20 — PASS** (bar 18/20; categories: clear-accept 7/8, disclosure 1/1, no-evidence 4/4, unfollowable-comms 3/3, wrong-target 4/4) — `pkg-05` disagreed on `claim-specific` (gold `accept`, my verdict `reject`), discussed below

**Package analysis**

`pkg-05` (conda/conda#16543): gold label is `accept`; my rubric's final run gave `reject`, failing `claim-specific`. This package's claim comment reads: *"First contribution attempt: I reproduced this on 26.7.0 (report below) and want to trace where `EnvironmentSectionNotValid` gets emitted... I'll report back what I find in the exceptions path."* My check's pass condition requires the claim to "promise the next artifact (a report) rather than a fix timeline or a merge" — but this claim already says "(report below)", i.e. it delivers the report in the same breath rather than promising one, and instead promises a follow-up root-cause investigation. On this run, the model read that as not satisfying "promises the next artifact," even though the comment is otherwise exactly the kind of specific, honest claim the check is meant to reward (it names the exact error and the exact behavior, `EnvironmentSectionNotValid` breaking `--json` output). Notably, this same package agreed as `accept` in both earlier partial runs (the 10-package run and its canary re-run) before this final run — the eval-format packages bundle claim and report together, which is a structural mismatch with my check's real-world assumption that a claim always comes *before* a report exists. That's a rubric-interpretation edge case, not a re-derivable rule, which is exactly why this check scored inconsistently across otherwise-identical runs.

**Check rationale**

From `rubric.md`, the `claim-specific` check's pass condition, quoted as it now reads:

> "Names the specific behavior or scenario from the issue (not "this bug" or a generic paraphrase) — specific enough that the comment could not be mistaken for a claim on a different issue — and promises the next artifact (a report) rather than a fix timeline or a merge. A version number is one way to be specific but is not required on its own when the issue itself isn't version-scoped, as long as the named scenario is unambiguous."

I wrote it this way after `pkg-09` (sharkdp/fd#2033) failed an earlier, stricter version of this check that required the claim comment to name both a version number and a behavior. `pkg-09`'s issue states "applies to all" versions, so its claim ("scenario 2, the argument-size flush reordering") never cites a version — yet the claim is completely unambiguous about which issue it belongs to. The lecture's own example ("v1.20.0 ignores `--style`") happened to use a version number, but the underlying principle it named was specificity ("nothing here fits any other issue"), not the literal presence of a version digit. I revised the check to test for that underlying principle directly, which correctly flipped `pkg-09` to `accept` without breaking any of the 6 packages I re-tested as canaries.

**Trade-offs**

Loosening `claim-specific` from "must name a version" to "must be unambiguous" traded a mechanical, fully-consistent rule for a more correct but more interpretive one — and I know exactly what it cost: `pkg-05`'s claim-specific grade flipped between runs (`accept` twice, then `reject` once) even though nothing about the rubric or the package changed between those runs, which a purely mechanical check (like a literal version-number requirement) would never do. I accepted that variance because the alternative — keeping the stricter, version-literal wording — would have *reliably* rejected `pkg-09` on every run, which is a real package in this set, whereas `pkg-05`'s occasional misread only affects one edge case (a claim that bundles in an already-completed report) that live-mode claims won't structurally hit, since in real use the claim is always posted before the report exists.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/repro-check/`.
