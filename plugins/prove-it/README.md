# Make your agent check the real thing before it says done

By Mackenzie Bowes, with MBSI's agents.

Before your agent says it is done, it runs the real program from outside and reads what it prints, instead of trusting a compile, a cached screenshot or its own word.

What it can see: only the chat you add it to.

For your agent (the text it matches on): Prove it works before saying done: check the real thing (run the program, read the actual value, look at the diff), never a proxy, a self-report or 'it compiles'. Use after finishing any task and before a hand-back or a 'done', when a neighbour reports success, or when invoked as /prove-it.

## Install

### Claude Code

```
/plugin marketplace add mbsi-labs/skills
/plugin install prove-it@skills
```

Later, `/plugin marketplace update` brings in changes.

### Claude apps (claude.ai and the desktop app)

Download https://mackenziebowes.com/skills/zips/prove-it.zip, then upload it as a skill in Settings.

### ChatGPT or Grok

Open https://mackenziebowes.com/skills/text/prove-it.txt, copy all of it, and paste it into a chat before your question.

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
