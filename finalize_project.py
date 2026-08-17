import os

project_root = "F:/Hermes/Herms_Teacher/ComfyUI-LMStudio-AI"
init_path = os.path.join(project_root, "__init__.py")
readme_path = os.path.join(project_root, "README.md")

with open(init_path, "w", encoding="utf-8") as f:
    f.write("from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS\n")
    f.write("__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']\n")

readme_content = """# ComfyUI-LMStudio-AI 🤖

A powerful custom node for ComfyUI that integrates **LM Studio** directly into your workflow. This node allows yous to use local LLMs (Large Language Models) and Multimodal models (Vision) to analyze text and images within your ComfyUI generation pipelines.

## ✨ Features

* **Multimodal Support:** Send both text prompts and images (automatically converted to Base64) to your local model.
* **Smart Logging:** Every request, including the prompt, response, and parameters, is automatically saved in a structured `prompt_history.jsonl` file for easy debugging and auditing.
* **Seamless Integration:** Automatically fetches all available models currently running in your LM Studio instance.
* **VRAM Friendly:** Designed to work alongside Comint-UI, allowing you to use local LLMs without breaking your workflow.
* **Advanced Parameters:** Control `temperature`, `max_tokens`, `seed`, and more directly from the node interface.

## 🚀 Installation

1. Clone this repository into your `ComfyUI/custom_nodes/` folder:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/YOUR_USERNAME/ComfyUI-LMStudio-AI.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r ComfyUI-LMStudio-AI/requirements.txt
   ```
3. Ensure **LM Studio** is running and the Local Server is active (default port `1234`).

## 🛠 Usage

1. Open ComfyUI.
2. Add the node: `ComfyUI-LMStudio-AI` -> `🤖 LMStudio AI (Pro)`.
3. Select your loaded model from the dropdown list.
4. (Optional) Connect an `IMAGE` input to analyze pictures using Vision models (like LLaVA or DeepSeek-VL).
5. Run your workflow! Check `prompt_history.jsonl` in the node folder to see your interaction history.

## 📝 License
MIT License.
"""

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"✅ Project finalized at: {project_root}")
print(f"✅ Created: __init__.py, README.md")
