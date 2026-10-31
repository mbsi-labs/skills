---
name: lever
description: "Build the lever: for any non-trivial edit, migration, analysis or check, write the small script, codemod or generator that does or proves it, instead of working by hand. Use when work has more than a couple of obvious edits, when a result must be checkable or rerun, when a neighbour would otherwise hand-apply a recipe, or when invoked as /lever."
---

# Build the lever

When the work isn't trivial, build the tool that does it. A script does the work the same way every time, reruns for free, and turns "trust me" into "run this".

- Do the first unit by hand to learn the recipe. Then write the tool, rerun it on that unit and diff against your hand version.
- Make it safe to rerun (idempotent).
- Codemod for edits, generator for repeated files, a query (sqlite, jq, awk) for analysis, a rerunnable command for checks.
- One deterministic pass beats handing units out. If neighbours share the work, write the recipe as a skill they read, outside the area they edit.
- Smallest tool that does the job, never a framework. Scratch levers live in the scratchpad; levers that outlive the session are committed. Rust or TypeScript on Bun for anything kept (`language-choice.md`).
- If you cite this skill and there is no script, codemod or generator in the result, you didn't apply it.
