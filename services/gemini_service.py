import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing in .env")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=30000)
)


def analyze_customer_message(message):

    prompt = f"""
Analyze this customer support message.

Category must be exactly one:
Complaint
Refund/Return
Sales Inquiry
Delivery Question
Account/Technical Issue
General Query
Spam

Sentiment must be exactly one:
Positive
Neutral
Negative

Generate a short professional customer support auto-reply.

Customer message:
{message}

Return ONLY valid JSON:

{{
    "category": "category name",
    "sentiment": "sentiment name",
    "auto_reply": "professional reply"
}}
"""

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    result = interaction.output_text.strip()

    return json.loads(result)