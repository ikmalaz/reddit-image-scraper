import requests
import json
import time
from pathlib import Path

BASE_URL = "https://www.reddit.com/r/bolehland/.json"
HEADERS = {"User-Agent": "Mozilla/5.0 (Reddit Scraper by /u/yourusername)"}
PAGES = 10
DELAY = 2
OUTPUT_FILE = Path("results.json")

def fetch_posts(pages=PAGES, delay=DELAY):
    after = None
    results = []

    for page in range(1, pages + 1):
        url = BASE_URL if after is None else f"{BASE_URL}?after={after}"
        print(f"[{page}/{pages}] Fetching: {url}")

        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            res.raise_for_status()
        except requests.RequestException as e:
            print(f"⚠️ Request failed: {e}")
            break

        try:
            data = res.json()
        except json.JSONDecodeError:
            print("⚠️ Failed to parse JSON")
            break

        children = data.get("data", {}).get("children", [])
        for post in children:
            post_data = post.get("data", {})
            title = post_data.get("title", "Untitled")
            image_url = post_data.get("url_overridden_by_dest", "")

            if image_url.lower().endswith((".jpg", ".png", ".jpeg", ".gif")):
                results.append({"post_title": title, "image_url": image_url})

        after = data.get("data", {}).get("after")
        if not after:
            print("✅ No more pages available.")
            break

        time.sleep(delay)  # be nice to Reddit API

    return results

def save_results(results, filepath=OUTPUT_FILE):
    filepath.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"💾 Saved {len(results)} posts with images to {filepath}")

if __name__ == "__main__":
    posts = fetch_posts()
    if posts:
        save_results(posts)
