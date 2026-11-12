# Agentic writing failure cases (check every draft against these before handing it back)

Sources: Wikipedia, "Signs of AI writing" (WikiProject AI Cleanup); prose-scrub's rules; the owner's "not good" on a devlog opening. Each case has an instance from that opening.

1. **Sanded-off voice.** The author's words are rough and specific: an exact count of minutes with exclamation marks, and a swear. The draft turns them into neat, calm sentences. Keep their words and their heat. Their voice is the proof a person wrote it.
2. **Generic where the material is specific.** The draft says "my pipeline" and "one of my agents" when the material names them (each agent's name) and gives numbers (81 release builds). Use the names and numbers.
3. **Vague cause.** The draft says "I gave every agent a home ... By that evening the suite ran in 13.5 seconds", which implies the homes made the tests fast. Homes made the waste visible. The fix was something else. Say what caused what.
4. **Rule of three.** "a name, its own terminal, a diary, and a hand-off note": a tidy list that looks complete and says little. Keep the one item that matters to the story.
5. **The punchline paragraph.** A short, quotable line closes the paragraph ("you can't engineer what you can't see", "The system was rotting."). One per piece at most, and only where the story earns it.
6. **Correct-the-misconception.** "It wasn't fine." Not X, but Y. Knocking down a claim nobody made.
7. **Promise without delivery.** "Here's how to build the same thing, and the repo to start from." It announces instead of doing. Give the first step itself.
8. **Formula title.** "Your agents are wasting hours you can't see": a second-person fear hook. The title names the gain with the specific thing in it.
9. **Flat rhythm.** Every sentence 8 to 15 words (prose-scrub burstiness 0.47; people sit at 0.6 to 1.2). Vary length on purpose.
10. **The too-neat arc.** Problem, realisation, fix, lesson, call to action, in five tidy paragraphs. Real stories have a wrong turn and a mess. Keep the mess the material has.
11. **No figure spots.** A figure artist draws figures where a mechanism or a before and after is hard to hold in words. Mark each spot after its passage with `<!-- figure: what it shows, and why it matters -->`. Every piece has at least two: the hero near the top, and the mechanism.
12. **Too short to carry the proof.** A reviewer called a 320-word opening too short. A devlog that stops after the opening gives the reader nothing to claim.
13. **Lecture before the answer.** The reader arrives holding the title's question. Same-topic pairs that real readers voted on (Stack Exchange, ELI5, HN) are won by the piece that opens with the usable answer and then backs it. Losers open with background, stay generic or wander, and leave the reader waiting. Pay the title's question in the first screen, then open the next one.
14. **Section as a slot.** A section written because articles have one (an "honest part", an install block, an ask) and not because the reader decides something there. For each section, name the decision it serves (start? was the promise real? is this about me? keep going? believe it? what now?) and what the reader gets. If you can't, cut it.
