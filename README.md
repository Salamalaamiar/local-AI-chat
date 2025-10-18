#  Local AI Chat

Backend :A lightweight **FastAPI backend** that connects your **React frontend** to a **locally running Ollama model (LLaMA, Gemma, Mistral, etc.)** for private, ChatGPT-style conversations — without any cloud dependencies.
Frontend: interface where user can interact with his AI local and send and recieves messages .

---

## Overview

This backend acts as a **bridge between the frontend and Ollama**:

1. The user sends a message via the chat interface (React app).
2. The FastAPI backend receives the request.
3. It forwards the prompt to the **Ollama server** (`http://localhost:11434/api/generate`).
4. The model generates and streams back the AI response.
5. The backend returns the final generated text to the frontend.

---

## 🧩 Tech Stack

- **Python 3.10+**
- **FastAPI** — REST API framework
- **Pydantic** — data validation for request/response models
- **Requests** — to communicate with the Ollama API
- **Uvicorn** — ASGI server for running FastAPI

---



## ⚙️ Setup Instructions

### Clone the repository

```bash
git clone https://github.com/Salamalaamiar/local-AI-chat.git
cd local-ai-chat/backend

```

---
### Create a virtual environment
```bash
python -m venv venv

```

---
#### Activate it

##### Windows PowerShell
```bash
venv\Scripts\activate

```
---

### Install dependencies

```bash
pip install -r requirements.txt

```
---
### Start the FastAPI server
```bash
uvicorn app.main:app --reload

```
---
### The backend will be running at:

```bash
http://127.0.0.1:8000

```
---
