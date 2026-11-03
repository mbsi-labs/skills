# Runbook: extract a brief

The steps for drawing a one-page brief out of someone who cannot say directly what they need: a client (Part A) or an Aion persona (Part B). A brief that comes back thin was filled from assumptions. Every field below must have a source: something the person said or did, with the time, or a line marked `guess:`.

The brief's fields: problem, objective, person, the feeling, insight, proposition, reason to believe, action, mandatories, limits, out of scope, judged by, sources.

## 1. Part A: a client

### 1.1 Before the interview

1. **Check the library** for the client and their trade: `qmd search "<client or trade>"`. Read the client's own site and anything they sent. You are learning their words, so your questions use them.
2. **Name who is in the room and who is not.** Who decides, who pays, who will say yes or no to the finished work, who uses the thing. Plan one interview per decider. Do not assume the person you are talking to is the one who judges.
3. **Write the goal** of the interview in one line: which fields of the brief you cannot fill yet.
4. **Write a discussion guide, not a script**. One topic per brief field, in the order of step 1.2.1. Write each question as a request for a past event ("tell me about the last time ..."), never "usually" and never yes or no. Do not write questions as "what are your expectations?" or "what features do you want?": they are the most common mistake.
5. **Fix how you will capture it.** Two people, or a recording with the client's consent.

### 1.2 In the interview

1. **Keep this order**:
   1. **Open.** Who you are, why you are asking, "there are no right answers; you won't hurt my feelings with negative feedback". Ask about their role first. This is rapport.
   2. **How it works today.** What the business does, who comes to it, how a customer finds them now. Ask who else I should speak to as the last question.
   3. **The problem, as an event.** "Tell me about the last time a customer ..." or "the last time the website let you down." The brief's Problem and Person come from this.
   4. **What has been tried.** "What have you tried before? How did it turn out? Why do you think it worked or missed?". The Insight (a tension in their own words) is usually here.
   5. **Success in their terms.** "What does success look like for you, three months after this is live?" Then ask for the number or the event: "how would you know?". This is Objective and Judged-by.
   6. **The one thing.** "If a stranger only remembered one thing from the page, what should it be, and why would they believe it?" This is Proposition and Reason to believe. If the answer has "and" in it, ask which half matters more.
   7. **Limits.** Deadline, budget, what must be reused, what is out. Technical points go here, last.
   8. **Close.** Read the brief back in outline (step 1.4). Thank them.
2. **Probe, don't accept the first answer**: "Can you give me an example?", "Tell me more about that", "Why is that important to you?". Go one level further than feels polite. Ladder: attribute (what it is), benefit (what it does for them), consequence (what that means for their day), emotional end (how they want to feel). Do not skip a level.
3. **Ask for the feeling by asking for the moment.** "When that happened, what was going through your head?" The brief's feeling field needs a feeling a person had in a moment, not an adjective.
4. **Stay silent after an answer** for a few seconds. Do not suggest an answer. Do not use leading wording.
5. **Mark contradictions** when they say one thing and describe another, and come back to them: "You said X, and earlier you told me Y. Help me understand.".
6. **Do not ask a technical question** unless you know they can answer it. If they do not know a word, stop and use theirs.

### 1.3 After the interview, before writing

1. **Transcribe or tidy your notes the same day.** Mark each fact with the time or the quote.
2. **Sort what you heard in three piles:** said and meant (they gave an event), said but unsupported (an opinion or a reason with no event behind it), and not said (fields still empty).
3. **Write the brief** from the first pile. Put the second pile in only as `guess:` lines. For the third, either ask again (step 1.4) or leave the field empty and say so in Sources. Do not fill it from your own assumptions.
4. **List the contradictions** you marked and what each could mean.

### 1.4 Check it back

