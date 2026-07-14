from src.data_loader import load_documents, create_chunks
from src.embeddings import setup_qdrant

print("📄 Documents load ho rahe hain...")
docs = load_documents()

print("✂️ Chunks ban rahe hain...")
parent_chunks, child_chunks = create_chunks(docs)

print("🔢 Qdrant mein store ho raha hai...")
setup_qdrant(child_chunks)

print("✅ Database ready!")