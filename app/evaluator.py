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


def evaluate(reference, answer):

    if not reference:
        return None

    if isinstance(reference, str):
        reference = [reference]

    answer_embedding = model.encode(answer)

    scores = []

    for item in reference:

        reference_embedding = model.encode(item)

        similarity = util.cos_sim(
            reference_embedding,
            answer_embedding
        )

        scores.append(similarity.item())

    return sum(scores) / len(scores)
