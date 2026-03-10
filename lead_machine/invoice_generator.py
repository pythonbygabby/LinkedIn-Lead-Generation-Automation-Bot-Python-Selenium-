from datetime import date

def generate_invoice(client, service, price):
    today = date.today()
    return f"""
INVOICE

Client: {client}
Service: {service}
Amount Due: ${price}
Date: {today}

Payment Methods:
- PayPal
- Wise
- Bank Transfer

Payment due upon delivery.

Thank you,
Gabriel
"""

if __name__ == "__main__":
    print(generate_invoice(
        "John Doe",
        "Excel Automation Script",
        250
    ))
