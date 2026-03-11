from utils.chunking import chunk_text
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model once
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieval_agent(topic, full_text):
    
    # 1. Chunk text
    chunks = chunk_text(full_text)
    
    if len(chunks) == 0:
        return "", 0.0

    # 2. Create embeddings
    embeddings = embed_model.encode(chunks)

    # 3. Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    # 4. Embed query
    query_embedding = embed_model.encode([topic])
    D, I = index.search(np.array(query_embedding), k=5)

    # 5. Retrieve relevant chunks
    relevant_chunks = [chunks[i] for i in I[0]]
    combined_text = " ".join(relevant_chunks)

    # 6. Confidence score
    similarities = 1 / (1 + D[0])
    confidence = float(np.mean(similarities) * 100)

    return combined_text, confidence