# State machines

Design each module as a state machine. Design each program as a state machine of modules.

Put the states of a module in one union type. Put its events in a different union type. Write one transition function. This function takes a state and an event. It gives the next state and the effects.

A surface is a CLI command, an HTTP route or a page. A surface sends events in and reads the state out. A surface does not make decisions.

Do not use classes. Do not use inheritance. Do not use methods that hide state.

Types do not reach across modules. When two modules need the same type, do one of two things:

1. Lift it out to a place both import from, if it is a fact about the domain (`Email`, `TicketId`, `Money`).
2. Merge the modules, if it is a state or event variant. The split was wrong, and they are one machine.
