---
name: design-docs
description: Write the design a person reviews before non-trivial code: by default the bronze tier (the ticket, the proposed types down to their leaves, the state machine, and the assumptions), recorded on the ticket or task it belongs to. Upgrade to silver (scenario traces, a standards check) or gold (an explainer film) only when the change calls for it. Use before writing or changing non-trivial code, when asked for a design or a design doc, or when a design was pushed back on.
---

# Design docs

A design ties the history together: **this kind of ask ⇒ these types ⇒ these functions**. The person reviewing mostly reads the assumptions, because that's where they notice a wrong turn and steer. Write the smallest design that lets them do that.

## Bronze: the default

Five parts, in this order, and nothing else:

1. **The ticket.** What the change does and why, in two or three sentences, with the person's words that started it (verbatim, with the time).
2. **The proposed types, in the real language, down to the leaves.** Every type the change adds or changes, as code. Then a short **Leaves** line: each name the types use, existing ones named as they are, new ones with what they wrap and what their parser refuses. Model states as union variants with their own fields. A reviewer should never meet a name the design doesn't define.
3. **The state machine.** Every module is a state machine and every program is a state machine of modules ([state-machines.md](state-machines.md)): its states, the events that move it, and the effects of each transition. A surface sends events in; a read-back reads state out.
4. **Assumptions.** Each one acceptable or rejectable on its own, none contradicting another. Keep them as their own list beside the types (where your tracker has a design record with an assumptions field, that field), so the reviewer can mark the wrong ones; the count of wrong ones per author is a measure to drive to zero. Every choice you made that the person might make differently goes here, including choices about what is left out.
5. **Serves.** Software is leverage over information: a build that fits one case, when a data file could switch it between several, is a one-off that someone rebuilds. Name the other cases this build serves and the data file or type that switches between them. Keep it beside the types as a record (where your tracker has a `serves` field, that field; refuse a design that lacks it): `{"also": ["<another case>"], "by": "<data file or type>"}`, or `{"oneOff": "because <why only this case>"}`. A case the plan treats as a choice between options is a case to list under `also`.

Writing it is where you find the gaps: if an assumption has no type behind it, or a type has no reason in the ticket, fix the model before recording it.

Record it wherever your team tracks work, attached to the ticket or task, and ask the person for a look. The person's answers go on the ticket verbatim, and into the next revision beside the assumption they answer.

## When to upgrade

- **[Silver](silver.md):** the change has behaviour over time or several actors (retries, concurrent writers, scenarios a reviewer can't check from the types alone), or the person couldn't follow the bronze. Adds traced scenarios, a Quint model check of the state machines, and a standards check.
- **[Gold](gold.md):** a design the person needs to *see* happen: an explainer film. Only when they ask for it.
