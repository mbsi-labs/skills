# Product demos, part 1: what ten launch films do

Evidence for the method in [RUNBOOK.md](RUNBOOK.md). Craft ideas and signs are in [craft.md](craft.md).

## 1. The films, and how they were measured

1. **Method.** Each film was downloaded at 480p from its maker's own YouTube channel. A script found the cuts with ffmpeg scene detection (`scene > 0.3`), measured the shot lengths, compared the cuts with the audio onsets (a jump of 6 dB or more in 0.1 s), and made a contact sheet of 30 frames spread across the film. A time below, such as "Arc 14–21 s", points at frames on those sheets.
2. **The ten films:**

| # | Film (maker, YouTube id) | Length | Cuts | Median shot | Longest hold, and where |
|---|---|---|---|---|---|
| 1 | Introducing the new Mac Studio, M5 (Apple, `3uAIqqg8ZHo`) | 79.6 s | 64 | 0.54 s | 6.8 s at 72.8 s (the end) |
| 2 | Boosts by Arc: Meet Your New Internet (The Browser Company, `N0jMmiCS8oQ`) | 42.1 s | 35 | 0.92 s | 3.8 s at 14.2 s |
| 3 | New Raycast. Coming 2026 (Raycast, `Mi173xGb0ZA`) | 38.6 s | 5 | 4.68 s | 13.6 s at 8.9 s |
| 4 | Stripe Sessions 2024 (Stripe, `KH0_HM6e66w`) | 108.9 s | 84 | 0.96 s | 5.2 s at 0.0 s |
| 5 | The Street Network, a Stripe Press short (Stripe, `TCFYgzBfFBs`) | 43.0 s | 17 | 1.58 s | 13.3 s at 29.7 s (the end) |
| 6 | Introducing Figma Motion (Figma, `l3HuAYXyOTo`) | 68.1 s | 20 | 2.00 s | 10.2 s at 26.6 s |
| 7 | field system (Teenage Engineering, `Tpnuo7H-Jkw`) | 48.1 s | 14 | 2.16 s | 16.1 s at 32.0 s (the end) |
| 8 | Say Hello to Playdate!! (Panic, `HdF3CnFvxg4`) | 123.1 s | 98 | 0.71 s | 8.0 s at 67.8 s |
| 9 | Phone (1). Pure instinct. (Nothing, `hQWDUPJFHdg`) | 23.5 s | 11 | 1.46 s | 6.9 s at 16.6 s (the end) |
| 10 | Intro to Linear (Linear, `9Q5BoiIFBiY`) | 240.6 s | 16 | 3.97 s | 179.3 s at 43.7 s |

3. **Why these.** Films 1 to 9 are ones people in the field cite: Apple's product films, Arc Boosts (Best Overall at the 2023 Product Video of the Year Awards, per Tella's write-up), Raycast's teasers, Stripe, Figma, Teenage Engineering, plus three arty or indie ones (Playdate, Nothing, Stripe Press). Film 10 is a walkthrough, and it is here as the counterexample.
4. **Limits.** These are frames and numbers, not listening. The onset measure is crude, so section 2.5 claims only what it can show.

## 2. What makes them exciting

### 2.1 One visual idea carries each film

Each good film has one picture-idea, a metaphor that moves, and every shot is a turn of it. None of them lists features.

1. **Arc:** one page, re-skinned again and again. The same Twitter profile appears in four different skins in the first 5 s, and the type cards say "are you" (1 s) and "your internet" (5–6 s). The idea, "the internet, made yours", is shown as one page changing.
2. **Nothing:** parrots beside a transparent phone, on black (2–19 s). Colour and curiosity meet a clear object. No feature is named.
3. **Stripe Press:** a network drawn on the world. Lines join the barrios of Havana on a satellite map (13–17 s). The film's subject, an offline street network, becomes one image.
4. **Figma Motion:** the film is made with the feature it launches. The timeline (14 s) and the easing curves (16–18 s) are on screen, and they move the film you are watching.
5. **Playdate:** the object is a character. The yellow console sits on a field of matching or clashing colour (0 s, 28 s, 80–84 s), and it is turned by a hand (40 s).
6. **The counterexample, Linear:** one 179 s screen recording. It teaches well, but it has no idea to carry, and it is a walkthrough, not a film.

**So:** before any shot, write the one moving idea (step 1 of the method in [RUNBOOK.md](RUNBOOK.md)).

### 2.2 The art treatment is restraint plus one accent

