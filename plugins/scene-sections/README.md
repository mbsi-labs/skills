# Draw a page's pictures for the words that sit on them

By Mackenzie Bowes, with MBSI's agents.

It sets each generated scene behind its section's words, drawn for where those words go, with its own render for phones and desktops.

What it can see: the chat you add it to; its script reads the image files you name and, when you run a render, sends them and your prompt to OpenRouter with your OPENROUTER_API_KEY.

For your agent (the text it matches on): Give a page section (a hero, a card, a band) a generated scene that sits behind its words and bleeds to the edges, drawn for where those words go, with its own render for each screen shape. Use when a hero or card should feel like a place rather than a picture beside a caption, when generated art keeps fighting the text, or when a wide scene breaks on phones.

## Install

### Claude Code

```
/plugin marketplace add mbsi-labs/skills
/plugin install scene-sections@skills
```

Later, `/plugin marketplace update` brings in changes.

### Claude apps (claude.ai and the desktop app)

Download https://mackenziebowes.com/skills/zips/scene-sections.zip, then upload it as a skill in Settings.

### ChatGPT or Grok

Open https://mackenziebowes.com/skills/text/scene-sections.txt, copy all of it, and paste it into a chat before your question.

## What is in it

- NOTICE.md
- SKILL.md
- credits.md
- references/masking.md
- references/prompting.md
- scripts/scene.py

## Sources

- Image prompting guide, by OpenAI (https://developers.openai.com/api/docs/guides/image-prompting). Licence: none (cited, not copied). Sketch as a layout reference; a number and a role for each reference image.
- Nano Banana Pro prompting guide, by Google (https://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n). Licence: none (cited, not copied). Section 9, structural control and layout guidance.
- Visual attentional orienting by eye gaze: a meta-analytic review of the gaze-cueing effect, by Psychological Bulletin, 2021 (https://pubmed.ncbi.nlm.nih.gov/35404635/). Licence: none (cited, not copied). Gaze reliably directs observers' attention.

The same list is in NOTICE.md.

## Recent changes

- 2026-10-28 (f025c9c): scene-sections: generated scenes behind a section's words, a render per screen shape, with canvas/render script and prompting and masking guides

The full list is in CHANGELOG.md.
