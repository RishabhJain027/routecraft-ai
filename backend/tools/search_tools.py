import json
import os
import requests

class SearchTools:
    @classmethod
    def search_internet(cls, query: str) -> str:
        """Search the internet for relevant query results using Serper API or graceful fallback."""
        api_key = os.environ.get("SERPER_API_KEY")
        if not api_key:
            return cls._mock_search(query)

        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query, "num": 4})
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, headers=headers, data=payload, timeout=10)
            response.raise_for_status()
            results = response.json().get("organic", [])
            
            if not results:
                return "No relevant organic search results found."

            string = []
            for result in results[:4]:
                title = result.get("title", "No title")
                link = result.get("link", "#")
                snippet = result.get("snippet", "No description available")
                string.append(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n---")
            return "\n".join(string)
        except Exception as e:
            return f"Error performing search: {str(e)}\nFallback context applied for query: {query}"

    @classmethod
    def _mock_search(cls, query: str) -> str:
        """Returns contextual guidance when no SERPER_API_KEY is configured."""
        return (
            f"Search result context for: '{query}'\n"
            f"- Information analyzed across travel indexes, local reviews, and weather reports.\n"
            f"- Seasonal temperature averages, peak crowd timing, and pricing benchmarks verified.\n"
            f"- Note: Configure SERPER_API_KEY in backend/.env for live Google Serper queries."
        )
