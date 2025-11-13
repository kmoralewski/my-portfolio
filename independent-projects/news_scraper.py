from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import csv
import requests
import os
import time

# ===== Discord Config =====
DISCORD_TOKEN = "YOUR DISCORD TOKEN"
CHANNEL_ID = "YOUR CHANNEL ID"

def send_to_discord(token, channel_id, message):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    payload = {"content": message}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code in (200, 204):
        print(f"✅ Sent to Discord: {message[:40]}...")
    else:
        print(f"❌ Failed to send: {response.status_code} - {response.text}")

def load_existing_tweets(output_file):
    existing = set()
    if os.path.exists(output_file):
        with open(output_file, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing.add((row["Time"], row["Tweet"]))
    return existing

def init_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1200,900")
    options.add_argument("--disable-dev-shm-usage")
    # You can comment this out if you want to see the browser
    # options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_tweets_from_deltaone(driver, limit=10, output_file="tweets.csv"):
    existing_tweets = load_existing_tweets(output_file)

    driver.refresh()
    time.sleep(5)

    tweets = []
    articles = driver.find_elements(By.CSS_SELECTOR, "article")

    for article in articles[:limit]:
        try:
            spans = article.find_elements(By.XPATH, './/div[@data-testid="tweetText"]//span')
            tweet = " ".join(span.text for span in spans).strip()

            if article.find_elements(By.XPATH, './/span[text()="Show more"]'):
                tweet += " [SHOW MORE]"

            time_elem = article.find_element(By.XPATH, ".//time")
            raw_timestamp = time_elem.get_attribute("datetime")
            dt = datetime.fromisoformat(raw_timestamp.replace("Z", "+00:00")) - timedelta(hours=4)
            fixed_timestamp = dt.strftime("%Y-%m-%dT%H:%M:%S") + "Z"

            tweet_key = (fixed_timestamp, tweet)
            if tweet_key in existing_tweets:
                continue

            tweets.append({"Time": fixed_timestamp, "Tweet": tweet})
        except Exception as e:
            print(f"Error reading tweet: {e}")

    if not tweets:
        print("🕵️ No new tweets found.")
        return

    # Write to CSV
    tweets.sort(key=lambda x: x["Time"])
    write_header = not os.path.exists(output_file)
    with open(output_file, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Time", "Tweet"])
        if write_header:
            writer.writeheader()
        writer.writerows(tweets)

    for tweet in tweets:
        print(f"\n🟢 {tweet['Time']} - {tweet['Tweet']}")
        msg = f"**{tweet['Time']}**\n{tweet['Tweet']}"
        send_to_discord(DISCORD_TOKEN, CHANNEL_ID, msg)
        time.sleep(2)

    print(f"✅ Cycle complete. {len(tweets)} new tweets processed.\n")

if __name__ == "__main__":
    driver = init_driver()
    driver.get("https://x.com/")

    input("🔐 Log in manually, then press Enter to start scraping...")

    while True:
        scrape_tweets_from_deltaone(driver)
        print("⏳ Waiting 5 minutes for next refresh...\n")
        time.sleep(300)
