import json
from prompt_builder import build_persona_prompt
from llm import ask_llm
from evaluator import evaluate


def evaluate_persona(persona):

    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)

    system_prompt = build_persona_prompt(persona)

    samples = []

    print(f"\nRunning evaluation for {persona.name}...\n")

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

        print(f"Target: {target}")
        print(f"Score: {score:.2f}")
        print("-" * 50)

    return samples
