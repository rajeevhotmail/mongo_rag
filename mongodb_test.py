from pymongo import MongoClient

# Replace <password> with your actual password

connection_string = "mongodb+srv://rajeevindia:Sherkhan%40123@cluster0.2pec5q4.mongodb.net/rag_test_db?retryWrites=true&w=majority&appName=Cluster0"


# Step 1: Connect to MongoDB
client = MongoClient(connection_string)

# Step 2: Create or select a database and collection
db = client["rag_test_db"]
collection = db["embeddings"]

# Step 3: Insert a sample embedding-like document
sample_doc = {
    "chunk_id": "001",
    "embedding": [0.12, 0.55, 0.93, 0.11, 0.77],  # Simulated vector
    "source": "README.md",
    "role": "programmer",
    "text": "This chunk explains how to set up the project."
}

inserted_id = collection.insert_one(sample_doc).inserted_id
print(f"Inserted document with ID: {inserted_id}")

# Step 4: Fetch and print it
retrieved = collection.find_one({"chunk_id": "001"})
print("Retrieved:", retrieved)