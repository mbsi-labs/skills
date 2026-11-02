# Get a spread of different answers instead of the obvious one

By Mackenzie Bowes, with MBSI's agents.

Answer one question with several different answers, each with the probability you give it, instead of the single most typical answer.

What it can see: only the chat you add it to.

For your agent (the text it matches on): Answer one question with several different answers, each with the probability you give it, instead of the single most typical answer. Use when invoked as /verbalized-sampling, when asked to 'sample', 'verbalize the distribution' or 'give me the spread', or when a question has many good answers (a name, a joke, an idea, a line, a guess) and your first answer would be the obvious one.

## Install

### Claude Code

```
/plugin marketplace add mbsi-labs/skills
/plugin install verbalized-sampling@skills
```

Later, `/plugin marketplace update` brings in changes.

### Claude apps (claude.ai and the desktop app)

Download https://mackenziebowes.com/skills/zips/verbalized-sampling.zip, then upload it as a skill in Settings.

### ChatGPT or Grok

Open https://mackenziebowes.com/skills/text/verbalized-sampling.txt, copy all of it, and paste it into a chat before your question.

## What is in it

- NOTICE.md
- SKILL.md
- credits.md

## Sources

- Verbalized Sampling prompting technique, by Jiayi Zhang, Simon Yu, Derek Chong, Anthony Sicilia, Michael R. Tomz, Christopher D. Manning, Weiyan Shi (https://arxiv.org/abs/2510.01171). Licence: arXiv paper; technique described in our own words. The steps follow the paper's VS-Standard prompt with probability tuning (k = 5, sample from the full distribution, tail probability below a threshold).

The same list is in NOTICE.md.

## Recent changes

- 2026-11-02 (fdf6343): Updated.

The full list is in CHANGELOG.md.
