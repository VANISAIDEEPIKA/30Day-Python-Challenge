import requests

# 🌐 URL to fetch
url = "https://example.com"

print(f"📡 Fetching content from: {url}")

try:
    # Send GET request
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors

    # ✅ Success
    print("\n✅ Page content fetched successfully!\n")
    print("-" * 50)
    print(response.text)  # Display the full HTML content
    print("-" * 50)

except requests.exceptions.RequestException as e:
    # ❌ Error handling
    print(f"❌ Failed to fetch the webpage.\n📛 Error: {e}")