1. **One accent on a quiet ground.** Teenage Engineering is grey seamless with one red LED (0 s) and one orange panel (26 s). Nothing is a black void, and the parrots are the only colour. Raycast is monochrome chrome, and the emoji are its only colour (14–17 s). Apple is black and silver, with purple on the chips.
2. **Texture binds the world.** Stripe Press is grainy documentary footage all through, macro included: a speaker cone (8 s), a ringed hand on a keyboard (9 s). Raycast puts a chrome wave behind every UI shot, so the UI floats on a material.
3. **Type as an image.** In Apple's Mac Studio film, about half of the 30 sampled frames are giant condensed type ("UP TO 40", "NOW", "TRILLION PARAMETER FRONTIER", "ONE MORE TIME" at 63 s). Arc splits a sentence across full-colour cards. Playdate repeats "All the hits" three times with the console through it (32 s).
4. **Or type that whispers.** Teenage Engineering sets tiny lowercase lines on grey ("ultra-portable audio production", 6 s; "full interconnectivity", 12 s). Nothing ends on "out now" in small type on black (21–23 s). Quiet type works only when the picture is strong.

### 2.3 The camera on UI never shows a whole window

1. **Macro crops past the edges.** Raycast's search bar fills the frame and runs off it (1–4 s). The emoji grid is a push-in with a selection ring that lands on one tile (14–17 s).
2. **Go to the thing that changed.** Arc highlights the sidebar item in yellow and pulls in as it is zapped (13–21 s). In Stripe Sessions, the one product-UI frame is a single gauge, "531 requests per second" (60 s).
3. **The cursor is a character.** Figma draws the cursor large and lets it act: it grabs, drags easing handles and types a prompt (16–34 s).
4. **Code as texture, not as content.** Apple shows code and a node graph for under a second each (sheet row 2). They read as "work happening", not as something to read.

### 2.4 Rhythm: fast in the middle, then one long hold

1. **Fast films cut very fast.** The median shot is 0.54 s (Apple), 0.71 s (Playdate), 0.92 s (Arc) and 0.96 s (Stripe Sessions).
2. **They end on a hold.** Four of the nine films end on their longest shot: Apple 6.8 s, Nothing 6.9 s, Stripe Press 13.3 s, Teenage Engineering 16.1 s. In Apple's and Nothing's films, the mean shot in the last third is 2 to 5 times the mean shot before it. The relief, or the product alone, gets time after the speed.
3. **Slow films hold one idea instead.** Raycast makes only 5 cuts in 38.6 s. The camera moves inside each shot, so it is never still.
4. **Focus changes at least every 4 s, at varied intervals.** Focus means the focal point: where the eye lands first, set by composition, contrast and weight. A change moves it to a new position or scale. A cut that leaves it where it was is a match cut and does not count. Plan an (x, y, scale) focal point for every shot and in-shot event, and check the plan and the render, for example with a saliency map. A long hold still works when focus moves inside it: a push-in, a rack focus, a layer that lands (a stamp, steam), or a numeral that ticks. Do the same with cuts that would otherwise come at an even rhythm. Vary the gaps (for example 0.4, 1.1, 0.6, 2.3 s), because an even beat reads as a slideshow. Use plenty of cuts and jump cuts, and put motion on every piece of text.
5. **Feeling beats legibility.** Some people can't read. The viewer should come away with "our product gives you relief quickly", not with the words. Text supports the image and does not carry the meaning. A caption may leave the screen before it can be read, as long as the picture already says it.

### 2.5 Sound

1. **What I could measure:** none of the films is silent for long (0–6% of 0.1 s windows below −50 dB; Linear is 12%). Cuts landed on audio onsets at about twice chance in Apple's film (31% against 16%) and Arc's (37% against 26%), and at no better than chance in Stripe Sessions, Playdate and Stripe Press. Teenage Engineering had 2 onsets in 48 s, so a steady bed with no hits.
2. **What I can't claim:** that cutting on the beat is what makes them exciting. My onset measure can't show it. Someone who listens should check this before it becomes a rule.

### 2.6 The hero moment and the people

1. **Each film builds to one image:** Arc's "Zap this", where a page element is destroyed, as delight (14–21 s). Teenage Engineering's three units lined up, held for 16 s (32–44 s). Nothing's parrot pecking the glowing phone (16–19 s). Playdate's crank turned by a hand (40 s).
2. **People:** Stripe Sessions and Playdate show faces. Stripe Press shows people mostly at a distance and a hand in macro (9 s). A hand is enough to put a person in the frame. A rule of no faces (no stock people) loses nothing that these films need.
