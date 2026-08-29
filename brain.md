# RouteCraft AI — Brain File

## 1. Source Repository & Lineage
- Upstream: https://github.com/crewAIInc/crewAI-examples
- Example path: `crews/trip_planner`
- Pinned snapshot: `da94a91e691e1cf5b3151416bb15b5b62729bea8`
- License stated by upstream README: MIT
- Purpose: demonstrate CrewAI agents collaborating to choose a destination and generate a detailed trip itinerary.
- Project Brand Name: **RouteCraft AI**

## 2. What the Original Example Does

The application collects four inputs:
1. Origin
2. Candidate cities
3. Trip date range
4. Traveler interests

It constructs a `TripCrew`, creates three agents, creates three tasks, then executes them through a CrewAI `Crew`.

Execution flow:
User inputs -> City Selection (Scout) -> Local Expert (Local) -> Travel Concierge (Concierge) -> Final trip plan.

## 3. Agents

### 1. City Selection Expert (Scout)
Goal: Select the best city using weather, season, flight prices, and traveler interests.
Tools:
- internet search (`SearchTools`)
- website scraping/summarization (`BrowserTools`)

Expected role:
Compare candidate destinations using current conditions, seasonal events, attractions, and travel costs.

### 2. Local Expert at this City (Local)
Goal: Provide the strongest local insight for the selected city.
Tools:
- internet search (`SearchTools`)
- website scraping/summarization (`BrowserTools`)

Expected role:
Surface attractions, customs, events, daily activities, hidden gems, cultural hotspots, weather, and practical costs.

### 3. Amazing Travel Concierge (Concierge)
Goal: Create the travel itinerary, budget, and packing suggestions.
Tools:
- internet search (`SearchTools`)
- website scraping/summarization (`BrowserTools`)
- calculator (`CalculatorTools`)

Expected role:
Turn research into a full seven-day plan with actual places, hotels, restaurants, weather expectations, packing guidance, and a detailed budget.

## 4. Tasks

### identify_task
Inputs:
- origin
- candidate cities
- interests
- date range

Produces:
- selected city
- flight costs
- weather forecast
- attractions
- detailed destination-selection report

### gather_task
Inputs:
- origin
- interests
- date range

Produces:
- comprehensive city guide
- local customs
- hidden gems
- cultural hotspots
- practical tips
- forecast and cost context

### plan_task
Inputs:
- origin
- interests
- date range

Produces:
- seven-day itinerary
- daily schedule
- weather
- places to eat
- actual hotels
- packing suggestions
- budget breakdown
- reasons for recommendations
- markdown final plan

## 5. Tools

### SearchTools
Uses Serper's Google-search-compatible endpoint:
`https://google.serper.dev/search`

Environment variable:
`SERPER_API_KEY`

Returns up to four organic results with:
- title
- link
- snippet

Fallback: Graceful search context synthesis if no API key is set.

### BrowserTools
Uses Browserless or BeautifulSoup HTTP parsing:
`https://chrome.browserless.io/content?token=...`

Environment variable:
`BROWSERLESS_API_KEY`

It retrieves website content, parses HTML, chunks large pages, and extracts clean text.

### CalculatorTools
Performs safe arithmetic by parsing an expression with Python AST.
Allowed operators include:
- +
- -
- *
- /
- **
- %
- unary +/-

The tool rejects unexpected characters/operators.

## 6. Runtime Environment

Configuration options:
- `SERPER_API_KEY`
- `BROWSERLESS_API_KEY`
- `OPENAI_API_KEY`

Modernization note:
Secret keys are stored server-side in `.env` or client session storage, never exposed in client bundles.

## 7. Project Structure

```
trip-planner-ai/
├── README.md                 # Complete documentation & run guide
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

## 8. Enhanced Product Direction

### Product name
**RouteCraft AI**

### UX concept
A functional dashboard with an illustrated notebook/sketch aesthetic:
- light parchment/notebook background
- hand-drawn borders & subtle paper drop shadows
- casual handwritten headings (`Caveat`, `DM Sans`)
- muted blue, grey, yellow, green tones
- bright accent states for selected metrics
- pencil/marker hover effects
- slight wobble/draw-in animations
- irregular but intentional card alignment
- clear hierarchy similar to a productivity dashboard

### Main features
1. Dashboard / trip brief with inspiration presets
2. Live Multi-Agent activity lane (Scout, Local, Concierge)
3. Candidate destination comparison matrix & scoring
4. 7-Day Chapter Itinerary with morning/afternoon/evening slots
5. Where the numbers go (Budget breakdown & currency selector: ₹, $, €, £, ¥)
6. Packing checklist with interactive toggle
7. Research Trail & source attribution
8. Export options (Print / PDF, Markdown, JSON)
9. Settings modal for API configuration

## 9. API Endpoints

- `GET /api/health` — API status and available key indicators.
- `GET /api/presets` — Pre-configured travel scenarios.
- `POST /api/plan` — Multi-agent plan execution.

Request shape:
```json
{
  "origin": "New Delhi",
  "cities": ["Tokyo", "Seoul", "Bangkok"],
  "date_range": "Oct 10–16, 2026",
  "interests": "Street food, anime culture, neighborhood walks",
  "currency": "INR"
}
```

Response shape:
```json
{
  "website_name": "RouteCraft AI",
  "selected_city": "Tokyo",
  "score": 94,
  "summary": "...",
  "weather": "...",
  "comparison": [],
  "agents": [],
  "itinerary": [],
  "budget": {},
  "packing_checklist": [],
  "sources": []
}
```
