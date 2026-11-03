---
name: time-bound
description: "Spend a set length of time on open-ended work that has no finish line (review a project, research a question, explore, play) with a countdown of reminders, one small checked piece per round, and a write-up shown at the last round. Use for /time-bound <minutes> <task>, or whenever you are told to spend a length of time on something."
---

# Time-bound work

Open-ended work has no "done", so you will stop at the first natural pause, often after ten minutes. A countdown of reminders keeps you on it for the time you were given. ([why](credits.md))

## 1. Set up

1. The length comes from the person who gave you the work. Do not choose one yourself.
2. Keep the work in one place: a ticket or task if you track work that way, or a notes file. Other work should not pull you away until the time is up.
3. Make one round per 5 minutes. With CronCreate (`recurring: false`), schedule one reminder for the end of each round. Each prompt names the task and its place: "Time-bound: review the bookkeeping project (round 4 of 12). Pick the next piece." The last prompt says: "Time-bound: <task> (round 12 of 12, the last one). Finish what you are on, write up what you found, and show it."
4. Say how many rounds there are and when the last one fires, then start round 1 at once.

## 2. Each round

1. Pick the next most useful small piece: one part of the project, one source, one question.
2. Do it, and check it against the real thing.
3. Add what you found to the running notes, then report it in one line.
4. When a thread runs out, open another one: a different part, a different source, a harder question. You are out of ideas, not out of time.
5. A round ends when its reminder fires, not when its piece is done. If you finish early, go deeper on the same piece until the reminder comes.

## 3. The last round

Finish the piece you are on. Write up the findings where their reader will look (a document for research, the ticket or issue for a review), show them, and close the task.

The reminders live in this session. They survive a context clear, but not the end of the session, and they fire only while you are idle.
