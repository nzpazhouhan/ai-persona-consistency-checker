from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer("all-MiniLM-L6-v2")


def evaluate(reference, answer):

    if not reference:
        return None

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
