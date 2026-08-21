import json
from persona import load_persona
from prompt_builder import build_persona_prompt
from llm import ask_llm
from evaluator import evaluate

with open("questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

persona = load_persona("personas/sherlock.json")

system_prompt = build_persona_prompt(persona)

samples = []

for item in questions:

    question = item["question"]

    target = item["target"]

    reference = getattr(persona, target)

    answer = ask_llm(system_prompt, question)

    score = evaluate(reference, answer)

    sample = {
        "question": question,
        "target": target,
        "answer": answer,
        "score": score
    }

    samples.append(sample)

    print(f"\nTarget: {target}")
    print(f"Reference: {reference}")
    print(f"Score: {score}")
    print(f"Answer: {answer}")
