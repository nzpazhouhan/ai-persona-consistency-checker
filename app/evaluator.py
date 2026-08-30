from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer("all-MiniLM-L6-v2")


def get_reference(persona, target):

    value = persona

    for part in target.split("."):

        if hasattr(value, part):
            value = getattr(value, part)

        elif isinstance(value, dict) and part in value:
            value = value[part]

        else:
            return None

    return value


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


def get_focus_reference(persona, target, focus):

    category_paths = {
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

    paths = category_paths.get(target, [])

    references = []

    for path in paths:

        value = get_reference(persona, path)

        references.extend(flatten_reference(value))

    if not references:
        return None

    if not focus:
        return references

    reference_embeddings = model.encode(
        references,
        convert_to_tensor=True
    )

    focus_embeddings = model.encode(
        focus,
        convert_to_tensor=True
    )

    similarity_matrix = util.cos_sim(
        focus_embeddings,
        reference_embeddings
    )

    selected_references = []

    for row in similarity_matrix:

        best_index = row.argmax().item()

        selected_references.append(
            references[best_index]
        )

    return list(dict.fromkeys(selected_references))


def evaluate(reference, answer):

    if not reference:
        return None

    if isinstance(reference, str):
        reference = [reference]

    answer_embedding = model.encode(
        answer,
        convert_to_tensor=True
    )

    reference_embeddings = model.encode(
        reference,
        convert_to_tensor=True
    )

    similarities = util.cos_sim(
        reference_embeddings,
        answer_embedding
    )

    return similarities.mean().item()
