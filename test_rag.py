from src.rag_pipeline import RAGPipeline

rag = RAGPipeline()

rag.create_vectorstore()

results = rag.retrieve_context(
    "Why am I getting 401 Unauthorized?"
)

print(results)