from utils.chunking import chunk_text
from utils.embeddings import create_vector_index, retrieve_relevant_chunks


def analysis_agent(topic, full_text):
    chunks = chunk_text(full_text)
    index, _ = create_vector_index(chunks)

    relevant_chunks, confidence = retrieve_relevant_chunks(topic, chunks, index)

    return " ".join(relevant_chunks), confidence