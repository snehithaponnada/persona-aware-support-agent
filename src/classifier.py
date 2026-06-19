import os
import json


from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def classify_persona(user_message):

    system_prompt = """
You are a customer persona classifier.

Classify the user into ONLY ONE category:

1. Technical Expert
2. Frustrated User
3. Business Executive

Return JSON format:

{
    "persona": "...",
    "confidence": 0.0,
    "reasoning": "..."
}
"""

    response_schema = {
        "type": "OBJECT",
        "properties": {
            "persona": {
                "type": "STRING"
            },
            "confidence": {
                "type": "NUMBER"
            },
            "reasoning": {
                "type": "STRING"
            }
        }
    }

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            response_mime_type="application/json",
            response_schema=response_schema,
            temperature=0.1
        )
    )

    return json.loads(response.text)