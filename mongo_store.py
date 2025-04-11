# mongo_store.py
import sys
import json
from pymongo import MongoClient
import os
from datetime import datetime

# Store your MongoDB URI here or read from env
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://rajeevindia:Sherkhan%40123@cluster0.2pec5q4.mongodb.net/rag_db?retryWrites=true&w=majority")

client = MongoClient(MONGO_URI)
db = client["rag_db"]
collection = db["embeddings"]

mongo_uri = "mongodb+srv://rajeevindia:Sherkhan%40123@cluster0.2pec5q4.mongodb.net/?retryWrites=true&w=majority"



def insert_chunk(chunk_id, embedding, chunk: dict):
    doc = {
        "chunk_id": chunk_id,
        "embedding": embedding,
        "text": chunk["content"],
        "chunk_type": chunk["chunk_type"],
        "file_path": chunk["file_path"],
        "start_line": chunk.get("start_line"),
        "end_line": chunk.get("end_line"),
        "language": chunk.get("language"),
        "parent": chunk.get("parent"),
        "name": chunk.get("name"),
        "metadata": chunk.get("metadata", {})
    }
    return collection.insert_one(doc).inserted_id

def insert_syntax_errors_to_mongodb(errors, repo_path, mongo_uri=mongo_uri):
    if not errors:
        print(f"⚠️ No syntax errors to insert for repo: {repo_path}")
        return

    client = MongoClient(mongo_uri)
    db = client["rag_db"]
    collection = db["syntax_errors"]

    documents = []
    for error in errors:
        documents.append({
            "repository": repo_path,
            "file_path": error.get("file_path"),
            "language": error.get("language", "unknown"),
            "error_type": "SyntaxError",
            "description": error.get("error_msg"),
            "line_number": error.get("line_number"),
            "function_name": error.get("function_name"),
            "timestamp": datetime.utcnow().isoformat()
        })

    if documents:
        collection.insert_many(documents)
        print(f"✅ Inserted {len(documents)} syntax errors for repo {repo_path}")