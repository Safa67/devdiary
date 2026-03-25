import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_note_with_llm(content: str ,mode: str = "ozet"):
    prompt= f"You are a software development assistant. Analyze the following note based on the '{mode}' mode. \n\nNOT:{content}"

    payload = {
        "model" : "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        result = response.json()
        return result.get("response", "Analiz alınamadı.")

    except Exception as e:
        return f"Ollama bağlantı hatası: {str(e)}"