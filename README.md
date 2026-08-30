# Persona Consistency Checker

A local LLM-based system for generating and evaluating consistent AI personas.

The project uses structured persona data, local LLM inference through Ollama, semantic embeddings, and consistency evaluation to determine whether an AI-generated response matches a predefined character.

---

# Project Goal

The goal of this project is to build a system that can:

1. Represent a fictional character as structured data.
2. Generate responses according to that character's personality.
3. Allow users to interact with multiple characters.
4. Evaluate whether generated responses remain consistent with the character.
5. Detect semantic alignment and contradictions.
6. Eventually evaluate consistency across entire multi-turn conversations.

---

# Current Architecture

```text
                    ┌──────────────────┐
                    │ Persona Dataset  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Persona Object │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Prompt Builder   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Ollama      │
                    │     Local LLM    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Generated Answer │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Evaluator     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Consistency Score│
                    └──────────────────┘
```

---

# Project Structure

```text
persona-consistency-checker/
│
├── app/
│   ├── main.py
│   ├── persona.py
│   ├── prompt_builder.py
│   ├── llm.py
│   ├── evaluator.py
│   ├── evaluate_persona.py
│   ├── questions.json
│   │
│   └── personas/
│       ├── sherlock.json
│       ├── batman.json
│       ├── harry_potter.json
│       ├── joker.json
│       └── tony_stark.json
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Master Roadmap

## Phase 0 — Project Foundation

- [x] Project structure
- [x] Virtual environment
- [x] Dependencies
- [x] GitHub repository
- [x] README foundation

---

# Phase 1 — Persona Representation

The persona system uses a shared schema for all characters.

```text
Persona
│
├── identity
│   ├── name
│   ├── description
│   └── background
│
├── personality
│   ├── traits
│   ├── emotional_patterns
│   ├── cognitive_style
│   ├── social_style
│   └── behavioral_patterns
│
├── values
│   ├── core_values
│   ├── moral_principles
│   ├── beliefs
│   └── boundaries
│
├── motivations
│   ├── goals
│   ├── drives
│   └── ambitions
│
├── preferences
│   ├── likes
│   ├── dislikes
│   ├── interests
│   └── hobbies
│
├── relationships
│   ├── friendship
│   ├── trust
│   ├── loyalty
│   └── attitude_toward_others
│
├── decision_making
│   ├── problem_solving
│   ├── risk_tolerance
│   ├── decision_style
│   └── response_to_uncertainty
│
├── communication
│   ├── tone
│   ├── humor
│   ├── verbosity
│   ├── language
│   └── mannerisms
│
├── knowledge
│   ├── expertise
│   ├── interests
│   └── learning_style
│
└── narrative
    ├── backstory
    └── important_events
```

### Status

- [x] Initial Persona structure
- [x] Initial Persona object
- [x] Initial Persona loader
- [x] Finalize rich Persona Schema
- [x] Update `persona.py` for final Schema

---

# Phase 2 — Persona Dataset

All characters must use the same schema.

Current characters:

```text
Sherlock Holmes
Batman
Harry Potter
Joker
Tony Stark
```

## Sherlock Holmes

- [x] Complete identity
- [x] Complete personality
- [x] Complete emotional patterns
- [x] Complete cognitive style
- [x] Complete social style
- [x] Complete behavioral patterns
- [x] Complete values
- [x] Complete motivations
- [x] Complete preferences
- [x] Complete relationships
- [x] Complete decision making
- [x] Complete communication
- [x] Complete knowledge
- [x] Complete narrative

## Batman

- [x] Complete Persona

## Harry Potter

- [x] Complete Persona

## Joker

- [x] Complete Persona

## Tony Stark

- [x] Complete Persona

### Dataset rule

Every character should have comparable coverage across the schema while maintaining character-specific information.

---

# Phase 3 — Question Dataset

The question dataset is used to probe different aspects of each persona.

Initial target:

```text
100+ questions
```

The dataset may eventually grow to:

```text
200–300+ questions
```

## Question Categories

```text
direct
scenario
moral_dilemma
emotional
problem_solving
decision_making
communication
conflict
relationship
preference
hypothetical
```

## Question Structure

```json
{
    "question": "...",
    "target": "...",
    "focus": ["...", "..."],
    "type": "..."
}
```

### Status

- [x] Initial question dataset
- [x] `target`
- [x] `focus`
- [x] `type`
- [x] Expand to 100+ high-quality questions
- [ ] Remove redundant questions
- [x] Map questions to the new Persona Schema


---

# Phase 4 — Persona Conversation System

The application currently supports interactive conversations with multiple characters.

```text
User
 ↓
Character Selection
 ↓
Persona Loading
 ↓
Prompt Generation
 ↓
