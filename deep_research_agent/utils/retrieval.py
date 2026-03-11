from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = None


def get_model():
    global model

    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")

    return model


def retrieve_relevant_chunks(query, chunks):

    if len(chunks) == 0:
        return []

    model = get_model()

    query_embedding = model.encode([query])

    chunk_embeddings = model.encode(chunks)

    scores = cosine_similarity(query_embedding, chunk_embeddings)[0]

    ranked = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [r[0] for r in ranked[:5]]