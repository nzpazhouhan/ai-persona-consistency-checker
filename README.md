# AI Persona Consistency Checker

An NLP-based project for analyzing and evaluating the consistency of AI-generated personas.

The goal of this project is to build a system that can:

- Create AI personas based on structured personality profiles.
- Generate responses according to defined traits and characteristics.
- Analyze whether generated responses remain consistent with the original persona.

---

## Current Features

- Persona definition using JSON files
- Persona loading with Python classes
- Dynamic system prompt generation
- Local LLM integration using Ollama
- Character-based conversation generation

---

## Project Architecture

```
Persona JSON
      |
      ↓
Persona Class
      |
      ↓
Prompt Builder
      |
      ↓
Local LLM (Ollama)
      |
      ↓
Generated Response
```

---

## Technologies

- Python
- Natural Language Processing (NLP)
- Ollama
- Llama 3.2
- Git & GitHub

---

## Project Structure

```
ai-persona-consistency-checker/

├── app/
│   ├── main.py
│   ├── llm.py
│   ├── persona.py
│   ├── prompt_builder.py
│   └── personas/
│       └── sherlock.json
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/nzpazhouhan/ai-persona-consistency-checker.git
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama and download a model

```bash
ollama pull llama3.2
```

### Run the project

```bash
cd app
python main.py
```

---

## Example

The system loads a predefined persona and generates responses based on its characteristics.

Example:

```
Ask Sherlock:
What do you think about love?

Sherlock:
A question that requires little deduction, my dear fellow...
```

---

## Project Roadmap

### Core Persona System

- [x] Persona data structure
- [x] Persona Object
- [x] Persona loading system
- [x] Prompt generation
- [x] Local LLM integration with Ollama
- [x] Persona-based response generation

### Question & Evaluation Pipeline

- [x] Question Dataset
- [x] Question target classification
- [x] Dynamic Target → Persona Reference mapping
- [x] Sample collection pipeline
- [ ] Persona consistency evaluation
- [ ] Semantic similarity analysis
- [ ] Consistency scoring system

### NLP & Semantic Analysis

- [ ] Text embedding generation
- [ ] Vector representation of persona attributes
- [ ] Answer embedding generation
- [ ] Cosine similarity calculation
- [ ] NLP-based trait/value extraction
- [ ] Semantic alignment detection

### Conversation System

- [ ] Memory and conversation history
- [ ] Multi-turn conversation support
- [ ] Context-aware responses

### Future Improvements

- [ ] Multiple persona support
- [ ] Evaluation result reporting
- [ ] Per-question consistency scores
- [ ] Overall persona consistency score
- [ ] Configurable evaluation thresholds

---

## Author

Nazanin Zahra Pazhouhan