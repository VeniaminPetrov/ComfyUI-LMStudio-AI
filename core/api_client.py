import json
import urllib.request
import urllib.error
import os
from .logger import PromptLogger

class LMStudioClient:
    def __init__(self, host=None, logger=None):
        self.host = host or os.environ.get("LMSTUDIO_URL", "http://127.0.0.1:1234")
        if not self.host.startswith("http"): self.host = f"http://{self.host}"
        self.logger = logger

    def fetch_models(self):
        try:
            endpoint = f"{self.host}/v1/models"
            with urllib.request.urlopen(endpoint, timeout=5.0) as response:
                data = json.loads(response.read().decode('utf-8'))
                return [m.get("id") for m in data.get("data", []) if m.get("id")]
        except: return []

    def chat_completion(self, model_id, messages, temperature=0.7, max_tokens=1024, seed=None):
        endpoint = f"{self.host}/v1/chat/completions"
        payload = {"model": model_id, "messages": messages, "temperature": temperature, "max_tokens": max_tokens}
        if seed: payload["seed"] = seed
        req = urllib.request.Request(endpoint, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(req, timeout=120.0) as response:
            res = json.loads(response.read().decode('utf-8'))
            content = res["choices"][0]["message"]["content"]
            if self.logger: self.logger.log_request(model_id, messages[0]['content'], content)
            return content
