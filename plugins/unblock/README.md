# Keep your agent moving instead of asking about everything

By Mackenzie Bowes, with MBSI's agents.

Your agent proceeds on reversible work, settles the mechanics itself and shows what it did and why, and still asks first about anything hard to reverse, outward-facing or costly.

What it can see: only the chat you add it to.

For your agent (the text it matches on): Don't block on the human: on reversible work, decide, do it and show the result instead of asking 'should I do X?'. Use when about to ask the user for permission on mechanics, conventions or reversible changes, when waiting idle on an answer, or when invoked as /unblock.

## Install

### Claude Code

```
/plugin marketplace add mbsi-labs/skills
/plugin install unblock@skills
```

Later, `/plugin marketplace update` brings in changes.

### Claude apps (claude.ai and the desktop app)

Download https://mackenziebowes.com/skills/zips/unblock.zip, then upload it as a skill in Settings.

### ChatGPT or Grok

Open https://mackenziebowes.com/skills/text/unblock.txt, copy all of it, and paste it into a chat before your question.

## What is in it

- NOTICE.md
- SKILL.md
- credits.md

## Sources

- principle-* skills in pstack, by Lauren Tan (https://github.com/cursor/plugins). Licence: MIT. Adapted; pstack's licence reads Copyright (c) 2026 Lauren Tan.

The same list is in NOTICE.md.

## Recent changes

- 2026-10-28 (996e89c): skill-design and unblock: steps stand alone for a reader without our private files
- 2026-10-16 (6f94f8b): Start mbsi-skills with five short-name skills adapted from pstack

The full list is in CHANGELOG.md.
