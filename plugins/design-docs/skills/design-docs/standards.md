# Code standards: what a silver design is checked against

Each standard is a property of the code that a reviewer can check by reading it. In a silver design, list each standard that applies and say how the model meets it. Replace any of these with your team's own where it has one.

## Types

- **Invalid states can't be represented.** Each state is its own variant, with only its own fields and an explicit `kind` tag so it can grow. No optional field stands in for a state, no flag sits beside a value, and `null` never means more than one kind of absence.
  - Not this: `{ value?: number; isFloor?: boolean }`
  - This: `{ kind: "exact", value } | { kind: "atLeast", value } | { kind: "unknown" }`
- **Raw input exists only at the edge.** One parser turns wire data into domain types. Past it, nothing re-checks a string or guesses at a shape. The edge is anywhere outside text enters: arguments, files, a subprocess's output, the network.
- **A missing field becomes a named state, never a default.** The parser turns absence into its own variant (`{ kind: "unknown", why }`), never into `0`, `""` or `false`.
- **Domain values have their own types** (`TicketId`, `Instant`), never a bare `string` or number that could be mixed up with another. A real type, not a nickname: `struct TicketId(i64)`, never `type TicketId = i64`.
- **No `as any`, and no other cast past the parser.**
- **A type shared across a language boundary is defined once** and generated on the other side from a schema.
- **Matches on a union are exhaustive.** No default arm hides a variant added later.
- **A fixed set is checked through its type, never by comparing its text.** `status.isClosed()`, never `status == "done"`.
- **Rows are read by column name, never by position.**
- **A list of allowed values is its own named type,** never an inline literal union repeated in each field.
- **Each type is defined once.** Others derive from it rather than restating its fields.
- **Sibling modules never share a type** by one defining it and the other borrowing it, or by copying it. Either lift it into a module both import, make one module the parent of the other, or merge them.

## Behaviour

- **Every module opens with one paragraph:** what it is, and the promise it keeps.
- **Every module is a state machine,** and every program is a state machine of modules (see [state-machines.md](state-machines.md)).
- **Adapters hold no decisions.** An HTTP handler, CLI command or tool call translates the wire into one event and the resulting state back.
- **Names are the domain's words** and say what a thing is or does. When code needs a comment to explain what it does, the name is wrong.

## Comments

No comment is the default. A comment that stays is written for someone reading the code later, stays true exactly as long as the code beside it, and is needed: without it a capable reader would plausibly change the code wrongly. A comment stating a rule a type could enforce is a missing type (`// never empty` should be `NonEmpty<T>`). What the change did belongs in the commit message, and what is left to do belongs in the ticket.

## Failure and honesty

- **Every error message comes from one catalogue per package.** Errors are variants of that package's error type, each variant's words written once. No function returns a free-text error.
- **Every error names what failed, the rule it broke and what to do next.**
- **Uncertainty is visible.** An estimate or a floor is typed and shown as one; "couldn't read" is never `0` or blank.
- **Numbers people see are computed by code,** never written by a model.

## Dependencies

- **Deep, hard layers come from libraries; thin layers are yours.** Depend on libraries for windowing, GPU, font shaping and parsers with years of edge cases. Write the widgets, styling and glue yourself.
- **Every library call matches the pinned version's real API,** checked in its source, not recalled.
