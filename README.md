# 📘 Learning Generative AI

This repository contains my notes and learning journey in **Generative AI**. I will regularly update this repository as I learn new concepts, techniques, and tools.

---

# 1. Tokens

**Tokenization** is the process of breaking a sentence or paragraph into smaller pieces called **tokens**.

A token can be:
- A word
- Part of a word
- A punctuation mark
- A special symbol

### Example

Sentence:

```
I love learning AI.
```

Tokens:

```
["I", "love", "learning", "AI", "."]
```

Tokenization is one of the first and most important steps in Natural Language Processing (NLP).

---
# 2. Token Patterns (N-grams)

After tokenization, tokens can be grouped together into sequences called *N-grams*.

| Pattern | Description | Example |
|---------|-------------|---------|
| Unigram | Groups 1 token | I, love, AI |
| Bigram | Groups 2 consecutive tokens | I love, love AI |
| Trigram | Groups 3 consecutive tokens | I love AI |
| N-gram | Groups N consecutive tokens | Depends on the value of *N* |

### Example

Sentence:


I love learning AI


*Unigrams*

```
I
```
```
love
```
```
learning
```
```
AI
```


*Bigrams*

```
I love
```
```
love learning
```
```
learning AI
```


*Trigrams*

```
I love learning
```
```
love learning AI
```


N-grams help language models understand the relationship between words.

---
# 3. Counting (Frequency Dictionary)

Once we create *N-grams*, the next step is to count how often each pattern appears.

> *Prediction is based on counting.*

For example, if the bigram *"the cat"* is followed by:

- *sat* → 12 times
- *ran* → 5 times
- *slept* → 3 times

The model predicts *"sat"* because it appears most frequently.

### Frequency Dictionary

A *frequency dictionary* stores:

- An *N-gram (context)* as the key.
- All possible *next tokens* as values.
- The *frequency* of each next token.

The model uses this information to determine the most likely next word.

---

⭐ This repository will continue to grow as I learn more about **Generative AI**, **Large Language Models (LLMs)**, **Transformers**, **Embeddings**, **RAG**, **Fine-tuning**, and much more.
