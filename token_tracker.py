from pymongo import MongoClient
from datetime import datetime

class TokenTracker:
    def __init__(self, mongo_uri, db_name="rag_db"):
        self.mongo_uri = mongo_uri
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db["token_usage"]

        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0

    def record_usage(self, usage):
        self.total_prompt_tokens += usage.prompt_tokens
        self.total_completion_tokens += usage.completion_tokens

    def get_total(self):
        return {
            "prompt": self.total_prompt_tokens,
            "completion": self.total_completion_tokens,
            "total": self.total_prompt_tokens + self.total_completion_tokens
        }

    def save_usage(self, repo_path, role, user="default-user"):
        record = {
            "user": user,
            "repo": repo_path,
            "role": role,
            "prompt_tokens": self.total_prompt_tokens,
            "completion_tokens": self.total_completion_tokens,
            "total_tokens": self.total_prompt_tokens + self.total_completion_tokens,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.collection.insert_one(record)
        print(f"✅ Token usage logged: {record['total_tokens']} tokens")
