# Write the design a person reviews before the code

By Mackenzie Bowes, with MBSI's agents.

Writes a short design a person can steer before you build: the ticket, the types down to their leaves, the state machine and the assumptions, with silver and gold tiers when the change needs traced scenarios, a model check or a film.

What it can see: only the chat you add it to.

For your agent (the text it matches on): Write the design a person reviews before non-trivial code: by default the bronze tier (the ticket, the proposed types down to their leaves, the state machine, and the assumptions), recorded on the ticket or task it belongs to. Upgrade to silver (scenario traces, a standards check) or gold (an explainer film) only when the change calls for it. Use before writing or changing non-trivial code, when asked for a design or a design doc, or when a design was pushed back on.

## Install

### Claude Code

```
/plugin marketplace add mbsi-labs/skills
/plugin install design-docs@skills
```

Later, `/plugin marketplace update` brings in changes.

### Claude apps (claude.ai and the desktop app)

Download https://mackenziebowes.com/skills/zips/design-docs.zip, then upload it as a skill in Settings.

### ChatGPT or Grok

Open https://mackenziebowes.com/skills/text/design-docs.txt, copy all of it, and paste it into a chat before your question.

## What is in it

- NOTICE.md
- SKILL.md
- credits.md
- gold.md
- silver.md
- standards.md
- state-machines.md

## Sources

- Quint, by Informal Systems (https://github.com/informalsystems/quint). Licence: Apache-2.0. The silver tier tells you to model-check the state machines with the quint command. The skill does not include Quint; you install it yourself.

The same list is in NOTICE.md.

## Recent changes

- 2026-11-09 (008fd7f): Updated.
- 2026-11-09 (539ba3a): Updated.
- 2026-11-09 (50d1c0d): Updated.
- 2026-11-07 (481ba32): Updated.
- 2026-11-07 (fc1c870): design-docs silver: model-check the state machines in Quint before recording

The full list is in CHANGELOG.md.
