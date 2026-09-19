---
description: Build/update the versioned course at notes/course/COURSE.md teaching how to build and deploy an application like this one, from scratch through production
argument-hint: [module name/number to update, or omit to review/refresh the whole course]
---

Maintain a complete, standalone course as a **single file**,
`notes/course/COURSE.md`, teaching someone with **no prior context** how
to build an application like this one — from a blank directory through to
a deployed, production-ready state. This is a textbook, not a decision
log: more explanatory and complete than `/teach`'s terse what/why/breaks
format, and it explains real underlying mechanics (what actually happens
at the protocol/kernel/OS level), not just surface-level "what it is."

**Source material:** ground lessons in this project's actual code/config
and the reasoning already captured in `notes/teaching/*.md` and
`notes/plans/*.md` — reuse and cite real decisions rather than inventing
generic examples. But the course's job is to teach the underlying concept
*fully*, not just log what was decided. Where a relevant concept wasn't
actually used in this project (Terraform, ECS, Kubernetes, secrets
managers, etc.) but is foundational or relevant to the topic being
covered, include and explain it anyway — never limit coverage strictly to
"what we did." Say plainly when something is being covered for breadth
even though this project doesn't use it.

**Structure inside the one file:** numbered modules (`## N. Topic`)
building progressively — each module only assumes what earlier modules
already taught, never something from a later one — organized under `##
Part N` groupings, preceded by a table of contents and a short "how to use
this" section.

**Each module should:**
1. State what it covers and where it sits in the overall journey.
2. Explain the foundational concept with real mechanics first — what's
   actually happening at the protocol/kernel/process/wire level, not just
   a plain-language gloss — before getting practical.
3. Ground the practical part in this project's real files, commands, and
   decisions, with concrete examples.
4. Note what's deliberately deferred or out of scope for that module and
   why, so the reader isn't confused about what's coming later.

**Versioning:** the file opens with a `**Version:** X.Y — <date>` line and
a `## Changelog` section, newest entry first. On every re-invocation of
this command that actually changes content:
- Bump the version (minor bump — `2.0` → `2.1` — for updating/extending
  existing modules; major bump — `2.0` → `3.0` — for a structural change
  like adding/removing/reordering modules or a depth-calibration pass
  across the whole course).
- Add a new changelog entry at the top describing what changed and why,
  dated with today's date.
- Never delete old changelog entries — the changelog is the file's own
  history, standing in for git history since `notes/` is gitignored.

**On update** (re-invoking this command, optionally naming a module):
read the existing file first, then revise only the affected module(s) in
place rather than regenerating the whole file from scratch — mirroring
how this project's own decisions evolve over time (e.g. if the Nginx setup
changes again, update that module's content, don't rewrite the whole
course). Keep the table of contents in sync with whatever modules exist.