1. **Send or show the one-page brief within two days.** Do not ask "does this look right?": people say yes to be agreeable.
2. **Ask them to say it back in their own words:** "If you were telling your partner what this page is for, what would you say?" Compare it to the Proposition, Person and Action. A gap is a field you got wrong.
3. **Test the fields with a case.** Give a concrete situation ("a customer finds you on her phone at night; what should she see first?") and see whether their answer matches the brief.
4. **Ask what is missing and who else should see it**.
5. **Mark the brief with the date it was confirmed and by whom.** Member checking has traps: do not hand over raw transcripts, and do not reopen a field they have already confirmed without telling them why.
6. **Update the brief and the Sources line.** Fields still `guess:` after the check-back stay marked.

## 2. Part B: an Aion persona

Aion is a role-play model: it feels what a person feels and invents everything else. The persona has no hidden memory to surface. What the interview does is draw specific, felt detail out of a person-in-a-moment. The result is a set of hypotheses, not a client's word. A real person's check (step 2.5) stays the test.

### 2.1 Choose the persona

1. **Find before you create.** Look for a persona you already have for this project, and use it. Never invent one yourself.
2. **Read the file.** Note the `kind:`, `reader:` line and what the body states as fact. These are the only facts; anything else Aion says is a guess.
3. **Check the date and the project.** An old persona may describe a different product.

### 2.2 Set up

1. **Run `aion status`.** A refused call means a cap was reached: stop and tell the owner.
2. **Start a session:** `aion ask --session <name> --persona <file> --attach <each source> "<prompt>"` (`aion help`). Attach every source it should speak from; given nothing it invents one.
3. **Forward only what is current.** Cut old versions of the facts. Never include examples of answers; Aion reuses their words.
4. **One job per call, written short and friendly,** as a person asks a writer.

### 2.3 Interview the persona

1. **Use the same order as Part A (step 1.2.1)**, one turn per topic, in the same session so it stays in character.
2. **Ask for events, not reasons.** "Tell me about the last time ..." Ask what happened next and what they did, not why in general.
3. **Ask for feelings one step at a time, each with a probability:** "What does she feel next? Five feelings, each with a probability.". The probabilities are Aion's, not data; use them to choose which feeling to check first.
4. **Probe as in Part A:** "Tell me more", "what happened right after that". Ladder up from what they saw to what it meant to how they wanted to feel.
5. **Ask the success and one-thing questions last,** after the event and the feeling are on the page.
6. **For a design brief, give one turn to the surface:** ask the persona to describe the version that makes them stay as a designer would draw it (layout, density, type, colour, how one item is drawn), not its words. Questions about content alone leave the design unasked.
7. **Do not ask Aion a question of fact** about the world, the product, a price, a law, or how Aion works.
8. **Read the transcript:** `aion transcript <name>`. Mine it, don't skim.

### 2.4 Write the brief

1. **Fill the fields from the transcript and the persona file.** Everything from the transcript is a hypothesis: prefix it `guess:` unless the persona file states it.
2. **Scan for your own words.** If a phrase you gave Aion comes back as its conclusion, the prompt leaked; re-ask without it.
3. **Check its facts yourself** against current sources, and mark what it invented. An invented fact about the world, the product or a person stays a guess.
4. **Send Aion's people-facing output to the owner as it is,** before you filter, rank or rewrite it.

### 2.5 Check it back

1. **Teach-back in a fresh session** (the same persona, no earlier turns): attach the finished brief and ask the persona to say, in their own words, what this page is for and what they would do on it. Compare with the Proposition and Action.
2. **Test with a case:** a concrete moment, one question at a time, and see whether the persona's answer matches the Person and Insight fields.
3. **List what stays a guess,** and hand the brief to the person who will test it with a real client or customer (the owner decides). Do not call a persona brief confirmed.

## 3. Open questions

1. **Does a persona brief match a real client's?** No study found.
2. **Reynolds and Gutman, Birt et al. and Ferrari et al.** were not retrieved in full. If a step leans on them, re-read them before relying on it.
