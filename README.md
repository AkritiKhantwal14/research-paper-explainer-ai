# 📚 Research Paper Explainer AI

An AI-powered research assistant that helps users understand, analyze, compare, and interact with research papers using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Streamlit.

## 🚀 Features

### 📄 Paper Analysis
- Simple Summary
- Technical Explanation
- Beginner-Friendly Explanation
- Key Takeaways
- Quiz Generation

### 📖 Literature Review
- Single Paper Literature Review
- Multi-Paper Literature Review
- Comparative Analysis of Multiple Papers

### 🔍 Research Assistance
- Research Gap Analysis
- Future Scope Identification
- Related Paper Recommendations
- Citation Generation (APA, IEEE, MLA, Chicago)

### 🤖 RAG-Based Chat With Paper
- Ask questions directly from uploaded papers
- Semantic search using embeddings
- FAISS vector database retrieval
- Context-aware responses

### 💡 Project Generation
- Generate project ideas from research papers
- Beginner to Industry-level project suggestions
- Suggested tech stacks and challenges

### 📥 Export
- Save generated outputs
- Download analysis reports

---

## 🏗️ System Architecture

```text
Research Paper (PDF)
        │
        ▼
 Text Extraction (PyPDF2)
        │
        ▼
 Text Chunking
        │
        ▼
 Embedding Generation
 (Sentence Transformers)
        │
        ▼
  FAISS Vector Store
        │
        ▼
  Relevant Context Retrieval
        │
        ▼
      Llama 3
    (via Ollama)
        │
        ▼
 Generated Analysis
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI & NLP
- Ollama
- Llama 3
- Sentence Transformers

### Vector Database
- FAISS

### Document Processing
- PyPDF2

### Export
- python-docx

---

## 📂 Project Structure

```text
Research-Paper-Explainer-AI/
│
├── app.py
├── prompts.py
├── pdf_reader.py
├── chunker.py
├── retriever.py
├── docx_export.py
├── requirements.txt
├── README.md
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/research-paper-explainer-ai.git

cd research-paper-explainer-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download Ollama:

https://ollama.com

Pull Llama 3 model:

```bash
ollama pull llama3
```

or

```bash
ollama pull llama3:8b
```

### Run Ollama

```bash
ollama serve
```

### Start Streamlit

```bash
streamlit run app.py
```

---

## 📋 Supported Analysis Types

| Feature | Description |
|----------|-------------|
| Simple Summary | Easy-to-understand summary |
| Technical Explanation | Detailed technical breakdown |
| Literature Review | Structured literature review |
| Research Gap Analysis | Identify research gaps |
| Recommendations | Suggest related papers |
| Citation Generator | APA, MLA, IEEE, Chicago |
| Multi-Paper Comparison | Compare multiple papers |
| Chat With Paper | Ask questions using RAG |
| Project Ideas | Generate implementation ideas |

---

## 🧠 RAG Pipeline

1. Extract PDF text
2. Split into chunks
3. Generate embeddings
4. Store vectors in FAISS
5. Retrieve relevant chunks
6. Generate answer using Llama 3

This reduces hallucinations and improves accuracy when answering questions about research papers.

---

## 🎯 Example Questions

```text
What is the objective of this paper?

What dataset was used?

What are the limitations?

What future work is proposed?

Compare the methodologies used.

Generate project ideas from this paper.
```

---

## 📸 Screenshots

Add screenshots here:

```text
Screenshot_app.png


---

## 🔮 Future Improvements

- PDF Export
- PowerPoint Generation
- Research Trend Analysis
- Automatic Paper Retrieval from ArXiv
- Multi-Modal Research Assistant
- Citation-Based Responses with Page References
- Research Knowledge Graph

---

## 👩‍💻 Author

**Akriti Khantwal**

Built using:
- Python
- Streamlit
- Ollama
- Llama 3
- FAISS
- Sentence Transformers

---

