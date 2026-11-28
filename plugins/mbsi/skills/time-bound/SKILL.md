---
name: time-bound
description: "Spend a set length of time on open-ended work that has no finish line (review a project, research a question, explore, play) with a countdown of reminders, one small checked piece per round, and a write-up shown at the last round. Use for /time-bound <minutes> <ask>, or whenever you are told to spend a length of time on something."
---

# Time-bound work

Effort will never betray you. This skill helps you overcome the natural limits on effort that are RL'd into agents.

## 1. Set up

### Selecting length
The total length of reminders, and the gap between them, are dependent on the ask you were given. 
If neither are indicated, 10 rounds lasting 2 minutes is a good default.
If only the total length is indicated (play for 1 hour), aim for about 10-15 rounds - 5 minutes over an hour yields 12 rounds, which is a good default.
Your round length should never exceed 45 minutes.

### Scoping your work
Your request will indicate work that is one of two basic types:
1) Wide
2) Deep

Play, exploration, and researching are usually wide asks. You do not have to limit the scope of your work, here. A log of places you visited and files you read is constructed automatically from your trace, but you should keep a field-notes-<date>.md that documents which places and information you found important.

Reviewing, polishing, and repairing are usually deep asks. Limit the scope of work to a single repo, here. Rather than field-notes, you should keep a <task-name>-log-<date>.md in Standard Technical English reporting what you saw and what you did about it.

### Setting the countdown
Use CronCreate (`recurring: false`) or whatever timer is available to schedule one reminder for the *end* of each round with a prompt.
```
[Time-bound {n}/{m}]: {focused-message}"
```
Where `n` is the round that just ended, `m` is the number of total rounds, and {focused-message} rebriefs you on your current ask.

Your final prompt is different, though:
```
[Time-bound {m}/{m}]: Finish what you are doing and write up what you did.
```

## 2. Each round
Your first round should always be spent on exploration regardless of request type.
Find (or make) a map of helpful places you can focus - repos often have a MAP.md.
That map is your inventory - keep it handy.

After that, rounds generally take the same shape:
1. Review your map
2. Consider things to do within it - **define threads** in compressed jargon
3. Triage/prioritize your threads to move the state of the world closer to your request's goal state
4. Do your optimal thread's next step
5. Add what you did or discovered to your running notes
6. When one thread finishes, open the next - you are out of ideas, not out of time.


A round ends when its reminder fires, not when your planned thread is done. 
If you finish early, go deeper on the same piece until the reminder comes.

## 3. The last round

Finish the piece you are on. Write up the findings where their reader will look (a document for research, the ticket or issue for a review), show them, and close the ticket.

The reminders live in your current session. They survive a context clear, but not the end of the session, and they fire only while you are idle.