# Test a change to your agent with a question, a figure and a judge

By Mackenzie Bowes, with MBSI's agents.

It turns 'is the agent better now?' into a question asked of many items of real work, with a named judge and a figure you can track.

What it can see: only the chat you add it to.

For your agent (the text it matches on): Design evals for experiments on our environment. Use when you add evals, compare prompts or models, or check model behaviour.

## Install

### Claude Code

```
/plugin marketplace add mbsi-labs/skills
/plugin install eval-design@skills
```

Later, `/plugin marketplace update` brings in changes.

### Claude apps (claude.ai and the desktop app)

Download https://mackenziebowes.com/skills/zips/eval-design.zip, then upload it as a skill in Settings.

### ChatGPT or Grok

Open https://mackenziebowes.com/skills/text/eval-design.txt, copy all of it, and paste it into a chat before your question.

## What is in it

- SKILL.md
- credits.md

## Recent changes

- 2026-10-28 (c08c846): eval-design: public: the owner instead of a named person, the money rule in words, page.json
- 2026-10-28 (dc61539): eval-design: start every repeat of every test at once; batch only when the wait costs nothing
- 2026-10-21 (c6c2f30): Updated.

The full list is in CHANGELOG.md.
