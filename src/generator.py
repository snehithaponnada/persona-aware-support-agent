from google import genai
import os

from dotenv import load_dotenv


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_response(
    question,
    context,
    persona
):

    prompt = f"""
You are a customer support assistant.

Persona: {persona}

Answer according to the persona style.

Question:
{question}

Retrieved Context:
{context}

Instructions:

Technical Expert:
- Detailed technical explanation
- Mention HTTP codes, APIs, configurations

Frustrated User:
- Empathetic tone
- Simple language
- Reassuring

Business Executive:
- Short and concise
- Focus on business impact
- Focus on resolution

Generate only the answer.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text