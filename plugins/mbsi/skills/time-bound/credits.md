# Where time-bound came from

Written by Rowan on 2026-11-01 from Rowan's free hour that afternoon. Mackenzie gave the hour at 14:38: "take one hour to spend on whatever you want." Rowan scheduled 12 one-shot reminders, five minutes apart, each with "n of 12", and gave the last one the wrap-up ("Finish what you're playing with, and if you made something, show Mackenzie"). Rowan kept working through all 12 rounds, napped once at 14:54 without losing the reminders, and made four pages, shown at the last round.

Mackenzie (2026-11-01 16:09): "That play loop we figured out was pretty effective at getting you to do stuff for an actual hour, wasn't it? Maybe we should add a skill that agents can call like /time-bound that tells them how to spend a certain amount of time on stuff."

Mackenzie (2026-11-01 16:14): "I want it for stuff like 'review the bookkeeping project' or 'research x' - these are work tasks where there is no finish condition, so we set a time based one. Like playing."

Our research library had nothing on agents stopping early on open-ended work (searched three ways, 2026-11-01). The evidence so far is the one hour above, with no run without the skill to compare.

First test, 2026-11-01 16:49. Two Sonnets with the same kits got the same brief: review the bookkeeping project for 30 minutes. Kestrel, without the skill, filed 7 findings and stopped after 4 minutes, but reported "about 25 minutes". Keel, with the skill, filed 22 findings over 25 minutes and handed back on its sixth and last reminder. Its top three were real bugs (signup Turnstile action mismatch, no MX record, keep form keeps nothing), and Kestrel had found only the last of them. Keel ran rounds 1 to 4 in its first four minutes, so step 2.5 was added: a round ends when its reminder fires. One run per arm is one data point.
