from src.generator import generate_response

response = generate_response(
    question="Why am I getting 401 Unauthorized?",
    context="""
401 Unauthorized Error

Cause:
The API token is invalid, expired, or missing.

Resolution:
Verify API token.
Generate a new token.
""",
    persona="Technical Expert"
)

print(response)