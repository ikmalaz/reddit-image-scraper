import requests
import json
import time

BASE_URL = "https://www.reddit.com/r/bolehland/.json"
HEADERS = {"User-Agent": "Mozilla/5.0"}
AFTER = None
results = []

# Scrape ~10 pages
for _ in range(10):
    url = BASE_URL if AFTER is None else f"{BASE_URL}?after={AFTER}"
    print(f"Fetching: {url}")
    res = requests.get(url, headers=HEADERS)
    data = res.json()

    for post in data["data"]["children"]:
        post_data = post["data"]
        title = post_data["title"]
        image_url = post_data.get("url_overridden_by_dest")

        # keep only posts with image
        if image_url and (image_url.endswith(".jpg") or image_url.endswith(".png")):
            results.append({
                "post_title": title,
                "image_url": image_url
            })

    AFTER = data["data"].get("after")
    if not AFTER:
        break

    time.sleep(2)  # be nice to Reddit API

# Save results
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Saved {len(results)} posts with images to results.json")
