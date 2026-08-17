import json
import datetime
import os

class PromptLogger:
    def __init__(self, log_filename="prompt_history.jsonl"):
        self.log_path = log_filename
    def log_request(self, model_name, user_input, response_text, error=None):
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "model": model_name,
            "prompt": user_input,
            "response": response_text,
            "status": "success" if error is None else "error",
            "error_details": str(error) if error else None
        }
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
