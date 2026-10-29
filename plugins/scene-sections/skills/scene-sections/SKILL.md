---
name: scene-sections
description: "Give a page section (a hero, a card, a band) a generated scene that sits behind its words and bleeds to the edges, drawn for where those words go, with its own render for each screen shape. Use when a hero or card should feel like a place rather than a picture beside a caption, when generated art keeps fighting the text, or when a wide scene breaks on phones."
---

# Scene sections

A scene section is a page section whose picture is its background: the words sit on a calm part of the scene that was drawn for them, and the action sits where the words are not. The image model places detail well when it knows two things: where the focal point is, and which part of the canvas the words will cover. Everything below serves those two facts.

1. **Code the section first.** Build the section with its real words, then measure where they sit at each screen shape you ship (a desktop width and a phone width at least). The scene answers the coded layout, never the other way round.
2. **Make one canvas per screen shape** at the section's aspect ratio: a flat grey box where the words go, and the subject (a sketch, a block, or an earlier render to grow) where the action goes. `scripts/scene.py canvas` does this.
3. **Write the prompt around the focal point and the covered area.** Say what the moment is and how it feels, give every reference image a number and one job, and tell the model the grey box is "darker and calmer, no faces, no figures, no bright lights, so light text stays readable on top". `references/prompting.md` has the prompt for each case: a new scene from a sketch, fixing who is who, growing a scene to a new shape, a card background, a phone square.
4. **Render, then change one thing per call.** `scripts/scene.py render` sends the prompt and numbered references to an image model on OpenRouter. If figures drift, pass the render back as image 1 and change only them, each with its own cropped reference.
5. **Mask it into the section.** Put the scene behind the words, pinned so its action stays in view, and swap in the phone render below the breakpoint so a phone downloads only its own file. `references/masking.md` has the desktop and phone patterns.
6. **Judge it in the page, at every shape.** Zoom in on hands and small props, then decide at real size in the real section. A flaw you can only see at 300% is not a flaw.

Each screen shape needs its own render: a wide scene cropped to a phone loses its focal point or its calm zone. Set the words in the room the model left for them, never above it as well, or the section doubles its padding.
