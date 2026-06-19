from src.classifier import classify_persona

result = classify_persona(
    "Our API is returning a 401 Unauthorized error."
)

print(result)