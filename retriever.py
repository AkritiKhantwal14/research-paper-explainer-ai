from sentence_transformers import SentenceTransformer
import streamlit as st
import faiss
import numpy as np

@st.cache_resource
def load_model():
    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

model = load_model()
@st.cache_resource
def create_vector_store(chunks):

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(
        np.array(embeddings).astype("float32")
    )

    return index, chunks

def retrieve_chunks(
    question,
    index,
    chunks,
    top_k=3
):

    query_embedding = model.encode([question])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    retrieved = []

    for idx in indices[0]:
        retrieved.append(chunks[idx])

    return "\n\n".join(retrieved)