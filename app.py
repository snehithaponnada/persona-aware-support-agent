from src.classifier import classify_persona
from src.rag_pipeline import RAGPipeline
from src.generator import generate_response
from src.escalator import should_escalate


def main():

    question = input("Ask your question: ")

    if should_escalate(question):

        print("\nESCALATION REQUIRED")
        print("Please connect user with human support.")

        return

    persona_result = classify_persona(question)

    persona = persona_result["persona"]

    rag = RAGPipeline()

    rag.create_vectorstore()

    context = rag.retrieve_context(question)

    response = generate_response(
        question=question,
        context=context,
        persona=persona
    )

    print("\nPERSONA:")
    print(persona)

    print("\nRESPONSE:")
    print(response)


if __name__ == "__main__":
    main()