---
name: skill-design
description: "Call this skill to learn how to write a skill that changes how other Claudes work, by modelling it on skills that already work here. Use it before you write a new skill, rule or brief, and when a skill you wrote keeps producing generic or over-specified work."
---

# Design a skill

Stand on the shoulders of giants. Read the skills the user wrote by hand (`outreach-dm`, `create-valuable-software`, `claims`) and the ones we adopted from poteto (`first-principles`), then write yours the same way. Don't search for a perfect skill with rounds of evals: that spends a lot of tokens to get a skill that's longer and worse.

1. **As long as the job needs.** Here's the range:
   - `first-principles`, about 180 words, is a reframe. It's one question ("Writing this from scratch with this requirement, what would we build?") and the signs that you didn't ask it.
   - `claims`, about 300 words, is a protocol: number every claim, then take the strikes.
   - `outreach-dm`, about 440 words, is a craft recipe: three parts of a message, plus a checklist file beside it.
   - `create-valuable-software`, about 1,200 words, is a lecture. It builds a model of the world from the bottom up (neurons, glycogen, reward) before it gives any steps.

   The length follows from how much the reader's beliefs have to change. A reframe or a protocol works on a reader who already sees the world correctly. A lecture has to change how they see it first.
2. **A description that says when to call it and what calling it earns.** "This skill teaches you how to get good at writing outreach DMs." "Call this skill to learn how to build valuable software for humans - the neuroscience under the hood." An agent calls a skill because of what it will gain from it.
3. **Give the mechanism, and derive the behaviour from it.** `claims` opens with why misalignment hides in implicit claims. `create-valuable-software` builds to one law ("A person only keeps doing something while the expected reward of the next step is greater than its cost...") and draws its guards from that law. A reader who has the mechanism can handle cases you never listed.
4. **Name the common failure outright.** "Every other AI DM skill recommends saying something specific about that person ... being specific about them is no longer pattern breaking." Naming the naive move is what moves the reader off its default.
5. **Point at the evidence instead of inlining it.** End with a "More" list of library runbooks and worked examples. Put checklists in a file beside the skill (`tics.md`).

Trust the reader. A skill that tries to specify everything gets followed like a parts list, and the work comes back weirdly specific.

With the draft on disk, read it back against the ways Claude-written instructions fail: padding, steps more specific than the job needs, a rule added because something went wrong once, "never" written for "not now". Fix every one you find. The user (11-27 17:04): "write up the draft ... *then* read the claude failure modes ... and *then* fix the draft."
