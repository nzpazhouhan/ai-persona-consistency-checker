from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer("all-MiniLM-L6-v2")


def evaluate(reference, answer):

    reference_text = ", ".join(reference)

    reference_embedding = model.encode(reference_text)

    answer_embedding = model.encode(answer)

    similarity = util.cos_sim(
        reference_embedding,
        answer_embedding
    )

    return similarity.item()
