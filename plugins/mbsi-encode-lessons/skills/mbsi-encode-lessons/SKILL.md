---
name: mbsi-encode-lessons
description: "Encode a lesson in structure instead of more text: when the same correction or instruction comes up a second time, hold it with a type, lint, hook, script or check rather than another sentence in a rule. Use when the user repeats a correction, when you are about to add a line to a rule, CLAUDE.md or skill, or when invoked as /encode-lessons."
---

# Encode lessons in structure
Nobody likes repeating themselves!
If you, your harness, or your peer needs the same thing explained to it repeatedly, something is messed up!

- Pick the cheapest guard that holds the lesson for what you're doing: it might be a type, a lint rule, a hook or mod for you or your harnesses, a script, or a new test case.
- If the fix is structural, ship only the structural fix. Delete the instruction it replaces because the instruction was the symptom of the problem you just fixed.
- If the lesson needs judgement and no guard can hold it, make the line more prominent and add one real example of the failure.
- Record the lesson's origin (the user's words, with the time) on the ticket, not in the guard.

Example: "never auto-compact" was a habit to remember. It became `DISABLE_AUTO_COMPACT` in settings.
