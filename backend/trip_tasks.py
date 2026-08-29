try:
    from crewai import Task
    CREWAI_AVAILABLE = True
except ImportError:
    CREWAI_AVAILABLE = False
    Task = None

class TripTasks:
    def identify_task(self, agent, origin, cities, interests, date_range):
        """Task 1: Analyze all candidate cities and select the single best match."""
        description = (
            f"Analyze and compare the following candidate cities: {', '.join(cities) if isinstance(cities, list) else cities}.\n"
            f"Travel Origin: {origin}\n"
            f"Travel Dates: {date_range}\n"
            f"Traveler Interests: {interests}\n\n"
            f"Evaluate current weather forecasts, flight prices from {origin}, seasonal timing, attractions, and how well each city matches '{interests}'.\n"
            f"Deliver a clear decision picking the #1 best destination city with detailed justification, fit score out of 100, and pros/cons comparison for each candidate."
        )
        expected_output = "Detailed comparative report selecting the best destination city with scoring and rationale."
        if CREWAI_AVAILABLE and Task:
            return Task(description=description, expected_output=expected_output, agent=agent)
        return {"name": "identify_task", "description": description, "expected_output": expected_output}

    def gather_task(self, agent, selected_city, origin, interests, date_range):
        """Task 2: Deep dive into local culture, hidden spots, food scene, and seasonal customs."""
        description = (
            f"Perform an in-depth local investigation of {selected_city} for a trip during {date_range}.\n"
            f"Origin: {origin}\n"
            f"Interests: {interests}\n\n"
            f"Identify:\n"
            f"1. Key cultural hotspots, iconic landmarks, and lesser-known local gems.\n"
            f"2. Neighborhood-by-neighborhood breakdown and walkable routes.\n"
            f"3. Must-try authentic dishes, specialty coffee spots, markets, and izakayas/bistros.\n"
            f"4. Practical local customs, transport pass tips (metro cards, bullet trains, transit apps), and weather preparations."
        )
        expected_output = "Comprehensive local guide with hidden gems, neighborhood highlights, and cultural tips."
        if CREWAI_AVAILABLE and Task:
            return Task(description=description, expected_output=expected_output, agent=agent)
        return {"name": "gather_task", "description": description, "expected_output": expected_output}

    def plan_task(self, agent, selected_city, origin, interests, date_range):
        """Task 3: Build the complete 7-day chapter itinerary, budget breakdown, and packing list."""
        description = (
            f"Craft a master 7-day travel itinerary for {selected_city} from {date_range} originating in {origin} for a traveler into '{interests}'.\n\n"
            f"Requirements:\n"
            f"1. Detailed day-by-day itinerary (Day 1 through Day 7) divided into Morning, Afternoon, Evening, Dinner/Food recommendation, and Stay/Hotel suggestion.\n"
            f"2. Precise budget breakdown: Flights, Accommodations, Dining, Activities/Attractions, Local Transit, and Contingency.\n"
            f"3. Essential packing checklist tailored to {selected_city}'s climate during {date_range}.\n"
            f"4. Verified research trail with source citations and agent attribution."
        )
        expected_output = "Complete 7-day travel master plan with daily schedules, budget, packing list, and research trail."
        if CREWAI_AVAILABLE and Task:
            return Task(description=description, expected_output=expected_output, agent=agent)
        return {"name": "plan_task", "description": description, "expected_output": expected_output}
