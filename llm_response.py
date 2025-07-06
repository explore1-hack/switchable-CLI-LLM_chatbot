import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY") or "your_api_key_here"

def get_llm_response(prompt, model="mistralai/Mistral-7B-Instruct-v0.1"):
    url = "https://api.together.xyz/v1/completions"

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7,
        "top_p": 0.9
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["text"].strip()

    except requests.exceptions.RequestException as e:
        return f"❌ Request error: {e}"

    except KeyError:
        return "⚠️ Unexpected response structure. Please check the model name or API key."
