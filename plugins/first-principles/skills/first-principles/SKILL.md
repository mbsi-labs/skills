---
name: first-principles
description: "Redesign from first principles: fold a new requirement into a design as if it had been there from the start, never bolt it on. Use when a requirement, rule or decision changes an existing design, type model or module, when a fix keeps needing special cases, or when invoked as /first-principles."
---

# Redesign from first principles

Don't bolt a change onto the current design. Redesign as if the new requirement had been an assumption from day one.

1. Read every affected file, type and rule. Know the current design before you change it.
2. Ask: "Writing this from scratch with this requirement, what would we build?" Answer in types and a state machine first, before any code.
3. Propagate the change everywhere it reaches: types, states, events, errors catalogue, docs, rules, examples. A leftover old name is a bug.
4. Design the whole redesign, then deliver it in small verifiable steps.

Signs you bolted it on: a new optional field or flag beside an old one, a `special case` branch, a comment explaining why two paths exist.
