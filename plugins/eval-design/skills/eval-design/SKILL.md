---
name: eval-design
description: Design evals for experiments on our environment. Use when you add evals, compare prompts or models, or check model behaviour.
---

# Eval design

## Words

- **Environment:** the briefs, skills, rules, harness, strategy, model and effort. We cannot change the model's weights.
- **Experiment:** one change to the environment, then runs of real tasks.
- **Eval:** a question and the figure that it produces. Ask the question of many items of work. Each answer is a number. A yes or no is a number. The answers together make the figure. The eval is both the question and the figure.
- **Judge:** the one who answers an eval's question: a program, the owner, or a model.
- **Rung:** one model at one effort. Opus medium is the top rung.
- **Owner:** the person whose judgement the work serves.
- **Lights out:** the work runs without a review by the owner. Lights out is the goal for all work.

## Kinds of eval

- **Capability eval:** a figure that we try to move. Read it as a trend. Do not put a bar on it, because agents hack bars.
- **Regression eval:** a figure that holds on this rung. It is a gate for each experiment and each step down.
- When a capability eval holds reliably, move it to regression.
- A gate without capability evals cannot improve. Do not use it until it has them.

## Write an eval

1. Write the question.
2. Write its answers as a list. Add "unsure" or "other". The judge picks one.
3. For each answer, write a child question that asks why. Its list also ends in "other".
4. Name the figure: the share of each answer over the items.
5. Name the judge.

**Every figure comes from a question. Do not add a figure that no question asks for. Each extra figure dilutes attention.**

Failure: "lines of test per line of code" is a figure. No question asks for it.

## Judge the judge

A model judge needs its own evals first. The owner and the judge answer the same items. The owner answers first.

- **Agreement:** the share of answers where the judge and the owner pick the same.
- **Correction:** the share of the owner's "unsure" or "other" answers where the judge named a reason and the owner accepted it on a look.
- **List gaps:** the share of "other" answers. When the judge picks "other", add the missing reason to the list.

Use a judge in place of the owner only on questions where its agreement holds.

## Climb

1. Keep the rung.
2. Change one part of the environment.
3. Read the capability evals.
4. Repeat until an eval holds at its goal.
5. Move the eval to regression. Remove the review that it measured.

## Step down

Do this after a loop is lights out.

1. Move to the next rung: Opus low, Sonnet high, then lower, then a local open model.
2. Run the regression evals.
3. If an eval fails, change the environment and run it again.
4. When all regression evals hold, step down again.

## Answer an eval

- Use items from real work.
- Record the model, effort and environment version on each run.
- Keep each output.
- Use a program as the judge when it can answer. Use a local model next. Use the owner last.
- Make the evals run in minutes.
- Start every repeat of every test at once, in parallel. Wait only where a step needs an earlier step's output. Use a batch API only when an hour's wait costs nothing.

API runs cost money. Before one, price it (the model, the number of calls, the tokens, the dollars) and get the owner's yes.

You skipped this skill if you cannot name the eval's question, its answers, its figure and its judge.