Ollama
 ↓
Character Response
```

### Status

- [x] Character selection
- [x] Numeric menu
- [x] Multiple personas
- [x] Connect/disconnect
- [x] User input
- [x] `q` command
- [x] Persona-specific system prompt
- [x] Ollama integration
- [x] Short response control
- [ ] Conversation history
- [ ] Multi-turn context
- [ ] Memory system

---

# Phase 5 — Prompt Engineering

The prompt builder converts structured Persona data into an LLM system prompt.

### Completed

- [x] Basic persona prompt
- [x] Identity injection
- [x] Traits injection
- [x] Values injection
- [x] Likes/dislikes injection
- [x] Speaking style
- [x] Backstory
- [x] Concise response guidelines

### Remaining

- [ ] Adapt prompt to the new Persona Schema
- [ ] Selectively inject relevant Persona information
- [ ] Prevent unnecessary verbosity
- [ ] Reduce generic LLM behavior
- [ ] Reduce catchphrase overuse
- [ ] Improve character-specific voice

---

# Phase 6 — Evaluation Pipeline

The evaluation pipeline determines how closely an answer matches the Persona reference.

```text
Question
   ↓
Character
   ↓
LLM Answer
   ↓
Persona Reference
   ↓
Embedding
   ↓
Semantic Similarity
   ↓
Score
```

### Current implementation

- [x] `evaluator.py`
- [x] Sentence Transformers
- [x] Embedding generation
- [x] Cosine similarity
- [x] Per-question score
- [x] Average score
- [x] `/evaluate`
- [x] Automatic character selection

### Remaining

- [ ] Adapt evaluator to new Persona Schema
- [ ] Use `focus` properly
- [ ] Generate relevant reference text
- [ ] Compare answer against relevant Persona attributes
- [ ] Per-question evaluation
- [ ] Category-level scores
- [ ] Overall consistency score
- [ ] Handle empty references
- [ ] Handle conflicting references

---

# Phase 7 — NLP / Semantic Analysis

This phase expands the basic embedding-based evaluator.

## Embeddings

- [x] Sentence embedding
- [x] Reference embedding
- [x] Answer embedding
- [x] Cosine similarity

## Improvements

- [ ] Compare against multiple reference embeddings
- [ ] Weighted similarity
- [ ] Focus-aware similarity
- [ ] Category-specific scoring
- [ ] Score normalization
- [ ] Evaluation thresholds
- [ ] Semantic contradiction detection

Example:

```text
Persona Value:
truth

Generated Answer:
"I believe deception is always justified."

        ↓

Semantic / contradiction analysis

        ↓

Consistency penalty
```

---

# Phase 8 — Advanced Evaluation Architecture

The evaluator should eventually move beyond simple cosine similarity.

```text
                         ┌── traits
                         ├── values
Answer ──────────────────┼── emotions
                         ├── motivations
                         ├── relationships
                         ├── decision making
                         └── communication
                                  │
                                  ▼
                           Category Scores
                                  │
                                  ▼
                         Weighted Aggregation
                                  │
                                  ▼
                       Persona Consistency Score
```

### Planned scores

- [ ] Trait consistency
- [ ] Value consistency
- [ ] Emotional consistency
- [ ] Motivation consistency
- [ ] Relationship consistency
- [ ] Decision-making consistency
- [ ] Preference consistency
- [ ] Communication consistency
- [ ] Overall consistency

---

# Phase 9 — LLM-as-Judge

A second evaluator can be added to capture semantic relationships that embeddings alone may miss.

```text
Generated Answer
       │
       ├──────────────► Embedding Evaluator
       │                       │
       │                       ▼
       │                     Score
       │
       └──────────────► LLM Judge
                               │
                               ▼
                             Score
                               │
                               ▼
                       Combined Evaluation
```

The LLM evaluator may analyze:

- contradiction
- behavioral consistency
- tone
- reasoning style
- context
- implied values
- character-specific behavior

### Status

- [ ] LLM-based evaluator
- [ ] Evaluator prompt
- [ ] Compare embedding and LLM evaluation
- [ ] Hybrid scoring
- [ ] Evaluate evaluator reliability

---

# Phase 10 — Conversation Memory

The system will eventually support long-term persona consistency.

```text
User
 ↓
Question 1
 ↓
Answer
 ↓
Memory
 ↓
Question 2
 ↓
Answer
 ↓
Memory
 ↓
...
```

### Status

- [ ] Conversation history
- [ ] Multi-turn context
- [ ] Context window management
- [ ] Persona persistence
- [ ] Memory extraction
- [ ] Long-term consistency
- [ ] Personality drift detection

---

# Phase 11 — Evaluation Reporting

The evaluator should eventually provide structured reports.

Example:

```text
Sherlock Holmes
────────────────────────

