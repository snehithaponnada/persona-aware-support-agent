import os

from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

from langchain_huggingface import HuggingFaceEmbeddings


class RAGPipeline:

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vectorstore = None

    def load_documents(self):

        documents = []

        data_folder = "data"

        for file in os.listdir(data_folder):

            file_path = os.path.join(data_folder, file)

            if file.endswith(".txt"):

                loader = TextLoader(
                    file_path,
                    encoding="utf-8"
                )

                documents.extend(
                    loader.load()
                )

            elif file.endswith(".md"):

                loader = TextLoader(
                    file_path,
                    encoding="utf-8"
                )

                documents.extend(
                    loader.load()
                )

            elif file.endswith(".pdf"):

                loader = PyPDFLoader(
                    file_path
                )

                documents.extend(
                    loader.load()
                )

        return documents

    def create_vectorstore(self):

        documents = self.load_documents()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=40
        )

        chunks = splitter.split_documents(
            documents
        )

        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory="chroma_db"
        )

        return self.vectorstore

    def retrieve_context(
        self,
        query,
        top_k=3
    ):

        results = self.vectorstore.similarity_search_with_score(
            query,
            k=top_k
        )

        retrieved_chunks = []

        for doc, score in results:

            retrieved_chunks.append(
                {
                    "text": doc.page_content,
                    "source": doc.metadata.get(
                        "source",
                        "Unknown"
                    ),
                    "score": round(
                        1 / (1 + score),
                        2
                    )
                }
            )

        return retrieved_chunks