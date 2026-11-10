# skills

By Mackenzie Bowes, with MBSI's agents.

Skills for AI agents, made and tested by MBSI.

Install the collection in Claude Code:

```
/plugin marketplace add mbsi-labs/skills
/plugin install mbsi@skills
```

That installs every skill, shown as mbsi:<name>. To install just one, use `/plugin install <name>@skills` (do not install both ways: a skill would show twice).

| Skill | What it does |
|---|---|
| [be-ambitious](plugins/be-ambitious/README.md) | Before your agent starts, it asks what the job is really for and what an expert would do, then asks for more than you first typed. |
| [but-therefore](plugins/but-therefore/README.md) | Rebuilds a devlog or post as a chain of "but" and "therefore" instead of "and then". |
| [claims](plugins/claims/README.md) | It has your agent list every claim in a plan or sentence, the unstated ones first, numbered, so you can strike the wrong ones by number and it rebuilds from what's left. |
| [cognitive-prophylactics](plugins/cognitive-prophylactics/README.md) | Before you draft, it asks for one line: the situation your reader might meet and the move that lifts or lowers their standing in it. |
| [decide](plugins/decide/README.md) | It compares the options for each person a choice affects, including doing nothing, then shows you a short result you can check. |
| [design-docs](plugins/design-docs/README.md) | Writes a short design a person can steer before you build: the ticket, the types down to their leaves, the state machine and the assumptions, with silver and gold tiers when the change needs traced scenarios, a model check or a film. |
| [dig-apc](plugins/dig-apc/README.md) | After a failure, it has your agent write what it did and what it believed, as axioms, principles and cruxes, then test each belief to find the one that is wrong. |
| [encode-lessons](plugins/encode-lessons/README.md) | When the same correction comes up a second time, it picks the cheapest guard that holds it (a type, a lint rule, a hook or a script) instead of adding another line of text. |
| [eval-design](plugins/eval-design/README.md) | It turns 'is the agent better now?' into a question asked of many items of real work, with a named judge and a figure you can track. |
| [first-principles](plugins/first-principles/README.md) | When a rule changes, it redesigns the type model or module from the start instead of adding another special case. |
| [lecture](plugins/lecture/README.md) | Before work in a craft your agent hasn't studied, it gives the lecture a leading university would give on it, checks the claims and why they work, and writes the steps as a runbook its next session starts from. |
| [lever](plugins/lever/README.md) | When the work isn't trivial, it has your agent write the script that does it, rerun it on the first unit and diff the result against the hand version. |
| [prove-it](plugins/prove-it/README.md) | Before your agent says it is done, it runs the real program from outside and reads what it prints, instead of trusting a compile, a cached screenshot or its own word. |
| [scene-sections](plugins/scene-sections/README.md) | It sets each generated scene behind its section's words, drawn for where those words go, with its own render for phones and desktops. |
| [signal-chain](plugins/signal-chain/README.md) | It ranks ways of carrying a message by how costly each is for the reader to decode, from faces and voices to writing and symbols, so you choose the one they can afford. |
| [skill-design](plugins/skill-design/README.md) | A change to a skill, rule or hook ships only if it is small, one or two intentful edits, because every added line carries claims nobody checked. |
| [time-bound](plugins/time-bound/README.md) | time-bound turns "spend 30 minutes on this" into six five-minute rounds, each ended by a reminder the agent can't talk itself out of, so it keeps picking the next piece until the last round hands you the write-up. |
| [unblock](plugins/unblock/README.md) | Your agent proceeds on reversible work, settles the mechanics itself and shows what it did and why, and still asks first about what cannot be undone: deleting, spending money, or sending a message to a person outside the team. |
| [verbalized-sampling](plugins/verbalized-sampling/README.md) | Answer one question with several different answers, each with the probability you give it, instead of the single most typical answer. |
| [visual-hierarchy](plugins/visual-hierarchy/README.md) | Ranks everything on a screen by what the screen is for and who it is for, then makes that order visible with size, weight, space, grouping and position. |
| [why-this-piece](plugins/why-this-piece/README.md) | Before you write, it asks four questions in writing: the point of the piece, why a reader would care, the business goal, and what making it says about us. |

Third-party sources are listed in NOTICE.md. Each skill is licensed as its own folder says; the rest is MIT.
