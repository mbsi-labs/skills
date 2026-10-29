---
name: skill-design
description: "Change how Claudes behave through their environment (a skill, rule, CLAUDE.md, hook or brief) with the smallest change that research and a test show works. Use when making, editing or ratcheting a skill, rule, CLAUDE.md, AGENTS.md or hook, or when invoked as /skill-design."
---

# Skill design: small, researched, tested

Every line in a loaded file carries implicit claims that nobody checked, and they add up to drift. So the best change to an agent's environment is a small one.

A change to a skill, rule, CLAUDE.md or hook ships only when all three hold:

1. **Small.** One or two intentful changes. If yours is longer, cut it to the one or two that matter before it ships; don't plan to trim it later.
2. **Researched.** You looked up the problem the change is for, in sources rather than memory.
3. **Tested.** Run the same task with the change and without it, a few times each, and look for the behaviour the change is for. If the runs look the same, the change does nothing yet.

Write it in a technical register: a defined term ("user-facing view", "hydration") carries what a sentence of plain words would. Name the class, not instances; a list of examples reads as exhaustive, and whatever is missing from it reads as exempt.
