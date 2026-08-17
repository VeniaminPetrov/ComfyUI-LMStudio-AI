import os, json, torch, numpy as np, io, base64
from PIL import Image
from .core.api_client import LMStudioClient
from .core.logger import PromptLogger

class LMStudioAI_Node:
    @classmethod
    def INPUT_TYPES(cls):
        client = LMStudioClient()
        models = client.fetch_models() or ["No models found"]
        return {
            "required": {
                "text_input": ("STRING", {"multiline": True, "default": ""}),
                "model_key": (models, ),
                "system_prompt": ("STRING", {"multiline": True, "default": "You are a helper."}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 2.0, "step": 0.1}),
                "max_tokens": ("INT", {"default": 1024, "min": 1, "max": 8192, "step": 128}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {"image": ("IMAGE",)}
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("Generated Text", "Request_log")
    FUNCTION = "process_request"
    CATEGORY = "ComfyUI-LMStudio-AI"

    def process_request(self, text_input, model_key, system_prompt, temperature, max_tokens, seed, image=None):
        client = LMStudioClient()
        logger = PromptLogger()
        messages = [{"role": "system", "content": system_prompt}]
        user_content = []
        if text_input.strip(): user_content.append({"type": "text", "text": text_input})
        if image is not None:
            img_np = (image[0].cpu().numpy() * 255).astype(np.uint8)
            buf = io.BytesIO(); Image.fromarray(img_np).save(buf, format="JPEG")
            b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            user_content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}})
        if not user_content: user_content.append({"type": "text", "text": "Analyze this."})
        messages.append({"role": "user", "content": user_content})
        
        try:
            res = client.chat_completion(model_key, messages, temperature, max_tokens, seed if seed != 0 else None)
            logger.log_request(model_key, text_input, res)
            return (res, "Success")
        except Exception as e:
            logger.log_request(model_key, text_input, "", error=e)
            return (str(e), "Error")

NODE_CLASS_MAPPINGS = {"LMStudioAI_Node": LMStudioAI_Node}
NODE_DISPLAY_NAME_MAPPINGS = {"LMStudioAI_Node": "🤖 LMStudio AI (Pro)"}
