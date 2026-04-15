# 🎙️ Voice Controlled AI Agent

Built for Mem0 Internship Assignment by Prakash Kumar

---

## 🚀 How I Built This Project — Step by Step

### Step 1 — Project Setup
- Created a folder called voice-agent on Desktop
- Created 4 Python files: app.py, stt.py, intent.py, tools.py
- Created output/ folder where all generated files are saved
- Created .env file to store API key safely

### Step 2 — Got Free API Key
- Went to https://console.groq.com
- Created free account
- Generated API key
- Saved it in .env file

### Step 3 — Built Speech to Text (stt.py)
- Used Groq Whisper Large V3 model
- This file takes audio file as input
- Converts audio to text automatically
- Returns the transcribed text

### Step 4 — Built Intent Detection (intent.py)
- Used LLaMA 3.3 70B model via Groq API
- This file reads the transcribed text
- Understands what user wants to do
- Returns one of 4 intents:
  - create_file
  - write_code
  - summarize
  - general_chat

### Step 5 — Built Tools (tools.py)
- Built 4 tools based on 4 intents
- create_file: Creates new file in output folder
- write_code: Generates Python code and saves it
- summarize: Summarizes given text using AI
- general_chat: Normal conversation with AI

### Step 6 — Built UI (app.py)
- Used Streamlit to build web interface
- Added audio file upload button
- Added Process button
- Shows transcribed text, detected intent, and result
- All output files saved in output/ folder

---

## 🛠️ Tools and Technologies Used

| Tool | Why I Used It |
|------|--------------|
| Python | Main programming language |
| Streamlit | To build web UI easily |
| Groq API | Free and fast AI API |
| Whisper Large V3 | Best speech to text model |
| LLaMA 3.3 70B | Best free intent detection model |
| Python-dotenv | To store API key safely |
| Git + GitHub | To store and share code |

---

## 🤖 How The Agent Works

User uploads audio file
↓
Groq Whisper converts audio to text
↓
LLaMA 3.3 70B reads text and detects intent
↓
Based on intent, tool is executed
↓
Result shown in Streamlit UI

---

## 💡 Example

User says in audio:Write a Python code for calculator

Agent does:

Step 1: Audio → "Write a Python code for calculator"
Step 2: Intent detected → write_code
Step 3: Python code generated automatically
Step 4: Code saved in output/generated_code.py
Step 5: Result shown in UI

---

## 🎯 Supported Intents

| Intent | What It Does |
|--------|-------------|
| create_file | Creates a new empty file |
| write_code | Generates Python code and saves |
| summarize | Summarizes the given text |
| general_chat | Normal AI conversation |

---

## 📁 Project Structure

voice-agent/
├── app.py        → Main Streamlit UI
├── stt.py        → Audio to Text conversion
├── intent.py     → Intent Detection
├── tools.py      → Tool Execution
├── output/       → All generated files
├── .env          → API Key (not uploaded)
├── .gitignore    → Git ignore
└── README.md     → This file

---

## ⚙️ How to Run

### 1. Clone repo

git clone https://github.com/prakashkumarmahato807/voice-agent.git
cd voice-agent

### 2. Install libraries
pip install streamlit groq python-dotenv pydub

### 3. Add API Key
Create .env file and add:

GROQ_API_KEY=your_key_here

### 4. Run app

streamlit run app.py

### 5. Open browser

http://localhost:8501

---

## ⚠️ Problems I Faced and How I Fixed Them

### Problem 1 — Model Stopped Working
- llama3-8b-8192 model was decommissioned
- Fixed by using llama-3.3-70b-versatile

### Problem 2 — Python Not Recognized
- python command not working on Windows
- Fixed by using py -m pip install

### Problem 3 — GitHub Push Failed
- Permission denied error
- Fixed by using Personal Access Token

---

## 🔑 Why I Used Cloud API

I used Groq Cloud API instead of local models because:
- Local Whisper needs GPU
- Local LLaMA needs high RAM
- Groq API is completely free
- Groq API is very fast