Overall Consistency       0.84

Personality               0.91
Values                    0.87
Emotions                  0.76
Relationships             0.82
Decision Making           0.93
Preferences               0.79
Communication             0.88

────────────────────────

Weakest Area:
Emotional consistency
```

### Status

- [ ] Per-question results
- [ ] Category results
- [ ] Overall score
- [ ] Weakest categories
- [ ] Strongest categories
- [ ] JSON evaluation report
- [ ] CLI report
- [ ] Optional visualization

---

# Phase 12 — Testing & Benchmarking

The evaluator must be tested against intentionally consistent and inconsistent answers.

### Test Cases

- [ ] Consistent answers
- [ ] Intentionally inconsistent answers
- [ ] Ambiguous answers
- [ ] Paraphrased answers
- [ ] Short answers
- [ ] Long answers
- [ ] Contradictory answers
- [ ] Different question types
- [ ] Different characters

### Evaluation Quality

- [ ] Test score separation
- [ ] Establish evaluation thresholds
- [ ] Measure false positives
- [ ] Measure false negatives
- [ ] Create a benchmark dataset

Example target behavior:

```text
Consistent answer       → High score
Mostly consistent       → Medium-high score
Ambiguous answer        → Medium score
Inconsistent answer     → Low score
```

The actual thresholds must be determined through benchmarking rather than arbitrarily chosen.

---

# Phase 13 — Performance & Deployment

## Performance

- [ ] Measure LLM latency
- [ ] Optimize Ollama configuration
- [ ] Select appropriate model
- [ ] GPU/CPU optimization
- [ ] Embedding caching
- [ ] Avoid repeated model loading
- [ ] Optimize evaluation runtime

## Deployment

- [ ] Clean requirements
- [ ] Environment configuration
- [ ] `.env` where required
- [ ] Production configuration
- [ ] Error handling
- [ ] Logging
- [ ] API layer
- [ ] Web UI / frontend
- [ ] Backend deployment
- [ ] Frontend deployment
- [ ] Production testing

---

# Current Project Status

```text
Project Foundation
██████████  Done

Persona System
███████░░░  In Progress

Persona Dataset
██░░░░░░░░  In Progress

Question Dataset
████░░░░░░  In Progress

Conversation System
█████████░  Almost Done

Prompt Engineering
████████░░  In Progress

Evaluation
████░░░░░░  Basic Version

Semantic Analysis
███░░░░░░░  Basic Version

Advanced Evaluation
░░░░░░░░░░

Memory
░░░░░░░░░░

Reporting
░░░░░░░░░░

Benchmarking
░░░░░░░░░░

Deployment
░░░░░░░░░░
```

---

# Current Development Position

The current development path is:

```text
100+ Questions
       ↓
Shared Persona Schema
       ↓
┌───────────────────────┐
│ Sherlock Holmes       │
│ Batman                │
│ Harry Potter          │
│ Joker                 │
│ Tony Stark            │
└───────────┬───────────┘
            ↓
      Update persona.py
            ↓
   Update prompt_builder.py
            ↓
     Update questions.json
            ↓
       Update evaluator.py
            ↓
         Benchmark
            ↓
     Advanced Evaluator
            ↓
          Memory
            ↓
       Deployment
```

---

# Development Rule

The project follows the roadmap sequentially.

**Do not jump to a later phase before completing the current phase unless there is a clear architectural reason.**

## Current Phase

> **Persona Dataset → Complete all five personas using the shared Persona Schema.**

The immediate order of work is:

```text
1. Finalize Persona Schema
2. Complete Sherlock
3. Complete Batman
4. Complete Harry Potter
5. Complete Joker
6. Complete Tony Stark
7. Update persona.py
8. Update prompt_builder.py
9. Expand and remap questions.json
10. Update evaluator.py
11. Benchmark evaluation
```

---

# Technology Stack

- Python
- Ollama
- Local LLM
- Sentence Transformers
- PyTorch
- Hugging Face
- NumPy
- SciPy
- scikit-learn
- JSON

---

# Long-Term Goal

The final system should be able to connect a user to a selected persona and evaluate whether that persona remains behaviorally, semantically, emotionally, and conversationally consistent over time.

```text
User
 │
 ▼
Select Persona
 │
 ▼
Conversation
 │
 ▼
LLM Response
 │
 ├───────────────► Persona Memory
 │
 ▼
Evaluation Engine
 │
 ├── Personality
 ├── Values
 ├── Emotions
 ├── Motivations
 ├── Relationships
 ├── Preferences
 ├── Decision Making
 └── Communication
 │
 ▼
Overall Persona Consistency
```

---

## Author

Nazanin Zahra Pazhouhan