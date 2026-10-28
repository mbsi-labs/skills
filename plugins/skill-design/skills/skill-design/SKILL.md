---
name: skill-design
description: "Change how Claudes behave through their environment (a skill, rule, CLAUDE.md, hook or brief) with the smallest change that research and a test show works. Use when making, editing or ratcheting a skill, rule, CLAUDE.md, AGENTS.md or hook, or when invoked as /skill-design."
---

# Skill design: small, researched, tested

Mackenzie (2026-10-16 13:58): "our lever is environment changes, and that pareto-optimal environment changes are **small**, and they are small **because** data-vomit sideloads a bunch of implicit claims that cause runaway misalignment."

A change to a skill, rule, CLAUDE.md or hook ships only when all three hold:

1. **Small.** One or two intentful changes. Every added line carries implicit claims, so a long change is refused, not trimmed later.
2. **Researched.** You looked up the problem the change is for, in sources rather than memory.
3. **Tested.** A run with the change and a run without it show the behaviour it was made for.

Write it in a technical register: a defined term ("user-facing view", "hydration") carries what a sentence of plain words would. Name the class, not instances; a list of examples reads as exhaustive, and whatever is missing from it reads as exempt (Mackenzie, 2026-10-28 13:56).

For a skill whose work reaches people (a page, copy, a brief, a persona), have Aion 3.5 (the `aion` CLI) draft it from the ground up, centred on what people feel, and sample its examples from a domain the work isn't in, so they don't leak; then test it as above. Ask with `aion ask`.
