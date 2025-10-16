import requests
import json

def query_ollama(prompt: str , model: str = "gemma3:1b") -> str:
    try:
        # Send prompt to Ollama server that is running locally
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt},
            stream=True   # Enable streaming mode
        )

        if response.status_code != 200:
            return f"Error: Ollama did not respond properly (status {response.status_code})"

        # Collect streamed responses line by line
        full_reply = ""
        for line in response.iter_lines():
            if line:  # avoid empty lines
                try:
                    data = json.loads(line.decode("utf-8"))
                    # Each chunk may contain partial text
                    if "response" in data:
                        full_reply += data["response"]
                    if data.get("done"):
                        break
                except json.JSONDecodeError:
                    continue  # skip malformed lines

        return full_reply or "No response from Ollama"

    except requests.exceptions.ConnectionError:
        return "Cannot connect to Ollama. Is it running? Try: 'ollama serve'"
    except Exception as e:
        return f"Unexpected error: {e}"
