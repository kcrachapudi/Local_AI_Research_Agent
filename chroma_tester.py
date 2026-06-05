import chromadb
import argparse
import json

def add_documents(collection, documents: list[str], ids: list[str]):
    """Add documents to ChromaDB collection"""
    
    existing = collection.get()
    existing_ids = existing['ids']
    
    new_docs = []
    new_ids = []
    
    for doc, id in zip(documents, ids):
        if id not in existing_ids:
            new_docs.append(doc)
            new_ids.append(id)
        else:
            print(f"  Skipping '{id}' — already exists")
    
    if new_docs:
        collection.add(documents=new_docs, ids=new_ids)
        print(f"  Added {len(new_docs)} documents\n")


def query_collection(collection, query_texts: list[str], n_results: int = 3):
    """Query ChromaDB and return results"""
    
    results = collection.query(
        query_texts=query_texts,
        n_results=n_results
    )
    
    output = []
    
    for q_idx, query in enumerate(query_texts):
        query_result = {
            "query": query,
            "results": []
        }
        
        docs = results['documents'][q_idx]
        distances = results['distances'][q_idx]
        ids = results['ids'][q_idx]
        
        for rank, (doc, dist, id) in enumerate(zip(docs, distances, ids)):
            query_result["results"].append({
                "rank":     rank + 1,
                "id":       id,
                "document": doc,
                "distance": round(dist, 4),
                "similarity": f"{round((1 - dist) * 100, 1)}%"
            })
        
        output.append(query_result)
    
    return output


def print_results(output: list):
    """Print results in a readable format"""
    
    for query_result in output:
        print(f"\n{'='*60}")
        print(f"QUERY: {query_result['query']}")
        print(f"{'='*60}")
        
        for r in query_result["results"]:
            print(f"\n  Rank {r['rank']}:")
            print(f"  ID:         {r['id']}")
            print(f"  Document:   {r['document']}")
            print(f"  Distance:   {r['distance']}  "
                  f"(Similarity: {r['similarity']})")


def main():
    parser = argparse.ArgumentParser(
        description="ChromaDB tester — add documents and query by meaning"
    )
    
    parser.add_argument(
        "--collection",
        type=str,
        default="test_collection",
        help="Collection name (default: test_collection)"
    )
    
    parser.add_argument(
        "--add",
        nargs=2,
        metavar=("DOCUMENTS_JSON", "IDS_JSON"),
        help='Add documents. Pass two JSON arrays: '
             '"[\\"doc1\\",\\"doc2\\"]" "[\\"id1\\",\\"id2\\"]"'
    )
    
    parser.add_argument(
        "--query",
        nargs="+",
        metavar="QUERY",
        help="One or more queries to run against the collection"
    )
    
    parser.add_argument(
        "--n",
        type=int,
        default=2,
        help="Number of results to return per query (default: 2)"
    )
    
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all documents currently in the collection"
    )
    
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear all documents from the collection"
    )

    args = parser.parse_args()
    
    # Connect to ChromaDB
    client = chromadb.PersistentClient(path="./data/chroma_db")
    collection = client.get_or_create_collection(name=args.collection)
    
    # List documents
    if args.list:
        existing = collection.get()
        print(f"\nCollection '{args.collection}' "
              f"has {len(existing['ids'])} documents:\n")
        for id, doc in zip(existing['ids'], existing['documents']):
            print(f"  [{id}] {doc}")
        return
    
    # Clear collection
    if args.clear:
        client.delete_collection(name=args.collection)
        print(f"\nCollection '{args.collection}' cleared.")
        return
    
    # Add documents
    if args.add:
        documents = json.loads(args.add[0])
        ids       = json.loads(args.add[1])
        
        if len(documents) != len(ids):
            print("Error: number of documents must match number of ids")
            return
        
        print(f"\nAdding {len(documents)} documents "
              f"to '{args.collection}'...")
        add_documents(collection, documents, ids)
    
    # Query
    if args.query:
        print(f"\nQuerying '{args.collection}'...")
        output = query_collection(collection, args.query, n_results=args.n)
        print_results(output)
        print()


if __name__ == "__main__":
    main()