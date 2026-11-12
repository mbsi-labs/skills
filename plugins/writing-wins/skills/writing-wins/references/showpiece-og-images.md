---
kind: post
title: "Every page on this site grows its own landscape: link previews drawn from the page's own words"
page_title: "Link previews drawn from each page's own words"
summary: "A generative system that turns each page's text and edit date into a unique topographic map for its social preview. Deterministic, built at no cost per visit, and split so anyone can write their own drawing style. How we designed it, how we proved each step, and all the code."
date: 2026-10-18
---

Share any page from this site and the preview shows a map of a landscape that exists nowhere else: hills raised by the page's own most distinctive words, terrain shaped by the rhythm of its sentences, weathering laid down on the day it was last edited. Edit the page, and its landscape changes.

!Twenty-one topographic maps, each different: brown terrain with orange halftone ribbons along the main contours.
*Every preview from one build of this site, 21 pages, 21 landscapes.*

Most sites solve link previews with one card for every page, or a template with the title pasted on. We wanted each page to have its own face, made from what the page actually says. Three problems had to be solved: what a preview picture is for, how to turn prose into terrain, and how to make the system something other people can build on. We solved all three in one working session.

## What a preview picture is for

We started from what platforms actually show. On Discord and X, the title, description and domain already sit beside the image, and X stamps its own label in the corner. Text baked into the picture repeats the first and collides with the second. So the picture carries no text at all. Its job is to say "this page is its own place" at a glance.

!A dark brown topographic map with orange halftone ribbons and a scatter of small cream dots, with no text.
*The real preview for one research page.*

Colour came from the same kind of looking. Nearly every app people scroll through is slightly blue, so a warm brown and orange picture reads as distinct from the interface around it.

## Turning prose into terrain

The pipeline has four stages, and only the first and last touch files: acquire the text and edit date, analyze the text into numbers, draw an SVG from the numbers, and rasterize it.

The text becomes six measurements, each from 0 to 1 on a fixed scale, so a page's picture never depends on the rest of the site: how long it is, how varied its vocabulary is, how long its sentences run, how much punctuation it uses, how many long words it has, and how numeric it is. Variety sets how many layers of noise build the land, sentence length sets how broad the landforms are, and punctuation sets how much the terrain twists. The nine most distinctive words each raise a hill, placed by a hash of the word. The edit date adds a finer layer of weathering.

The detail that makes it look printed is the halftone. A dot screen covers the image, and every dot is sized by its distance in pixels to the nearest contour line. The dots trace the paths the terrain takes, so the brightest contours read as ribbons of ink.

!Three versions of one map: thin contour lines, halftone ribbons only, and both mixed.
*One page in three styles: lines, halftone, and the mix the site uses.*

It's fully deterministic: the same page always gives the same bytes, so platform caches behave. Every image is drawn once at build time, so visitors never wait for one and it costs nothing per visit.

## Making it something others can build on

The first version worked and was fitted to one picture. To publish it, we split what describes a page from what draws it. The result is a small plain-JSON description of a page, the seed, which says nothing about how to draw. It holds three independent sources of randomness (one stable across edits, one that changes with any edit, one that changes with the edit day), the facts, the six measurements, the salient words and two profiles along the page.

We proved each step. Before the split, we recorded the exact output of 24 renders. After it, none matched, and a numeric diff traced every difference to one constant: 1/4.4 written as 0.2273. With the exact value, all 24 came back byte-identical.

To prove the seed isn't secretly shaped like terrain, we wrote a second drawing style, stacked ridgelines driven by the sentence-length profile, with no change to the seed at all.

!The same page drawn twice: a topographic map on the left, stacked orange ridgelines on the right.
*One seed, two drawing styles.* And because one randomness source is stable across edits, an edited page can keep its landscape. The terrain before and after adding a sentence correlates at 1.00, and at 0.91 after adding a paragraph.

!Four maps in a grid: the top pair re-rolls completely after an edit; the bottom pair keeps the same hills with changed detail.
*Top: a page re-rolled by an edit. Bottom: the same edit with the stable layout. The hills stay, and only the detail is re-surveyed.*

## How the design moved

| In the first plan | What we decided |
|---|---|
| Tree rings for page age | Cut: the only geometric shape in an organic picture, and nobody could read it |
| A domain mark on the image | Removed after testing real Discord and X previews |
| Teal on near-black | Warm brown and orange |
| Plain contour lines | Halftone ribbons on the main contours, chosen side by side |

Research ran as five parallel passes: generative examples, editorial design, trends, rendering technique and platform behaviour. One lesson from it is worth taking. Ask what's out there, and leave your own choice out of the prompt, or the research will confirm what you already picked.

## What this says about how we work

A link preview is the smallest surface a site has, and most people never think about it. We treated it as a design problem worth solving from first principles: we looked at how platforms really show it, built a system instead of a template, proved every step with measurements, and gave the whole method away. That's how we approach every problem a template doesn't fit, whether it's a preview picture or a client's business.

## Take it

All of it is free to copy: the seed format, both drawing styles, the shared tests every style must pass (deterministic output, a response to content and date changes, no crash on an empty seed), and the rules for writing your own style. It's in the [full build log](https://www.mackenziebowes.com/posts/generative-og-images-built-and-measured).

If you're solving a design problem that the usual template doesn't fit, I'd like to hear about it: mackenzie@mackenziebowes.com or [@_mackenziebowes](https://x.com/_mackenziebowes).
