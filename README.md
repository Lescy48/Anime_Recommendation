# 🎌 Anime Recommendation Expert System (Sistem Pakar)

A rule-based **expert system** (sistem pakar) for recommending anime based on user preferences. Built with Python and Flask, using a forward-chaining inference engine.

## Features

- **Knowledge Base** — 25+ popular anime with attributes (genre, mood, type, episodes, era)
- **Inference Engine** — Forward-chaining rule engine that matches user preferences to anime
- **Step-by-step Quiz** — 5-question questionnaire to capture user preferences
- **Ranked Results** — Top 8 recommendations with match scores and reasoning

## How It Works

The expert system follows three components:

1. **Knowledge Base** (`knowledge_base.py`) — Contains the anime database and inference rules
2. **Inference Engine** (`inference_engine.py`) — Applies forward-chaining rules to score anime
3. **Web UI** (`app.py` + `templates/`) — Flask web application with the questionnaire

The system asks users about:
- Preferred genre (action, romance, fantasy, mystery, etc.)
- Preferred mood (dark, light, mixed)
- Format preference (TV series vs. movie)
- Episode length (short, medium, long)
- Era preference (classic, modern, recent)

Each answer triggers rules in the inference engine that add weighted scores to anime candidates. The top-scoring anime are presented as recommendations with explanations.

## Installation

```bash
pip install -r requirements.txt
```

## Running the App

```bash
python app.py
```

Then open <http://localhost:5000> in your browser.

## Project Structure

```
├── app.py               # Flask web application
├── knowledge_base.py    # Anime data + inference rules + questions
├── inference_engine.py  # Forward-chaining inference engine
├── templates/
│   ├── index.html       # Home / landing page
│   ├── quiz.html        # Step-by-step questionnaire
│   └── results.html     # Recommendation results page
└── requirements.txt
```