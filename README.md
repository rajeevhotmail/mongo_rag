# mongo_rag

**mongo_rag** is a Retrieval-Augmented Generation (RAG) application designed to analyze GitHub repositories and generate role-specific PDF reports using OpenAI's ChatGPT. It stores vector embeddings in **MongoDB Atlas** for scalable retrieval.

---

## 🚀 Features

- Analyze a GitHub repo and generate answers tailored to a **target role** (e.g., Programmer, CEO, Sales).
- Answers are generated using ChatGPT and stored in structured markdown format.
- Generates a professional PDF report using WeasyPrint.
- Embedding vectors are stored and retrieved using MongoDB Atlas.
- Designed for multi-role analysis with reusable embeddings and reduced token cost.

---

## 🧠 Technologies Used

- Python 3.10+
- OpenAI (ChatGPT)
- Hugging Face Transformers
- MongoDB Atlas (vector storage)
- FAISS (fallback in earlier versions)
- Tree-sitter (syntax-aware chunking for Python/Java)
- WeasyPrint (PDF generation)

---

## 📦 Installation

```bash
git clone https://github.com/<your-org>/mongo_rag.git
cd mongo_rag
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
