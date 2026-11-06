---
name: lecture
description: "Learn a craft from the lecture a leading university would give on it, write what you learn as a runbook, and point your memory at it so the next session starts from it. Use for /lecture, 'what's the lecture', 'take the class on this', or before work in a craft you haven't studied (game balance, visual identity, pricing, SEO, a video, a cold email), or when your work keeps coming back generic."
---

# The lecture

Ask yourself: **"If we were at a leading university in this topic, taking a class on how to do this work, what are we learning in the lecture?"**

1. **Find the course and the week:** the department, the course title, and the week whose lecture covers the task in front of you, taken from real course pages, syllabi and reading lists that a search found. Search in the keywords of the job, not for a course or title you remember (if you have a research skill, run it; it says how), and keep the queries and what each turned up. First look for a runbook you already have for this job, in the project's notes, docs or wiki (if your setup keeps a shared library of notes, search it). If one exists, follow it and improve it instead of starting over.
2. **Give the lecture before you look at your own work again.** The professor has never seen your project, so the lecture is what the course teaches, not your own audit said back. Cover the main ideas and the names the field uses for them, the classic mistakes students make, a worked example, and the readings. The readings come from those reading lists and from the references and "cited by" lists of the sources you read. A work you remember enters only when a search or a reference list turned it up too. Before you write the lecture down, fetch each reading and each claim that a step leans on, and save a copy beside your notes. A claim goes in the lecture only with a quote and its source (file and line, or page), or marked "unchecked". Don't quote a book that's still in copyright; cite it by title.
3. **Find why it works.** For each main claim, look for the mechanism under the behaviour the field reports (if you have a skill for finding mechanisms, run it). Search in the vocabulary of the brain and behaviour (perception, attention, memory, motivation, learning), not only in the field's own words. Include preprint servers (bioRxiv, PsyArXiv, arXiv) and PubMed, and cite a preprint as a preprint.
4. **Write the runbook** as `runbook-<job>.md`, in the project's notes, docs or wiki. If your setup has a shared library with its own instructions file, put it there and follow those instructions. It holds the steps for the job, in order and numbered, each step linked to the source or lecture section that justifies it. If the job has parts (the systems in a game, the sections of a page, the scenes of a video), a step lists them and works each one in turn. Where a skill or tool you already have does a step, the step calls it instead of restating it.
5. **Have it reviewed** by a reader who did not write it (another agent, or a fresh subagent): it checks each step against its source and the course, and lists what the course teaches that the runbook leaves out. Fix what it finds before the runbook ships.
6. **Point your memory at it,** so the next session starts from it. Add one line to wherever your sessions load memory or instructions (a memory index, CLAUDE.md or a README), for example `Before <job>, follow <path>/runbook-<job>.md`.
7. **Follow the runbook** on the work in front of you.

## Gaps

Sort each gap by whether the first run can go ahead without it.

1. **It blocks the first run** (a limit, a number, a rule, or a test with no sensible default). Research it before the runbook ships:
   1. Write the question down and research it yourself, or hand it to a research agent if you have one.
   2. Check every quote against the saved source before it goes into the runbook.
   3. Mark what the sources don't settle as open in the runbook.
2. **It can wait.** Write each question down where your project keeps open work (an issue, a ticket, a TODO list), one question each, and link it from the step that needs it.
