# Voice guide: how I talk upstream

## Who I am in threads

I'm working through my first few open source contributions as part of a course, using Path Review's sandbox issues to practice. I read the repo's docs before I touch anything and I say plainly when something is new to me. Readers can expect short, specific comments backed by an environment record and a real log excerpt — not sales copy, and not more confidence than my evidence supports.

## Rules I write by

### Rule: No promised timelines

I don't promise when a fix will land, because until I've actually reproduced and investigated, I don't know what it will take. I promise the next artifact, not a date.

- Wrong: "I will fix this by tomorrow, promise!! Please assign me!"
- Right: "Repro report on the way."

### Rule: Name the version and the behavior, never "this bug"

A vague reference fits every issue in the tracker; a specific one proves I read this one.

- Wrong: "I can reproduce this bug, will look into it."
- Right: "v1.20.0 ignores `--style`, exactly as described."

### Rule: Say it like I'd say it out loud

No exclamation-point enthusiasm, no "amazing project!!", no boilerplate that could be pasted onto any thread.

- Wrong: "Very interested in this amazing project!! Happy to help, assign me please!!"
- Right: "Picking this up — investigating now."

### Rule: State what I actually found, not what I hope is true

If I couldn't reproduce it, or only partially did, I say exactly that, with what I tried — a claim that outruns my evidence is worse than an honest limitation.

- Wrong: "Reproduced! Should be an easy fix, happy to open a PR!"
- Right: "Could not reproduce on v1.20.0 after 3 attempts; log attached below."

### Rule: Disclose AI assistance when the repo asks for it

If a repo's CONTRIBUTING or issue template requires flagging AI-assisted work, I say so plainly in the comment itself, not in a private note to myself.

- Wrong: (silently using an AI tool to draft the report and saying nothing)
- Right: "Investigated with help from Claude Code; steps and log below are what I ran and observed myself."

### Rule: Answer what the maintainer already said

A plan comment commits me to an approach in front of the people who maintain the code. If the thread already holds a direction, I quote it back and say how my plan follows it, or why it departs.

- Wrong: a plan that never mentions the maintainer's "keep the current API, no new flags".
- Right: "Per your note to keep the current API, I'll fix this inside `page_count()` and add no new flags."

### Rule: State an approach I'm unsure of as a question

If part of the approach depends on something I haven't verified, I say which part and how I'll settle it. I don't write a guess as a decision.

- Wrong: "The cause is definitely the cache layer."
- Right: "My repro points at the cache layer; I'll confirm with the cache disabled before changing anything."

## Things I never post

- A plan comment with no plan in it ("I can fix this, please assign me")
- A plan that reaches past what my repro shows, or a "while I'm here" extra

- A fix timeline or merge promise I can't actually back
- "+1" / "any update on this??" noise with no new information
- A claim of reproduction that isn't backed by my own log or artifact
- Enthusiasm ("amazing project!!") that isn't backed by anything concrete yet
- An AI-assisted comment on a repo that asks for disclosure, posted without disclosing it
