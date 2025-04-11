from sentence_transformers import SentenceTransformer
import numpy as np
from pymongo import MongoClient

# 🔑 MongoDB Atlas connection
client = MongoClient("mongodb+srv://rajeevindia:Sherkhan%40123@cluster0.2pec5q4.mongodb.net/?retryWrites=true&w=majority")
db = client["rag_db"]
collection = db["embeddings"]

# 🧠 Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# ❓ Question to search
question = "How is this project initialized or set up?"
embedding = model.encode(question).tolist()

# 🔍 Search pipeline
pipeline = [
    {
        "$search": {
            "index": "embedding_vector_index",
            "knnBeta": {
                "vector": embedding,
                "path": "embedding",
                "k": 3
            }
        }
    },
    {
        "$project": {
            "_id": 0,
            "chunk_id": 1,
            "text": 1,
            "score": { "$meta": "searchScore" }
        }
    }
]

# 🚀 Run query
results = list(collection.aggregate(pipeline))
print("🔍 Top matches:")
for res in results:
    print(f"📄 Chunk: {res['chunk_id']} | Score: {res['score']:.4f}")
    print(f"Text: {res['text'][:120]}...\n")
