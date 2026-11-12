---
name: prove-it
description: "Prove it works before saying done: check the real thing (run the program, read the actual value, look at the diff), never a proxy, a self-report or 'it compiles'. Use after finishing any task and before a hand-back or a 'done', when a neighbour reports success, or when invoked as /prove-it."
---

# Prove it works

Unverified work has unknown correctness. Check the real thing directly.

- Run the real program from outside and read what it prints (a demonstration, `definitions.md`). Not mtimes, not a cached screenshot, not an agent's word.
- Check liveness directly (the process, the listener), not state derived from it.
- When a check fails, suspect the way you looked before you suspect the system.
- An empty result proves nothing: a grep with no match, an empty `git log A..B`, a curl that printed nothing. A wrong query, a redirect or a script that exited early look the same. Pair every "X is gone" with a count of something that must be there (the page title, the function's name), and run the check in a call of its own so its output can't be confused with another command's.
- Script the check when you can, so a reviewer reruns it instead of trusting you. Put the command and its output in the hand-back.
- A script that proves a fix is a demonstration, not a new test. Add a test only for a promise no step checks yet (`code-standards.md`).
- Visual results go to the user, shown inline. Their eyes are the check.
