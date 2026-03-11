import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


# ------------------------------
# Load model only when needed
# ------------------------------
def get_model():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


# ------------------------------
# Create vector index
# ------------------------------
def create_vector_index(chunks):

    model = get_model()

    embeddings = model.encode(chunks)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index, embeddings


# ------------------------------
# Retrieve relevant chunks
# ------------------------------
def retrieve_relevant_chunks(topic, chunks, index, top_k=5):

    model = get_model()

    query_embedding = model.encode([topic])

    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    relevant_chunks = [chunks[i] for i in indices[0]]

    similarities = 1 / (1 + distances[0])

    confidence_score = float(np.mean(similarities) * 100)

    return relevant_chunks, confidence_score