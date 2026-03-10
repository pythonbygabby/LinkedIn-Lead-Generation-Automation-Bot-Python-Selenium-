def generate_proposal(name, problem, price):
    return f"""
Hi {name},

Thanks for getting back to me.

Based on what you described ({problem}), I can build a small Python automation that will:
- Remove repetitive manual work
- Reduce errors
- Save you several hours per week

✅ What I’ll deliver:
- A clean Python script
- Setup instructions
- One round of revisions

💰 Price: ${price} (one-time)
⏱ Delivery: 2–3 days

If this works for you, I can get started immediately.

Best,
Gabriel
"""

# Example usage
if __name__ == "__main__":
    print(generate_proposal(
        name="John",
        problem="manual Excel reporting",
        price=250
    ))
