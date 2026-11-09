# Silver: traces, state machines, a model check, a standards check

Silver is bronze plus what a reviewer needs when the types alone can't show the behaviour. Keep bronze's three parts, and add, in this order after the types:

1. **A roster table** of every name in the types (what it is, where it comes from, what its parser refuses), and a table of **which type owns which decision**.
2. **Each scenario traced as calls between the real types**: who calls whom with what, what comes back, which state changes, which rows or files are written. One trace per scenario: the ordinary path, the first run, each failure, each way a person gets involved. Draw the main path as a Flow (actors as steps, calls as links).
3. **The state machines** as Flows, with only states that exist in the types. A step inside one function call isn't a state.
4. **The state machines model-checked in Quint**, before the design is recorded. Write them as a `.qnt` model with every actor and every interruption the ask allows (crash, context clear, timeout, a second writer). State what must always hold and what must never happen, for the person and for the agents working under it. Run `quint run`, then `quint verify` one at a time under a memory cap. List each bad trace in plain words as a flaw in the design, with the change it calls for, or as a mistake in the model. Attach the `.qnt` to the ticket or task. Quint is the `quint` command; install it from https://github.com/informalsystems/quint, and read its language and modelling guides at https://quint-lang.org/docs. A module that is not named after its file needs `--main <module>`.
5. **A check against the code standards** ([standards.md](standards.md)): each standard that applies, and how the model meets it.
6. **What changed, and why**, per revision, quoting the review that caused it.

Then the assumptions, last.

- No metaphors and no stand-in characters: the actors are the real types under their real names.
- Write the traces before recording the design. A step the types can't do is a gap: fix the model and say so under "what changed".
- The shape to copy: a design for a recurring job (a scheduler that runs a task on a cadence), with its roster tables, one trace per scenario (ordinary run, first run, a failed run, a person stepping in), its state machines as flows, and a model check.
