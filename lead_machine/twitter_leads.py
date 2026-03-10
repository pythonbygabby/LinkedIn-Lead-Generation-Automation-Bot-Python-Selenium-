import snscrape.modules.twitter as sntwitter
import csv

keywords = [
    "need python automation",
    "looking for python developer",
    "automate excel",
    "need web scraping",
    "hiring python dev"
]

LIMIT = 30

with open("leads.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["source", "name", "username", "context", "link"])

    for keyword in keywords:
        for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(keyword).get_items()
        ):
            if i >= LIMIT:
                break

            writer.writerow([ 
                "twitter",
                tweet.user.displayname,
                tweet.user.username,
                tweet.content[:200],
                tweet.url
            ])

print("✅ Twitter leads collected")
