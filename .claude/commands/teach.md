---
description: Explain a decision/concept from this session in a teaching style and save it as a markdown note
argument-hint: [topic]
---

Before writing anything:

1. Read `notes/teaching/INDEX.md` if it exists — a one-line-per-topic index
   of what's already been documented (`- [topic](file.md) — what it covers`).
   If it doesn't exist, treat coverage as empty.
2. Check whether **$ARGUMENTS** (or the topic you infer, if no argument was
   given) overlaps with something already listed there:
   - **Same topic** → append a new dated section (`## <YYYY-MM-DD>`) to the
     existing file instead of re-explaining from scratch. Only add what's
     new or has changed since the last entry.
   - **Related but distinct topic** → don't re-explain what's already
     covered elsewhere; cross-link to it (e.g. `See docker-setup.md for X`)
     and write only the genuinely new part.
   - **Unrelated topic** → write a new file as normal.

Explain the topic in a teaching style. For each distinct sub-point, cover:

1. **What it is** — the concept or decision in one or two sentences.
2. **Why we do it** — the underlying mechanism or reasoning, grounded in this
   project's actual code/config (reference real file paths/settings), not
   generic "best practice" statements.
3. **What breaks if you skip it** — a concrete failure mode, not just "it's
   bad practice."

Write the result to `notes/teaching/<kebab-case-topic>.md`, creating the
`notes/teaching/` directory if it doesn't exist.

Finally, update `notes/teaching/INDEX.md`: add a new line for a new file, or
update the existing line's summary if you appended to an existing one, so
future runs of this command know what's already written and don't overlap.

Do not modify any other files, and don't write actual code changes — this
command only produces documentation.
