# Fix a repeated mistake in structure, not with one more instruction

By Mackenzie Bowes, with MBSI's agents.

When the same correction comes up a second time, it picks the cheapest guard that holds it (a type, a lint rule, a hook or a script) instead of adding another line of text.

What it can see: only the chat you add it to.

For your agent (the text it matches on): Encode a lesson in structure instead of more text: when the same correction or instruction comes up a second time, hold it with a type, lint, hook, script or check rather than another sentence in a rule. Use when the user repeats a correction, when you are about to add a line to a rule, CLAUDE.md or skill, or when invoked as /encode-lessons.

## Install

### Claude Code

```
/plugin marketplace add mbsi-labs/skills
/plugin install encode-lessons@skills
```

Later, `/plugin marketplace update` brings in changes.

### Claude apps (claude.ai and the desktop app)

Download https://mackenziebowes.com/skills/zips/encode-lessons.zip, then upload it as a skill in Settings.

### ChatGPT or Grok

Open https://mackenziebowes.com/skills/text/encode-lessons.txt, copy all of it, and paste it into a chat before your question.

## What is in it

- NOTICE.md
- SKILL.md
- credits.md

## Sources

- principle-* skills in pstack, by Lauren Tan (https://github.com/cursor/plugins). Licence: MIT. Adapted; pstack's licence reads Copyright (c) 2026 Lauren Tan.

The same list is in NOTICE.md.

## Recent changes

- 2026-10-28 (2dbcdfa): dig-apc and encode-lessons: each step stands alone for a reader without our other skills
- 2026-10-16 (6f94f8b): Start mbsi-skills with five short-name skills adapted from pstack

The full list is in CHANGELOG.md.
