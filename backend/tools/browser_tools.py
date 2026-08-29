import json
import os
import requests
from bs4 import BeautifulSoup

class BrowserTools:
    @classmethod
    def scrape_and_summarize_website(cls, website: str) -> str:
        """Scrapes text content from a website using Browserless or direct HTTP fallback."""
        if not website or website == "#":
            return "No URL provided for scraping."

        browserless_key = os.environ.get("BROWSERLESS_API_KEY")

        try:
            if browserless_key:
                url = f"https://chrome.browserless.io/content?token={browserless_key}"
                payload = json.dumps({"url": website})
                headers = {"cache-control": "no-cache", "content-type": "application/json"}
                response = requests.post(url, headers=headers, data=payload, timeout=15)
                html_content = response.text
            else:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
                response = requests.get(website, headers=headers, timeout=10)
                html_content = response.text

            soup = BeautifulSoup(html_content, "html.parser")
            for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
                tag.extract()

            text = soup.get_text(separator=" ", strip=True)
            # Limit characters to keep concise context
            trimmed_text = text[:2500] if len(text) > 2500 else text
            return f"Summary from {website}:\n{trimmed_text}"
        except Exception as e:
            return f"Note: Unable to scrape live website {website} directly ({str(e)}). Fallback local destination knowledge active."
