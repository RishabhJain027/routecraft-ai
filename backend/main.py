from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import List, Optional
import os
from crew_runner import RouteCraftRunner

app = FastAPI(
    title="RouteCraft AI API",
    description="Multi-Agent AI Travel Planning & Itinerary Synthesis Engine",
    version="2.0.0"
)

# CORS middleware allowing frontend connectivity from any local origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

runner = RouteCraftRunner()

class PlanRequest(BaseModel):
    origin: str = Field(..., example="New Delhi")
    cities: List[str] = Field(..., example=["Tokyo", "Seoul", "Bangkok"])
    date_range: str = Field(..., example="Oct 10–16, 2026")
    interests: str = Field(..., example="Food, anime, culture, hidden gems")
    currency: Optional[str] = Field(default="INR", example="INR")
    custom_api_key: Optional[str] = Field(default=None, example="gsk_...")

@app.get("/api/health")
def health():
    has_groq = bool(os.environ.get("GROQ_API_KEY"))
    return {
        "status": "healthy",
        "service": "RouteCraft AI API",
        "version": "2.0.0",
        "ai_engine": "Groq Llama-3.3-70B Multi-Agent" if has_groq else "Contextual Engine",
        "has_groq_key": has_groq,
        "has_openai_key": bool(os.environ.get("OPENAI_API_KEY")),
        "has_serper_key": bool(os.environ.get("SERPER_API_KEY")),
        "has_browserless_key": bool(os.environ.get("BROWSERLESS_API_KEY")),
    }

@app.get("/api/presets")
def get_presets():
    """Return pre-configured inspiring travel scenarios for instant demo."""
    return [
        {
            "id": "tokyo-anime",
            "title": "🌸 Tokyo: Anime & Food Odyssey",
            "origin": "New Delhi",
            "cities": ["Tokyo", "Seoul", "Bangkok"],
            "date_range": "Oct 10–16, 2026",
            "interests": "Street food, anime culture, neighborhood walks, vintage shopping, shrine visits"
        },
        {
            "id": "euro-heritage",
            "title": "🏛️ European Grand Heritage",
            "origin": "London",
            "cities": ["Rome", "Paris", "Barcelona"],
            "date_range": "Nov 5–12, 2026",
            "interests": "Renaissance art, historic architecture, wine tasting, cobblestone plazas, artisanal bakeries"
        },
        {
            "id": "bali-tropical",
            "title": "🌴 Tropical Bali & Spiritual Retreat",
            "origin": "Singapore",
            "cities": ["Bali", "Phuket", "Langkawi"],
            "date_range": "Dec 1–7, 2026",
            "interests": "Emerald rice terraces, wellness yoga, surf breaks, waterfall hikes, sunset beach clubs"
        },
        {
            "id": "korea-kculture",
            "title": "🥢 Seoul: K-Culture & Night Markets",
            "origin": "Mumbai",
            "cities": ["Seoul", "Tokyo", "Taipei"],
            "date_range": "Sep 15–22, 2026",
            "interests": "K-pop landmarks, palace photo walks, Hanok villages, BBQ alleys, indie cafe hopping"
        }
    ]

@app.post("/api/plan")
def create_plan(req: PlanRequest):
    """Orchestrates Scout, Local, and Concierge agents using Groq to deliver a comprehensive trip plan."""
    try:
        plan_result = runner.run_plan(
            origin=req.origin,
            cities=req.cities,
            date_range=req.date_range,
            interests=req.interests,
            custom_api_key=req.custom_api_key
        )
        return plan_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Planning pipeline failed: {str(e)}")

# Mount static frontend files if directory exists
frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
