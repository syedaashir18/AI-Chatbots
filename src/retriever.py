from langchain_community.retrievers import BM25Retriever
from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document
from src.embeddings import load_qdrant
from typing import List

class HybridRetriever(BaseRetriever):
    semantic_retriever: object
    bm25_retriever: object
    
    def _get_relevant_documents(self, query: str) -> List[Document]:
        semantic_docs = self.semantic_retriever.invoke(query)
        bm25_docs = self.bm25_retriever.invoke(query)
        
        # Combine and deduplicate
        seen = set()
        combined = []
        for doc in semantic_docs + bm25_docs:
            content = doc.page_content[:100]
            if content not in seen:
                seen.add(content)
                combined.append(doc)
        
        return combined[:8]

def get_retriever(chunks):
    vectorstore = load_qdrant()
    
    semantic_retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "fetch_k": 10}
    )
    
    bm25_retriever = BM25Retriever.from_documents(chunks)
    bm25_retriever.k = 5
    
    return HybridRetriever(
        semantic_retriever=semantic_retriever,
        bm25_retriever=bm25_retriever
    )