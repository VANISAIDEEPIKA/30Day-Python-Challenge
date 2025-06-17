import requests
from bs4 import BeautifulSoup

# 🌐 Target news site (you can change this to another one)
url = "https://news.ycombinator.com"

print(f"📡 Connecting to: {url}")
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise error for non-200 responses

    # 🍜 Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 🎯 Extract headline links (tag: <a> with class "storylink" or "titlelink")
    headlines = soup.select(".titleline > a")

    print("\n📰 Top Headlines:\n" + "-"*40)
    for idx, headline in enumerate(headlines[:10], start=1):  # Top 10 headlines
        print(f"{idx}. {headline.text.strip()}")
        print(f"   🔗 {headline['href']}\n")

except requests.exceptions.RequestException as e:
    print(f"❌ Failed to connect.\n📛 Error: {e}")
