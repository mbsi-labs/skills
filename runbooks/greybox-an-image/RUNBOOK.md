# Runbook: greybox an image

An image greybox works like a page greybox: fix the intent cheaply, get the owner's explicit yes, then hand the rendering on. The division of labour: "intent, gesture, pose, and story are our side and a lot of the mechanics like silhouette and rendering belong to the model". Depth is minor. Silhouette, lighting, materials and rendering are left out of this runbook on purpose.

The lecture: Animation 1 at the University of New Mexico (swardson.com/unm/animation1), week 8 (solid drawing and twins) and week 12 (appeal), plus the twelve principles' "staging" and figure-drawing teaching on the line of action. Mechanism: the attention and implied-motion studies in section 3.

## 1. Steps

1. **Write the beat in one sentence:** who does what to whom, and what the reader should feel. Staging is "the presentation of any idea so that it is completely and unmistakably clear" (Johnston and Thomas, via Wikipedia, "Twelve basic principles of animation"). AnimSchool calls it breaking the story "into the most simple and basic beats" (AnimSchool, "Storytelling in staging"), and says to stage "the emotions behind those actions", not just the actions (AnimSchool, "Storytelling in staging"). One image holds one beat.
2. **Name the subject:** the one place the eye must land (a title zone, a handed-over object, a face). Everything else in the steps below points at it. Keep motion and fuss away from it: the UNM course's example is that if the face carries the beat, "the characters arms shouldn't be flailing" (UNM animation course, "Appeal").
3. **Cast it, with a character language for each figure:** one line per figure saying who it is through how it moves (eager, unimpressed, careful, proud). The pose carries the character; the reference images carry the look.
4. **Pair them:** every figure acts on, looks at or reacts to another figure or the subject. No figure stands alone facing the reader unless it is talking to the reader.
5. **Draw each figure's line of action first,** as one curve down the spine, then hang the body on it. "The more curve you put into that line, the more attitude, force and/or movement the image will communicate" ("Gesture basics: line of action"). Lines of action are "curves, but they are not S shaped or squiggles" ("Gesture basics: line of action"); "A line of action should be a simple, readable gesture rather than a zigzag maze" (Drawn to Animation, "Line of action").
6. **Give standing figures weight on one leg (contrapposto):** shoulders and hips tilted against each other. "Usually when we see the shoulders and hips parallel to each other, the character feels off balance or stiff. Or both!" (UNM animation course, "Appeal"). Contrapposto is "standing with most of its weight on one foot, so that its shoulders and arms twist" (Wikipedia, "Contrapposto").
7. **Aim the eye path:** every gaze, pointing arm and line of action leads to the subject from step 2. Check it by drawing an arrow along each gaze and arm on a copy; every arrow should end at the subject or hand on to another figure that leads there. Use "contrasting motion" on purpose, "to the most important thing in the shot" (UNM animation course, "Appeal").
8. **Break the rhythm:** uneven spacing, varied heights, figures overlapping in their pairs, and no two figures in the same pose. Avoid twinning: "a character being drawn perfectly symmetrical" (UNM animation course, "Solid drawing"). A row of figures on one floor line reads as a legend, not a room.
9. **Depth, if it helps:** a near figure and a far figure at most. It is minor.
10. **Lay out, then pose.** Claude lays every character out as a stick figure on a perspective grid (horizon at the tallest person's eye level, vanishing point near the subject), one named Krita layer per character, already in its key colour, at the right scale for its depth, with props as blocks and the text zone from the coded page locked on its own layer (a small script writes the `.ora`). The user poses them in Krita with Liquify or Warp. The story, gesture and staging are settled in that sketch.
11. **Key every layer to its own hex code** and name each code in the prompt ("#FF0000 red: the man from image 4, down on one knee..."). Tell the model the colours are labels only. The legend lives in the prompt, never in the sketch.
12. **Get the user's yes on the sketch in his words** before any paid call (greybox gate; spends need his yes).
13. **First call: layout.** Image 1 is the keyed sketch, padded to the model's canvas; then the style reference, then each recurring character with its own reference and role.
14. **Second call: identity.** Pass the first render back as image 1 and change only the characters that drifted, each with its own cropped reference from the cast sheet ("change only the agents ... keep everything else exactly as it is"). One cast sheet with many figures is not enough: on the /skills hero the first call turned every agent into the same hooded figure, and the per-character crops fixed it. One change per call (OpenAI, image prompting guide).
15. **Zoom on hands and small props, then judge in context.** Check each figure's place, gaze and hands at full size, then put the image in the coded page before deciding. A floating hand on the /skills hero flag was plain when zoomed and invisible at hero size; the user judged it in the page.

16. **Tell the model the focal point and what the page will cover,** and let it place the detail. For an outpaint or a background, give the canvas at the card's shape, mark the subject (a coloured block or the old scene), mark where text will sit, and say how that area should behave ("keep the left side darker and calmer so text can sit over it, but still full of the market"). The model put detail where it mattered and quiet ground where the text went.
17. **Put the text where the model left room, never beside it as well.** If the prompt asks for an empty corner for a heading, set the heading in that corner; a heading above the picture plus the empty corner doubles the padding.
18. **Each screen shape gets its own render.** A wide card scene does not crop to a phone: plan a separate layout and outpaint for the phone's shape.

## 2. Classic mistakes

1. Figures lined up on one floor line, evenly spaced, facing the reader.
2. Straight spines and parallel shoulders and hips: stiff (step 5, step 6).
3. Twins: two figures, or two arms, doing the same thing (step 8).
4. A busy figure next to the subject pulling the eye away from it (step 2).
5. Spending the greybox on rendering, silhouette or lighting, which the model does.

## 3. Why it works

1. **Gaze and pointing steer the viewer's attention.** A meta-analysis of 423 gaze-cueing effects found that "others' eye gaze reliably directs observers' attention". Attention "is more powerfully captured by interfering social signals (such as others' gaze or hand orientation) than by non-biological directional cues (such as an arrow)". So a figure's gaze and pointing arm (steps 4 and 7) steer the reader's eye more strongly than arrows or other graphic devices would.
2. **A twisted pose reads as an action.** In monkey STS, cells "did not respond to the sight of non-articulated static posture" but "responded vigorously to the articulated static posture that formed the end-point of the action", and not to similar postures "in a more relaxed muscular state". In people, still photographs with implied motion drive the brain's motion areas (MT/MST) more than photographs without it. Synthesis: a curved line of action and a twist between shoulders and hips (steps 5 and 6) are what make a still figure read as doing something; that is a reading of these results, not a test of stick figures.

## 4. Open

1. Tested once (a site hero image): GPT Image kept every figure's place, size, pose and the room's perspective from the keyed sketch, leaked no key colours, and kept the title zone empty. It lost agent identities (fixed by step 14) and one gaze (the typist kept facing its screen). One test, not a rate.
2. The readings named in the field but not saved here (Thomas and Johnston, *The Illusion of Life*; Richard Williams, *The Animator's Survival Kit*; Mike Mattesi, *Force*; Will Eisner, *Comics and Sequential Art*) are in copyright and cited by title only.
