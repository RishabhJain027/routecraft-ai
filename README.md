# 🗺️ RouteCraft AI — Multi-Agent Travel Planner

> **A tiny travel crew in your notebook ✦**  
> An AI-powered travel planning platform powered by multi-agent collaboration (Scout, Local, and Concierge) with a sketch/notebook-style dashboard.

---

## 🌟 Key Features

- **Multi-Agent AI Collaboration**:
  - 🔭 **Scout (City Selection Expert)**: Analyzes weather, flight prices, seasonality, and interests to pick the best city among candidates.
  - 🧭 **Local (Local Guide & Secrets)**: Unearths cultural landmarks, neighborhood walks, street food stalls, and secret viewpoints.
  - 🧳 **Concierge (Travel Concierge)**: Crafts a 7-day day-by-day itinerary, categorized budget breakdowns, and climate-tailored packing checklists.
- **Notebook / Sketch Aesthetic**: Warm parchment backgrounds, hand-drawn cards, Caveat handwritten accents, stamp badges, and marker highlights.
- **Dynamic Inspiration Presets**: One-click travel ideas (Tokyo Anime, European Heritage, Tropical Bali, Seoul K-Culture).
- **Candidate Comparison Matrix**: Clear scoring, pros/cons, and flight estimates across all considered cities.
- **Interactive 7-Day Itinerary**: Morning, afternoon, and evening timelines with dining suggestions and boutique stays.
- **Budget Breakdown & Currency Switcher**: Switch between **₹ INR**, **$ USD**, **€ EUR**, **£ GBP**, and **¥ JPY**.
- **Interactive Packing Checklist**: Check off essential travel gear and documents as you prepare.
- **Verified Research Trail**: Cites real research sources attributed to each agent.
- **Export & Sharing**: One-click Print/PDF save, Markdown itinerary download, and JSON data export.
- **Zero-Config Demo Mode**: Works out-of-the-box with rich contextual trip generation even without paid API keys!

---

## 🚀 Quick Start Guide

### 1. Run the Frontend (Static)

You can open `frontend/index.html` directly in your browser, or start a local static server:

```bash
cd frontend
python -m http.server 5173
```

Then navigate to: `http://localhost:5173`

---

### 2. Run the Full Backend API

The backend uses **FastAPI** with optional **CrewAI** integration.

1. **Navigate to the backend directory and install dependencies**:
   ```bash
   cd backend
   python -m pip install -r requirements.txt
   ```

2. **(Optional) Configure API Keys**:
   Copy `.env.example` to `.env` and provide your keys:
   ```bash
   cp .env.example .env
   ```
   - `OPENAI_API_KEY`: Enables live GPT-4 / GPT-4o CrewAI agents.
   - `SERPER_API_KEY`: Enables live Google Serper search queries.
   - `BROWSERLESS_API_KEY`: Enables cloud web scraping.

   *(If no keys are provided, RouteCraft AI automatically runs in its intelligent Contextual Engine mode!)*

3. **Start the FastAPI server**:
   ```bash
   python -m uvicorn main:app --reload --port 8000
   ```

4. **Access RouteCraft AI**:
   - **Frontend Web UI**: `http://localhost:8000`
   - **Interactive API Docs (Swagger)**: `http://localhost:8000/docs`
   - **API Health Endpoint**: `http://localhost:8000/api/health`

---

## 🏗️ Architecture Overview

```
trip-planner-ai/
├── README.md                 # Project documentation & run guide
├── brain.md                  # System architecture and agent specifications
├── backend/
│   ├── main.py               # FastAPI backend with REST endpoints & static server
│   ├── crew_runner.py        # Multi-agent orchestrator & contextual trip engine
│   ├── trip_agents.py        # CrewAI 3-agent definitions (Scout, Local, Concierge)
│   ├── trip_tasks.py         # CrewAI 3-task definitions
│   ├── requirements.txt      # Python dependencies
│   ├── .env.example          # Environment variables template
│   └── tools/
│       ├── __init__.py
│       ├── search_tools.py   # Serper Google Search tool
│       ├── browser_tools.py  # Browserless / BS4 scraping tool
│       └── calculator_tools.py # AST-based safe calculator
└── frontend/
    ├── index.html            # Sketch/notebook responsive dashboard
    ├── style.css             # Illustrated notebook CSS with Caveat typography
    └── app.js                # Dynamic UI logic, currency conversion & presets
```

---

## 📡 API Reference

### `POST /api/plan`
Generates a comprehensive 7-day multi-agent trip plan.

**Request Body**:
```json
{
  "origin": "New Delhi",
  "cities": ["Tokyo", "Seoul", "Bangkok"],
  "date_range": "Oct 10–16, 2026",
  "interests": "Street food, anime culture, neighborhood walks, vintage shopping",
  "currency": "INR"
}
```

### `GET /api/presets`
Returns inspiring preset travel scenarios.

### `GET /api/health`
Returns backend health and API key configuration status.

---

## 📜 License
MIT
