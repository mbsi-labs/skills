# Prompting for scene sections

Every prompt names the moment and how it feels, gives each reference image a number and one job, and says what the calm zone must do. Ask for the feeling of the section, not its job: "an agent writing code" gets a desk; "the moment the work runs for the first time, and they lean back, delighted" gets a scene.

## 1. A new scene from a layout sketch

Use when poses, staging and the eye path matter. Draw the layout first (stick figures on a perspective grid, one layer per character, the words' box from the coded page), then give every layer its own flat colour.

1. Image 1 is the sketch, padded to the model's canvas. Say: "Image 1 sets the layout only. Keep every figure where it is, at its size, in its pose, and keep the room's perspective. Keep the grey rectangle as empty, plain dark ground. The colours are only labels; do not paint anything in them, and add no text."
2. Write the colour key in the prompt, never in the sketch: one line per colour, saying who it is, what they do and how they feel ("#FF0000 red: the host, down on one knee, handing a strip of paper to the blue figure; patient").
3. Say where every gaze goes. Gaze and pointing steer the reader's eye more than any graphic device.
4. Then the style reference, then each recurring character with its own reference.

## 2. Fixing who is who

Use when the layout is right but characters drift: a model given one sheet with many characters tends to turn them all into one generic figure.

1. Image 1 is the render. Say: "Change only the [characters] so each matches its reference; keep everything else exactly as it is", then list what must not move.
2. Crop each character from its sheet into its own reference, numbered, and map each figure in the render to its number by place and pose.
3. One change per call.

## 3. Growing a scene to a bigger or different shape

Use when an approved scene is too small for its section, or a new screen shape needs it.

1. Image 1 is the canvas: the old scene placed where the action should stay, the rest plain ground, and the words' grey box.
2. Say: "Keep that scene's moment, figures and layout, and extend the same place outward to fill the canvas." Name what may be added (more figures at work, shelves, lights) so the new area belongs to the story.
3. A person who appears in the scene gets their own reference and "draw them in the same style and proportions as the others".

## 4. A card or section background

Use when the scene should fill a card with the words over it.

1. Mark the words' area and say how it should behave: "keep this area darker and calmer so text can sit over it, but still part of the place". The model then fills the rest with detail and leaves the words their quiet ground.
2. Put the focal action where the words are not, and say where (on the right, low, in the far corner).
3. A crowded scene (a market, a workshop) can run behind the words if that side is darker; an empty side is not needed.

## 5. A phone version

1. Use a square or tall canvas, with the words' box across the top and the approved scene placed low.
2. Grow it upward: "extend the same place upward to fill the square; keep the top darker and calmer, with no faces, no figures and no bright lights".
3. Render it separately from the desktop scene; never crop the wide one.

## 6. Checks after every render

1. Zoom in on hands, faces and small props: floating hands and extra fingers hide there.
2. Look for leaked label colours and any lettering.
3. Put it in the coded page at real size before judging it.
