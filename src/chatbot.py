from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGSMITH_PROJECT", "legal-ai-chatbot")

def get_chain(retriever):
    prompt = PromptTemplate(
        template="""You are an expert Pakistani legal assistant.
Answer in the same language as the question (English or Urdu).
Use ONLY the context below to answer.
Always cite the relevant law/section number.
If not sure, say: "Please consult a qualified lawyer."
Add disclaimer at end: "⚠️ This is for informational purposes only."

Chat History:
{chat_history}

Context:
{context}

Question: {question}

Detailed Answer:""",
        input_variables=["context", "question", "chat_history"]
    )

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        api_key=os.getenv("GROQ_API_KEY")
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Returns a plain callable function — NOT a RunnableSequence
    def run_chain(inputs: dict) -> str:
        docs = retriever.invoke(inputs["question"])
        context = format_docs(docs)
        chain = prompt | llm | StrOutputParser()
        return chain.invoke({
            "context": context,
            "question": inputs["question"],
            "chat_history": inputs.get("chat_history", "")
        })

    return run_chain