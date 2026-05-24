# LunarLegion, AI-Powered Study App

An interactive learning platform built with **Streamlit** and Python. LunarLegion gives you four modes to actually learn and test yourself: Practise, Quiz, Exam, and Chat with AI. The sidebar navigation keeps it clean and simple.

This was my first real attempt at building a full AI-integrated study tool from scratch. I wanted something that felt like an actual study partner, not just flashcards.

Building the tool you wish existed is birarenze and honestly one of the best reasons to code.

---

## Features

| Mode | Description |
|------|-------------|
| **Practise** | Guided practice problems with instant feedback |
| **Quiz** | Timed quiz mode to test your knowledge |
| **Exam** | Full exam simulation |
| **Chat with AI** | Conversational AI assistant for questions and explanations |

All four modes are accessible via a radio button sidebar, switch between them instantly.

---

## Project Structure

```
LunarLegion/
├── LunarLegion-main/
│   ├── main.py          # Entry point, Streamlit app with sidebar nav
│   ├── app.py           # Exam mode
│   ├── chatbot.py       # AI chat interface
│   ├── practise.py      # Practice mode
│   ├── quiz.py          # Quiz mode
│   └── requirements.txt # Dependencies
└── streamlit/           # Streamlit config/assets
```

---

## Tech Stack
- **Framework:** Streamlit
- **Language:** Python 3
- **AI Integration:** Chatbot module (LLM-backed)

---

## Running It

```bash
pip install -r LunarLegion-main/requirements.txt
streamlit run LunarLegion-main/main.py
```

The app opens in your browser at `http://localhost:8501`.

---

## Background
LunarLegion started as an experiment: could I build a study app that actually engaged me more than just re-reading notes? The AI chat mode was the most exciting part to build, being able to ask questions in natural language and get real explanations is a different kind of studying. This project proved to me early on that AI + education is where I wanted to spend my energy.
