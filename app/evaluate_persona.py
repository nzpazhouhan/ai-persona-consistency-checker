import json

from prompt_builder import build_persona_prompt
from llm import ask_llm
from evaluator import evaluate, get_focus_reference


def evaluate_persona(persona):

    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)

    system_prompt = build_persona_prompt(persona)

    category_scores = {}

    print(f"\nRunning evaluation for {persona.name}...\n")

    for item in questions:

        question = item["question"]
        target = item["target"]
        focus = item.get("focus", [])

        reference = get_focus_reference(
            persona,
            target,
            focus
        )

        answer = ask_llm(system_prompt, question)

        score = evaluate(reference, answer)

        if score is not None:
            category_scores.setdefault(target, []).append(score)

    print("\n" + "=" * 50)
    print(f"Evaluation Results — {persona.name}")
    print("=" * 50)

    overall_scores = []

    for category, scores in category_scores.items():

        category_score = sum(scores) / len(scores)

        overall_scores.append(category_score)

        print(f"{category}: {category_score:.2f}")

    if overall_scores:

        overall_score = sum(overall_scores) / len(overall_scores)

        print("-" * 50)
        print(f"Overall Consistency: {overall_score:.2f}")

    print("=" * 50)

    return category_scores
