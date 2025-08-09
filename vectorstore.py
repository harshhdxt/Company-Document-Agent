import os
import pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Pinecone as PineconeStore

def init_pinecone(api_key, environment):
    pinecone.init(api_key=api_key, environment=environment)

def get_or_create_index(index_name, dimension=768):
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(index_name, dimension=dimension)
    return pinecone.Index(index_name)

def get_vectorstore(index, embeddings):
    return PineconeStore(index, embeddings.embed_query, "text")

def get_embeddings():
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001")
