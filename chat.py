import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.vectorstore import init_pinecone, get_embeddings, get_vectorstore
import pinecone

load_dotenv()

# Load env vars
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")

# Initialize Pinecone
init_pinecone(PINECONE_API_KEY, PINECONE_ENV)
index = pinecone.Index("company-files")

# Setup Vector Store
embeddings = get_embeddings()
vectorstore = get_vectorstore(index, embeddings)

# Setup Chat LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Setup Retrieval QA Chain
qa = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=vectorstore.as_retriever(),
    memory=memory
)

if __name__ == "__main__":
    print("💬 Company Docs Chatbot Ready (type 'exit' to quit)")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        result = qa.run(query)
        print("Bot:", result)
