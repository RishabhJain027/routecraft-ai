import os
from tools.search_tools import SearchTools
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools

try:
    from crewai import Agent
    CREWAI_AVAILABLE = True
except ImportError:
    CREWAI_AVAILABLE = False
    Agent = None

class TripAgents:
    def city_selection_agent(self):
        """Scout Agent: Analyzes and selects the best destination based on weather, costs, and interests."""
        if CREWAI_AVAILABLE:
            return Agent(
                role="City Selection Expert",
                goal="Select the best city based on weather, season, flight prices, and traveler interests",
                backstory=(
                    "An expert travel analyst who rigorously compares multiple destination candidates "
                    "using up-to-date weather data, seasonal timing, airfare benchmarks, and user preferences."
                ),
                tools=[
                    SearchTools.search_internet,
                    BrowserTools.scrape_and_summarize_website,
                ],
                verbose=True,
            )
        return {
            "name": "Scout",
            "role": "City Selection Expert",
            "goal": "Select the best city based on weather, season, flight prices, and traveler interests",
            "description": "Compares candidate destinations using weather, seasonal signals, and flight price estimates."
        }

    def local_expert(self):
        """Local Agent: Provides rich cultural, neighborhood, food, and hidden-gem insights."""
        if CREWAI_AVAILABLE:
            return Agent(
                role="Local Expert at this City",
                goal="Provide the strongest local insights, hidden gems, and cultural hotspots for the selected city",
                backstory=(
                    "A passionate local resident and travel curator with encyclopedic knowledge of neighborhoods, "
                    "secret viewpoints, local customs, street food stalls, and authentic experiences."
                ),
                tools=[
                    SearchTools.search_internet,
                    BrowserTools.scrape_and_summarize_website,
                ],
                verbose=True,
            )
        return {
            "name": "Local",
            "role": "Local Expert",
            "goal": "Provide authentic local secrets, customs, and neighborhood highlights",
            "description": "Surfaces attractions, customs, daily activities, hidden gems, and cultural hotspots."
        }

    def travel_concierge(self):
        """Concierge Agent: Assembles the complete 7-day schedule, budget breakdown, packing, and logistics."""
        if CREWAI_AVAILABLE:
            return Agent(
                role="Amazing Travel Concierge",
                goal="Create a detailed seven-day itinerary with exact schedules, restaurant recommendations, hotels, packing lists, and budget calculations",
                backstory=(
                    "A world-class luxury and budget travel concierge who crafts seamless, realistic day-by-day "
                    "itineraries balancing timing, transport logistics, dining, accommodations, and exact budgets."
                ),
                tools=[
                    SearchTools.search_internet,
                    BrowserTools.scrape_and_summarize_website,
                    CalculatorTools.calculate,
                ],
                verbose=True,
            )
        return {
            "name": "Concierge",
            "role": "Travel Concierge",
            "goal": "Assemble the full 7-day itinerary, budget breakdown, and packing guidance",
            "description": "Turns research into a complete 7-day plan with dining, hotels, packing list, and budget."
        }
