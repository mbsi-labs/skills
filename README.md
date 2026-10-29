# skills

By Mackenzie Bowes, with MBSI's agents.

Skills for AI agents, made and tested by MBSI.

Install the collection in Claude Code:

```
/plugin marketplace add mbsi-labs/skills
```

Then install any skill below with `/plugin install <name>@skills`.

| Skill | What it does |
|---|---|
| [be-ambitious](plugins/be-ambitious/README.md) | Before your agent starts, it asks what the job is really for and what an expert would do, then asks for more than you first typed. |
| [but-therefore](plugins/but-therefore/README.md) | Rebuilds a devlog or post as a chain of "but" and "therefore" instead of "and then". |
| [cognitive-prophylactics](plugins/cognitive-prophylactics/README.md) | Before you draft, it asks for one line: the situation your reader might meet and the move that lifts or lowers their standing in it. |
| [decide](plugins/decide/README.md) | It compares the options for each person a choice affects, including doing nothing, then shows you a short result you can check. |
| [dig-apc](plugins/dig-apc/README.md) | After a failure, it has your agent write what it did and what it believed, as axioms, principles and cruxes, then test each belief to find the one that is wrong. |
| [encode-lessons](plugins/encode-lessons/README.md) | When the same correction comes up a second time, it picks the cheapest guard that holds it (a type, a lint rule, a hook or a script) instead of adding another line of text. |
| [eval-design](plugins/eval-design/README.md) | It turns 'is the agent better now?' into a question asked of many items of real work, with a named judge and a figure you can track. |
| [first-principles](plugins/first-principles/README.md) | When a rule changes, it redesigns the type model or module from the start instead of adding another special case. |
| [lever](plugins/lever/README.md) | When the work isn't trivial, it has your agent write the script that does it, rerun it on the first unit and diff the result against the hand version. |
| [prove-it](plugins/prove-it/README.md) | Before your agent says it is done, it runs the real program from outside and reads what it prints, instead of trusting a compile, a cached screenshot or its own word. |
| [scene-sections](plugins/scene-sections/README.md) | It sets each generated scene behind its section's words, drawn for where those words go, with its own render for phones and desktops. |
| [signal-chain](plugins/signal-chain/README.md) | It ranks ways of carrying a message by how costly each is for the reader to decode, from faces and voices to writing and symbols, so you choose the one they can afford. |
| [skill-design](plugins/skill-design/README.md) | A change to a skill, rule or hook ships only if it is small, one or two intentful edits, because every added line carries claims nobody checked. |
| [unblock](plugins/unblock/README.md) | Your agent proceeds on reversible work, settles the mechanics itself and shows what it did and why, and still asks first about anything hard to reverse, outward-facing or costly. |
| [why-this-piece](plugins/why-this-piece/README.md) | Before you write, it asks four questions in writing: the point of the piece, why a reader would care, the business goal, and what making it says about us. |

Third-party sources are listed in NOTICE.md. Each skill is licensed as its own folder says; the rest is MIT.
