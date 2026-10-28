# Build the small tool that does the job, not the job by hand

By Mackenzie Bowes, with MBSI's agents.

When the work isn't trivial, it has your agent write the script that does it, rerun it on the first unit and diff the result against the hand version.

What it can see: only the chat you add it to.

For your agent (the text it matches on): Build the lever: for any non-trivial edit, migration, analysis or check, write the small script, codemod or generator that does or proves it, instead of working by hand. Use when work has more than a couple of obvious edits, when a result must be checkable or rerun, when a neighbour would otherwise hand-apply a recipe, or when invoked as /lever.

## Install

### Claude Code

```
/plugin marketplace add mbsi-labs/skills
/plugin install lever@skills
```

Later, `/plugin marketplace update` brings in changes.

### Claude apps (claude.ai and the desktop app)

Download https://mackenziebowes.com/skills/zips/lever.zip, then upload it as a skill in Settings.

### ChatGPT or Grok

Open https://mackenziebowes.com/skills/text/lever.txt, copy all of it, and paste it into a chat before your question.

## What is in it

- NOTICE.md
- SKILL.md
- credits.md

## Sources

- principle-* skills in pstack, by Lauren Tan (https://github.com/cursor/plugins). Licence: MIT. Adapted; pstack's licence reads Copyright (c) 2026 Lauren Tan.

The same list is in NOTICE.md.

## Recent changes

- 2026-10-16 (6f94f8b): Start mbsi-skills with five short-name skills adapted from pstack

The full list is in CHANGELOG.md.
