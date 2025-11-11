"""
RAG (Retrieval Augmented Generation) service for semantic search over portfolio content.
"""
import json
import chromadb
from chromadb.config import Settings as ChromaSettings
# from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any
from pathlib import Path
from config import get_settings


class RAGService:
    """Handles document embedding and semantic search."""

    def __init__(self):
        self.settings = get_settings()
        self.embedding_model = None #SentenceTransformer(self.settings.embedding_model)

        # Initialize ChromaDB
        self.client = chromadb.PersistentClient(
            path=self.settings.vector_store_path,
            settings=ChromaSettings(anonymized_telemetry=False)
        )

        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name="portfolio",
            metadata={"description": "Portfolio content for RAG"}
        )

        # Load and index content if collection is empty
        if self.collection.count() == 0:
            self._load_and_index_content()

    def _load_portfolio_data(self) -> Dict[str, Any]:
        """Load portfolio data from JSON file."""
        with open(self.settings.portfolio_data_path, 'r') as f:
            return json.load(f)

    def _create_document_chunks(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create searchable document chunks from portfolio data."""
        chunks = []

        # Personal info chunk
        personal = data.get('personal', {})
        chunks.append({
            'text': f"{personal.get('name')} - {personal.get('title')}. {personal.get('bio')}",
            'metadata': {'type': 'personal', 'id': 'personal_info'}
        })

        # Skills chunks
        skills = data.get('skills', {})
        for category, skill_list in skills.items():
            chunks.append({
                'text': f"{category.replace('_', ' ').title()} skills: {', '.join(skill_list)}",
                'metadata': {'type': 'skills', 'category': category}
            })

        # Project chunks (detailed)
        for project in data.get('projects', []):
            # Main project description
            project_text = f"""
            Project: {project['title']}
            Description: {project.get('long_description', project['description'])}
            Technologies: {', '.join(project['tech_stack'])}
            Highlights: {' '.join(project['highlights'])}
            Category: {project['category']}
            """
            chunks.append({
                'text': project_text.strip(),
                'metadata': {
                    'type': 'project',
                    'id': project['id'],
                    'title': project['title'],
                    'category': project['category'],
                    'featured': project.get('featured', False)
                }
            })

        # Experience chunks
        for exp in data.get('experience', []):
            exp_text = f"""
            Role: {exp['role']} at {exp['company']}
            Duration: {exp['duration']}
            Description: {exp['description']}
            Responsibilities: {' '.join(exp['responsibilities'])}
            Achievements: {' '.join(exp['achievements'])}
            Technologies: {', '.join(exp['tech_stack'])}
            """
            chunks.append({
                'text': exp_text.strip(),
                'metadata': {
                    'type': 'experience',
                    'id': exp['id'],
                    'company': exp['company'],
                    'role': exp['role']
                }
            })

        # Blog post chunks
        for post in data.get('blog_posts', []):
            post_text = f"""
            Blog Post: {post['title']}
            Summary: {post['excerpt']}
            Category: {post['category']}
            Tags: {', '.join(post['tags'])}
            """
            chunks.append({
                'text': post_text.strip(),
                'metadata': {
                    'type': 'blog',
                    'id': post['id'],
                    'title': post['title'],
                    'slug': post['slug']
                }
            })

        return chunks

    def _load_and_index_content(self):
        """Load portfolio content and create embeddings."""
        print("Loading and indexing portfolio content...")

        # Load data
        data = self._load_portfolio_data()

        # Create chunks
        chunks = self._create_document_chunks(data)

        # Prepare for ChromaDB
        texts = [chunk['text'] for chunk in chunks]
        metadatas = [chunk['metadata'] for chunk in chunks]
        ids = [f"{chunk['metadata']['type']}_{i}" for i, chunk in enumerate(chunks)]

        # Add to collection (ChromaDB will handle embeddings via sentence-transformers)
        self.collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )

        print(f"Indexed {len(chunks)} document chunks")

    def search(self, query: str, top_k: int = None) -> List[Dict[str, Any]]:
        """
        Perform semantic search over portfolio content.

        Args:
            query: Search query text
            top_k: Number of results to return (default from settings)

        Returns:
            List of relevant document chunks with metadata
        """
        if top_k is None:
            top_k = self.settings.top_k_results

        # Query the collection
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )

        # Format results
        formatted_results = []
        if results['documents'] and len(results['documents']) > 0:
            for i in range(len(results['documents'][0])):
                formatted_results.append({
                    'text': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'distance': results['distances'][0][i] if 'distances' in results else None
                })

        return formatted_results

    def get_context_string(self, query: str) -> str:
        """
        Get formatted context string for LLM prompt.

        Args:
            query: Search query

        Returns:
            Formatted context string
        """
        results = self.search(query)

        if not results:
            return "No relevant information found."

        context_parts = []
        for i, result in enumerate(results, 1):
            context_parts.append(f"[Source {i}]:\n{result['text']}\n")

        return "\n".join(context_parts)


# Global instance
_rag_service = None


def get_rag_service() -> RAGService:
    """Get or create RAG service singleton."""
    global _rag_service
    if _rag_service is None:
        _rag_service = RAGService()
    return _rag_service