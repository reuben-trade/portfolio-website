import chromadb
from chromadb.config import Settings as ChromaSettings
from typing import List, Dict
from ..config import settings
from .embeddings import embedding_service


class RAGService:
    def __init__(self):
        self.client = chromadb.Client(ChromaSettings(
            persist_directory=settings.chroma_persist_directory,
            anonymized_telemetry=False
        ))
        self.collection = self.client.get_or_create_collection(
            name="portfolio_content",
            metadata={"description": "Portfolio content for RAG"}
        )

    def add_documents(self, documents: List[str], metadatas: List[Dict], ids: List[str]):
        """
        Add documents to the vector store
        TODO: Add batch processing and duplicate detection
        """
        embeddings = embedding_service.generate_embeddings(documents)
        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

    def query(self, query_text: str, n_results: int = 5) -> Dict:
        """
        Query the vector store for relevant documents
        TODO: Add reranking and filtering
        """
        query_embedding = embedding_service.generate_embedding(query_text)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results

    def delete_collection(self):
        """Delete the collection (for testing/reset)"""
        self.client.delete_collection(name="portfolio_content")


rag_service = RAGService()
