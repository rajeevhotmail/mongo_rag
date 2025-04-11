# vector_search.py

from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

# MongoDB connection setup
client = MongoClient("mongodb+srv://rajeevindia:Sherkhan%40123@cluster0.2pec5q4.mongodb.net/?retryWrites=true&w=majority")
db = client["rag_db"]
collection = db["embeddings"]

# Load the model once (reuse this in your app if needed)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def query_similar_chunks(question, model, top_k=3):
    question_embedding = model.encode(question).tolist()

    pipeline = [
        {
            "$search": {
                "index": "embedding_vector_index",
                "knnBeta": {
                    "vector": question_embedding,
                    "path": "embedding",
                    "k": top_k
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

    results = list(collection.aggregate(pipeline))
    return [res["text"] for res in results]
