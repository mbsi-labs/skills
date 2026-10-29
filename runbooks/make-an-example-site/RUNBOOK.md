# Runbook: make an example site that makes an owner say "I want to look like that"

An example site is a made-up business page for a niche (painters, a massage clinic, a wool shop) that a real owner in that niche sees and wants. This runbook is the order that worked: one example at a time, one person judging each step. The first example took about an hour after a day of examples that failed.

## 1. Before this runbook (what failed)

1. One shared template filled per niche: every example came out the same, and the set read as "you'll get a template".
2. Briefs built from checklists and invented stories without looking at the real sites: the result was a plain document that looked worse than the niche's own sites.
3. AI close-ups of craft (a hinge, cabinet grain): exactly where generated images fail, on the one thing the page claims.

## 2. The steps

1. **The simple ask.** Start from "make me an amazing landing page for my <niche> business" and care about it as if it were your own. A long, clever brief made it worse.
2. **One persona.** The owner in that niche who has to look at it and want it. Every judgement is for that one person.
3. **Look at the real local sites yourself.** Open the niche's real sites in the area at full size. They are the floor: what customers expect, and what the example must clearly beat. Many are already modern; "your site is old" is not the bar.
4. **Greybox.** In grey only, the layout an average person expects for this niche's page, every section a `<section>` with a `data-section` name. Show it to whoever decides taste. Before showing it, check: the niche's live thing (the next opening, the quote button) is on the first screen; every person the copy names has a face slot; the address has a street number; no social handle is invented; "made up" is said once in the imprint, never beside each fact.
5. **Take the structural corrections** (for a painter: a full-bleed photo of the house as the hero). Research a section only if it needs it, not one per section.
6. **Modernise and set the hierarchy.** No equal-column card grids, no stat bar, no alternating bands. Say the order of the page in words for the persona, give each screen one large thing, use three sizes, spend contrast once on the action, and group by space. Squint-test a blurred screenshot. Commit and save the greybox.
7. **Brand pictures first.** Ask an image model for a brand board: the made-up business's mark, colour swatches, type, and touchpoints (the sign, a shirt, a business card, the vehicle or the door, a print ad). Examples need the impression of depth, not a strategy. Price the run before you start, and watermark every picture used. The prompt is the brief and one direction line, nothing prescriptive: a recent model needs room, so generate more and choose. For a touchpoint at full size, pass the chosen board back as a reference image. Keep a phone number that cannot ring a real person (a 555 number). With no direction line at all, ten runs came back as one board, so give each run its own direction when you want a spread. Mine the board as a kind, not an instance: where it asks for one serif, read "a high-contrast serif" and take one the live set does not use; where it asks for cream, take a different warm off-white. Then put the new palette and type beside the first screens of every live example and translate again if it shares a heading family or a field colour with one.
8. **Hydrate the approved greybox with the brand.** Keep the greybox's layout section by section. Take colours, type and mark from the brand board and self-host the fonts. Test at 1440, 1280, 1024, 768 and 390 wide (three widths missed sideways scroll at 1024 and 1280), then look at every screenshot. A style direction applied at this step can swallow the greybox's bones, so check the layout survived.
9. **Make the scene pictures.** Use a local image model for scenes and people, and an image-edit model for every "after" and colourway of the same shot, so before and after match. Make a contact sheet, check each picture at full size, redo the failures with a new seed or a tighter prompt, and keep a close-up of craft off the page unless it holds up. Watermark every generated picture the page uses, with white "AI-generated example" across the centre at 45 degrees, baked into the file so it survives a screenshot. Keep the unwatermarked originals out of the site.
10. **Run the hierarchy and dated-site checks again, on every section of the hydrated page,** not only the hero. Each section needs its own large thing and its own picture beside its words. Squint-test each section at 390 and 1280 and write one line on what survives.
11. **Never invent a fact the reader can check.** Maps come from data, with towns and lakes where they really are. Prices, reviews and people are labelled as made up in the example strip and footer.
12. **Fix what the decider's eye catches.** Contrast over photographs (a neutral scrim, a dark backing), gimmicks (a postcard footer), clunky UI (a toolbar of labels on the hero). Simplify; don't decorate. Re-run the width checks after each fix.
13. **Commit, show it live or as a draft, and ask what's wrong.** The decider's look is the gate; the checks are only the floor.

## 3. What is untested

1. One example (a painter) went through these steps. The next niche tests whether steps 3 to 10 transfer.
2. A second pass (a wool shop) needed one review and no layout rebuild, against two reviews and a rebuild on the massage clinic: brand board first, one master room and the greybox's bones kept.
3. Step 7's style directions are dealt at random, so two niches may draw the same one. Check the set side by side and redraw when two examples would share a look.
