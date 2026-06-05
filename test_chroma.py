import chromadb

# Create a local ChromaDB that saves to disk
client = chromadb.PersistentClient(path="./data/chroma_db")

# Create a collection - think of this like a database table
collection = client.get_or_create_collection(name="test_collection")

# Add some text documents with IDs
collection.add(
    documents=[
        "Python is a programming language great for backend development",
        "FastAPI is a modern Python web framework for building APIs",
        "ChromaDB is a vector database that stores embeddings",
        "Ollama runs large language models locally on your machine",
        "Django is a batteries included Python web framework"
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
)

# Now query by meaning - not exact match
results = collection.query(
    query_texts=["I want to build a REST API in Python"],
    n_results=2
)

print(f"All Results: {results}")

print("\n=== QUERY: I want to build a REST API in Python ===")
for i, doc in enumerate(results['documents'][0]):
    print(f"\nResult {i+1}: {doc}")

print("\n=== DISTANCES (lower = more similar) ===")
for i, dist in enumerate(results['distances'][0]):
    print(f"Result {i+1} distance: {dist:.4f}")


query2 = "I want to store and retrieve vectors"
results2 = collection.query(
    query_texts=[query2],
    n_results=2
)

print(f"\n=== QUERY: {query2} ===")
for i, doc in enumerate(results2['documents'][0]):
    print(f"\nResult {i+1}: {doc}")

print("\n=== DISTANCES (lower = more similar) ===")
for i, dist in enumerate(results2['distances'][0]):
    print(f"Result {i+1} distance: {dist:.4f}")


query3 = "What is the best recipe for Chocolate Chip Cookies?"
results3 = collection.query(
    query_texts=[query3],
    n_results=2
)

print("\n=== QUERY: What is the best recipe for Chocolate Chip Cookies? ===")
for i, doc in enumerate(results3['documents'][0]):
    print(f"\nResult {i+1}: {doc}")

print("\n=== DISTANCES (lower = more similar) ===")
for i, dist in enumerate(results3['distances'][0]):
    print(f"Result {i+1} distance: {dist:.4f}")

