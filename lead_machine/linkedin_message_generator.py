import csv

def generate_message(name, context):
    return f"""Hi {name},

I came across your profile and noticed you deal with {context}.
I help businesses remove repetitive work using small Python automations
(CSVs, Excel, reports, data cleanup).

If this is relevant, happy to suggest a simple solution.

Best,
Gabriel
"""

with open("linkedin_leads.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("-----")
        print(generate_message(row["name"], row["context"]))
