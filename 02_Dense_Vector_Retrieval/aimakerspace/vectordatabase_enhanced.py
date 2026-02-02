import numpy as np
from collections import defaultdict
from typing import List, Tuple, Callable, Dict, Optional
from aimakerspace.openai_utils.embedding import EmbeddingModel
import asyncio


def cosine_similarity(vector_a: np.array, vector_b: np.array) -> float:
    """Computes the cosine similarity between two vectors."""
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    return dot_product / (norm_a * norm_b)


def euclidean_distance(vector_a: np.array, vector_b: np.array) -> float:
    """Computes the Euclidean distance between two vectors (inverted for ranking)."""
    distance = np.linalg.norm(vector_a - vector_b)
    # Return inverse so that smaller distances (more similar) rank higher
    return 1 / (1 + distance)


def manhattan_distance(vector_a: np.array, vector_b: np.array) -> float:
    """Computes the Manhattan distance between two vectors (inverted for ranking)."""
    distance = np.sum(np.abs(vector_a - vector_b))
    return 1 / (1 + distance)


class VectorDatabaseWithMetadata:
    """
    Enhanced Vector Database with metadata support for filtering and categorization.

    Features:
    - Metadata storage for each document (year, source, topic, etc.)
    - Multiple distance metrics (cosine, euclidean, manhattan)
    - Metadata-based filtering during search
    - Statistics and analytics on stored documents
    """

    def __init__(self, embedding_model: EmbeddingModel = None):
        self.vectors = {}  # key -> vector
        self.metadata = {}  # key -> metadata dict
        self.embedding_model = embedding_model or EmbeddingModel()

    def insert(self, key: str, vector: np.array, metadata: Optional[Dict] = None) -> None:
        """Insert a vector with optional metadata."""
        self.vectors[key] = vector
        self.metadata[key] = metadata or {}

    def search(
        self,
        query_vector: np.array,
        k: int,
        distance_measure: Callable = cosine_similarity,
        filter_metadata: Optional[Dict] = None,
    ) -> List[Tuple[str, float, Dict]]:
        """
        Search for similar vectors with optional metadata filtering.

        Args:
            query_vector: The query vector to search for
            k: Number of results to return
            distance_measure: Distance function to use (cosine_similarity, euclidean_distance, manhattan_distance)
            filter_metadata: Optional dict to filter results (e.g., {"year": "2025", "topic": "investment"})

        Returns:
            List of tuples: (text, score, metadata)
        """
        # Apply metadata filtering if specified
        filtered_items = self.vectors.items()
        if filter_metadata:
            filtered_items = [
                (key, vector)
                for key, vector in self.vectors.items()
                if self._matches_filter(key, filter_metadata)
            ]
        else:
            filtered_items = list(self.vectors.items())

        # Calculate scores
        scores = [
            (key, distance_measure(query_vector, vector), self.metadata.get(key, {}))
            for key, vector in filtered_items
        ]

        # Sort by score (descending) and return top k
        return sorted(scores, key=lambda x: x[1], reverse=True)[:k]

    def _matches_filter(self, key: str, filter_metadata: Dict) -> bool:
        """Check if a document's metadata matches the filter criteria."""
        doc_metadata = self.metadata.get(key, {})
        for filter_key, filter_value in filter_metadata.items():
            if doc_metadata.get(filter_key) != filter_value:
                return False
        return True

    def search_by_text(
        self,
        query_text: str,
        k: int,
        distance_measure: Callable = cosine_similarity,
        filter_metadata: Optional[Dict] = None,
        return_as_text: bool = False,
    ) -> List[Tuple[str, float, Dict]]:
        """
        Search by text query with optional metadata filtering.

        Args:
            query_text: The text query to search for
            k: Number of results to return
            distance_measure: Distance function to use
            filter_metadata: Optional dict to filter results
            return_as_text: If True, return only text; if False, return (text, score, metadata)
        """
        query_vector = self.embedding_model.get_embedding(query_text)
        results = self.search(query_vector, k, distance_measure, filter_metadata)

        if return_as_text:
            return [result[0] for result in results]
        return results

    def retrieve_from_key(self, key: str) -> Tuple[np.array, Dict]:
        """Retrieve vector and metadata for a specific key."""
        return self.vectors.get(key, None), self.metadata.get(key, {})

    async def abuild_from_list(
        self,
        list_of_text: List[str],
        metadata_list: Optional[List[Dict]] = None
    ) -> "VectorDatabaseWithMetadata":
        """
        Build the database from a list of texts with optional metadata.

        Args:
            list_of_text: List of text documents
            metadata_list: Optional list of metadata dicts (same length as list_of_text)
        """
        embeddings = await self.embedding_model.async_get_embeddings(list_of_text)

        if metadata_list is None:
            metadata_list = [{}] * len(list_of_text)

        for text, embedding, metadata in zip(list_of_text, embeddings, metadata_list):
            self.insert(text, np.array(embedding), metadata)

        return self

    def get_statistics(self) -> Dict:
        """Get statistics about the stored documents."""
        stats = {
            "total_documents": len(self.vectors),
            "metadata_fields": set(),
            "metadata_values": defaultdict(set),
        }

        for metadata in self.metadata.values():
            for key, value in metadata.items():
                stats["metadata_fields"].add(key)
                stats["metadata_values"][key].add(value)

        # Convert sets to lists for JSON serialization
        stats["metadata_fields"] = list(stats["metadata_fields"])
        stats["metadata_values"] = {
            k: list(v) for k, v in stats["metadata_values"].items()
        }

        return stats

    def filter_by_metadata(self, filter_dict: Dict) -> List[str]:
        """Get all document keys that match the given metadata filter."""
        return [
            key for key in self.vectors.keys()
            if self._matches_filter(key, filter_dict)
        ]


if __name__ == "__main__":
    # Example usage with metadata
    list_of_text = [
        "I like to eat broccoli and bananas.",
        "I ate a banana and spinach smoothie for breakfast.",
        "Chinchillas and kittens are cute.",
        "My sister adopted a kitten yesterday.",
        "Look at this cute hamster munching on a piece of broccoli.",
    ]

    # Create metadata for each document
    metadata_list = [
        {"category": "food", "sentiment": "positive"},
        {"category": "food", "sentiment": "neutral"},
        {"category": "animals", "sentiment": "positive"},
        {"category": "animals", "sentiment": "neutral"},
        {"category": "animals", "sentiment": "positive"},
    ]

    vector_db = VectorDatabaseWithMetadata()
    vector_db = asyncio.run(vector_db.abuild_from_list(list_of_text, metadata_list))

    # Search with metadata filter
    print("=== Search with filter (animals only) ===")
    results = vector_db.search_by_text(
        "cute pets",
        k=2,
        filter_metadata={"category": "animals"}
    )
    for text, score, metadata in results:
        print(f"Score: {score:.3f}, Metadata: {metadata}")
        print(f"Text: {text[:80]}...\n")

    # Compare distance metrics
    print("\n=== Comparing Distance Metrics ===")
    query = "I think fruit is awesome!"

    print("Cosine Similarity:")
    results_cosine = vector_db.search_by_text(query, k=2, distance_measure=cosine_similarity)
    for text, score, _ in results_cosine:
        print(f"  Score: {score:.3f}, Text: {text[:60]}...")

    print("\nEuclidean Distance:")
    results_euclidean = vector_db.search_by_text(query, k=2, distance_measure=euclidean_distance)
    for text, score, _ in results_euclidean:
        print(f"  Score: {score:.3f}, Text: {text[:60]}...")

    print("\n=== Database Statistics ===")
    print(vector_db.get_statistics())
