import requests
import json
from requests.auth import HTTPDigestAuth

# 🗝️ MongoDB Atlas API credentials (replace with your actual keys)
PUBLIC_KEY = "wyxkjajv"
PRIVATE_KEY = "1259656c-bba5-4e7c-b706-b0157938c8dd"
PROJECT_ID = "67f4e7ff2532591a83cf4f1a"
CLUSTER_NAME = "Cluster0"  # Change if your cluster has a different name
DB_NAME = "rag_db"
COLLECTION_NAME = "embeddings"

# 🛠️ Endpoint for creating a Search Index
url = f"https://cloud.mongodb.com/api/atlas/v1.0/groups/{PROJECT_ID}/clusters/{CLUSTER_NAME}/fts/indexes"

headers = {
    "Content-Type": "application/json"
}

# 🧠 Vector Search Index Definition (384 dimensions for MiniLM)
index_definition = {
    "collectionName": COLLECTION_NAME,
    "database": DB_NAME,
    "name": "embedding_vector_index",
    "mappings": {
        "dynamic": False,
        "fields": {
            "embedding": {
                "type": "knnVector",
                "dimensions": 384,
                "similarity": "cosine"
            }
        }
    }
}

# 🧪 Make the API call
response = requests.post(
    url,
    auth=HTTPDigestAuth(PUBLIC_KEY, PRIVATE_KEY),
    headers=headers,
    data=json.dumps(index_definition)
)

# 📋 Print the result
print("✅ Status Code:", response.status_code)
print("🧾 Response Text:", response.text)
