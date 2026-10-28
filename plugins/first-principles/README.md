# Fold a new requirement into a design as if it was always there

By Mackenzie Bowes, with MBSI's agents.

When a rule changes, it redesigns the type model or module from the start instead of adding another special case.

What it can see: only the chat you add it to.

For your agent (the text it matches on): Redesign from first principles: fold a new requirement into a design as if it had been there from the start, never bolt it on. Use when a requirement, rule or decision changes an existing design, type model or module, when a fix keeps needing special cases, or when invoked as /first-principles.

## Install

### Claude Code

```
/plugin marketplace add mbsi-labs/skills
/plugin install first-principles@skills
```

Later, `/plugin marketplace update` brings in changes.

### Claude apps (claude.ai and the desktop app)

Download https://mackenziebowes.com/skills/zips/first-principles.zip, then upload it as a skill in Settings.

### ChatGPT or Grok

Open https://mackenziebowes.com/skills/text/first-principles.txt, copy all of it, and paste it into a chat before your question.

## What is in it

- NOTICE.md
- SKILL.md
- credits.md

## Sources

- principle-* skills in pstack, by Lauren Tan (https://github.com/cursor/plugins). Licence: MIT. Adapted; pstack's licence reads Copyright (c) 2026 Lauren Tan.

The same list is in NOTICE.md.

## Recent changes

- 2026-10-28 (c6d1e92): Updated.
- 2026-10-16 (6f94f8b): Start mbsi-skills with five short-name skills adapted from pstack

The full list is in CHANGELOG.md.
