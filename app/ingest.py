import chromadb
import pymupdf
import hashlib
import os
from pathlib import Path


# ─── Configuration ───────────────────────────────────────────
CHROMA_PATH  = "./data/chroma_db"
UPLOAD_PATH  = "./data/uploads"
CHUNK_SIZE   = 500   # characters per chunk
CHUNK_OVERLAP = 50   # overlap between chunks


# ─── Connect to ChromaDB ─────────────────────────────────────
def get_collection(collection_name: str = "documents"):
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    return client.get_or_create_collection(name=collection_name)


# ─── Extract text from PDF ───────────────────────────────────
def extract_text_from_pdf(pdf_path: str) -> str:
    """Open a PDF and extract all text from every page"""
    
    doc = pymupdf.open(pdf_path)
    full_text = ""
    
    for page_num, page in enumerate(doc):
        text = page.get_text()
        full_text += f"\n[Page {page_num + 1}]\n{text}"
    
    doc.close()
    
    print(f"  Extracted {len(full_text)} characters "
          f"from {len(doc)} pages")
    
    return full_text


# ─── Split text into chunks ──────────────────────────────────
def split_into_chunks(text: str, 
                      chunk_size: int = CHUNK_SIZE,
                      overlap: int = CHUNK_OVERLAP) -> list[str]:
    """
    Split text into overlapping chunks.
    Overlap ensures sentences split across chunk 
    boundaries don't lose context.
    """
    
    chunks = []
    start  = 0
    
    while start < len(text):
        end   = start + chunk_size
        chunk = text[start:end]
        
        # Don't store empty or whitespace-only chunks
        if chunk.strip():
            chunks.append(chunk.strip())
        
        # Move forward by chunk_size minus overlap
        # This creates the overlap between consecutive chunks
        start += chunk_size - overlap
    
    print(f"  Split into {len(chunks)} chunks "
          f"(size={chunk_size}, overlap={overlap})")
    
    return chunks


# ─── Generate a unique ID for each chunk ─────────────────────
def generate_chunk_id(pdf_name: str, chunk_index: int) -> str:
    """
    Create a unique, reproducible ID for each chunk.
    Using filename + index means re-ingesting the same 
    PDF won't create duplicate chunks.
    """
    raw = f"{pdf_name}_chunk_{chunk_index}"
    return hashlib.md5(raw.encode()).hexdigest()


# ─── Check if PDF already ingested ───────────────────────────
def is_already_ingested(collection, pdf_name: str) -> bool:
    """
    Check if this PDF was already ingested by looking 
    for its first chunk ID in ChromaDB.
    Prevents duplicate ingestion.
    """
    first_chunk_id = generate_chunk_id(pdf_name, 0)
    result = collection.get(ids=[first_chunk_id])
    return len(result['ids']) > 0


# ─── Main ingestion function ──────────────────────────────────
def ingest_pdf(pdf_path: str, 
               collection_name: str = "documents") -> dict:
    """
    Full pipeline:
    1. Extract text from PDF
    2. Split into chunks
    3. Store chunks in ChromaDB
    
    Returns a summary of what was ingested.
    """
    
    pdf_name   = Path(pdf_path).name
    collection = get_collection(collection_name)
    
    print(f"\nIngesting: {pdf_name}")
    
    # Skip if already ingested
    if is_already_ingested(collection, pdf_name):
        print(f"  Already ingested — skipping")
        return {
            "status":  "skipped",
            "file":    pdf_name,
            "chunks":  0,
            "message": "Already ingested"
        }
    
    # Step 1 — Extract text
    print(f"  Step 1: Extracting text...")
    text = extract_text_from_pdf(pdf_path)
    
    if not text.strip():
        return {
            "status":  "error",
            "file":    pdf_name,
            "chunks":  0,
            "message": "No text found — PDF may be scanned image"
        }
    
    # Step 2 — Split into chunks
    print(f"  Step 2: Splitting into chunks...")
    chunks = split_into_chunks(text)
    
    # Step 3 — Store in ChromaDB
    print(f"  Step 3: Storing in ChromaDB...")
    
    ids       = []
    metadatas = []
    
    for i, chunk in enumerate(chunks):
        ids.append(generate_chunk_id(pdf_name, i))
        metadatas.append({
            "source":      pdf_name,
            "chunk_index": i,
            "total_chunks": len(chunks)
        })
    
    # Store in batches of 100 to avoid memory issues
    batch_size = 100
    for i in range(0, len(chunks), batch_size):
        collection.add(
            documents=chunks[i:i + batch_size],
            ids=ids[i:i + batch_size],
            metadatas=metadatas[i:i + batch_size]
        )
    
    print(f"  Done — {len(chunks)} chunks stored\n")
    
    return {
        "status":  "success",
        "file":    pdf_name,
        "chunks":  len(chunks),
        "message": f"Successfully ingested {len(chunks)} chunks"
    }


# ─── Run directly to test ─────────────────────────────────────
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python -m app.ingest <path_to_pdf>")
        print("Example: python -m app.ingest data/uploads/sample.pdf")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        sys.exit(1)
    
    result = ingest_pdf(pdf_path)
    print(f"Result: {result}")