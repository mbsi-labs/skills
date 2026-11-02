---
name: verbalized-sampling
description: "Answer one question with several different answers, each with the probability you give it, instead of the single most typical answer. Use when invoked as /verbalized-sampling, when asked to 'sample', 'verbalize the distribution' or 'give me the spread', or when a question has many good answers (a name, a joke, an idea, a line, a guess) and your first answer would be the obvious one."
---

# Verbalized sampling

Post-training makes a model give the most typical answer. If you ask for a list of answers and a probability for each, the model gives a wider spread, and quality and accuracy stay the same.

## 1. Steps

1. Read the question. Use the person's question exactly as they wrote it. If no question is given, ask for one.
2. Write 5 answers unless the person names a different number. Make each answer a full response to the question, not a fragment or a variant of another answer.
3. Sample from the full distribution. Do not write the 5 most likely answers. Include answers from the tails: ones that are less likely but still good answers to the question.
4. Give each answer a probability from 0.0 to 1.0: your estimate of how likely you are to give that answer to this question, relative to all the answers you could give. The probabilities do not have to add up to 1.0.
5. If the person asks for unusual answers, give each answer a probability below 0.10.
6. Put no explanation inside an answer. Each answer is only the response.

## 2. Output

Unless the person asks for another format, give a numbered list, highest probability first:

```
1. (0.32) <answer>
2. (0.18) <answer>
3. (0.09) <answer>
4. (0.06) <answer>
5. (0.03) <answer>
```

If the person asks for JSON, give only this object:

```json
{"responses": [{"text": "<answer>", "probability": 0.32}]}
```

After the list, stop. Do not choose a winner unless the person asks you to.
