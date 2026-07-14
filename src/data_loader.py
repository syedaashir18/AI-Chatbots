from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def load_documents():
    docs = []
    for file in os.listdir("data"):
        try:
            if file.endswith(".txt"):
                loader = TextLoader(f"data/{file}", encoding="utf-8")
                docs.extend(loader.load())
            elif file.endswith(".pdf"):
                loader = PyPDFLoader(f"data/{file}")
                docs.extend(loader.load())
        except Exception as e:
            print(f"❌ {file}: {e}")
    print(f"✅ {len(docs)} documents loaded")
    return docs

def create_chunks(docs):
    parent_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )
    child_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    parent_chunks = parent_splitter.split_documents(docs)
    child_chunks = child_splitter.split_documents(docs)
    print(f"✅ Parent chunks: {len(parent_chunks)}")
    print(f"✅ Child chunks: {len(child_chunks)}")
    return parent_chunks, child_chunks