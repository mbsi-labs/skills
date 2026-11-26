# State machines: how a design models behaviour

Design each module as a state machine, and each program as a state machine of modules.

- Put a module's states in one union type, with each state its own variant carrying only its own fields.
- Put its events in a different union type.
- Write one transition function. It takes a state and an event and gives the next state and the effects.
- A surface is a CLI command, an HTTP route or a page. A surface sends events in and reads the state out. A surface does not make decisions.
- No classes, no inheritance, no methods that hide state.
- Types do not reach across modules. When two modules need the same type, either lift it out to a place both import from (when it is a fact about the domain, such as `Email`, `TicketId` or `Money`), or merge the modules (when it is a state or event variant: the split was wrong and they are one machine).

In a design, show the states, the events that move between them, and the effects of each transition. A step inside one function call is not a state.
