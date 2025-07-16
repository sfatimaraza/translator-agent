🌍 Translator Agent
🤖 Purpose
This project demonstrates the use of the OpenAI Agents SDK to build a custom multilingual translator agent. The agent takes any input sentence and returns translations in multiple languages.

🔧 Features
Accepts natural language input (e.g., Urdu, Arabic, etc.)

Translates into English, French, and Chinese

Uses a Large Language Model (LLM) to generate high-quality, context-aware translations

Built with modular agent components for easy extension

🛠️ Technologies Used
Python 🐍

OpenAI Agents SDK

(Attempted) Gemini API

dotenv (for environment variable management)

⚠️ Note on Gemini API
Currently, the OpenAIChatCompletionsModel is designed to work with OpenAI models like gpt-3.5 or gpt-4o. While this project uses a Gemini API key, full compatibility with Gemini via Agents SDK is not supported yet. For stable results, it's recommended to use OpenAI models.

🧪 Sample Input
arduino
Copy
Edit
"الفاظ وہ آئینہ ہیں جن میں دل کی تصویر نظر آتی ہے, translate into english, chinese"
📤 Sample Output
vbnet
Copy
Edit
English: Words are the mirror in which the image of the heart is seen.
Chinese: 言语是映照内心图像的镜子。
French: Les mots sont le miroir dans lequel se reflète l’image du cœur.
📂 How to Run
bash
Copy
Edit
uv run main.py
Make sure you have your .env file set up with:

ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
