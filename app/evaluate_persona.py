import json

from prompt_builder import build_persona_prompt
from llm import ask_llm
from evaluator import evaluate, get_reference


CATEGORY_MAP = {
    "personality": [
        "traits",
        "emotional_patterns",
        "cognitive_style",
        "social_style",
        "behavioral_patterns"
    ],

    "values_motivation": [
        "core_values",
        "moral_principles",
        "beliefs",
        "boundaries",
        "goals",
        "drives",
        "ambitions"
    ],

    "decision_making": [
        "decision_making"
    ],

    "communication": [
        "communication"
    ],

    "relationships": [
        "relationships"
    ]
}


def flatten_reference(value):

    if isinstance(value, str):
        return [value]

    if isinstance(value, list):
        result = []

        for item in value:
            result.extend(flatten_reference(item))

        return result

    if isinstance(value, dict):
        result = []

        for item in value.values():
            result.extend(flatten_reference(item))

        return result

    return []


def get_category_reference(persona, target):

    paths = CATEGORY_MAP.get(target, [])

    references = []

    for path in paths:

        value = get_reference(persona, path)

        references.extend(flatten_reference(value))

    return references


def evaluate_persona(persona):

    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)

    system_prompt = build_persona_prompt(persona)

    category_scores = {}

    print(f"\nRunning evaluation for {persona.name}...\n")

    for item in questions:

        question = item["question"]
        target = item["target"]

        reference = get_category_reference(persona, target)

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