import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.drive import get_drive_service, list_files_in_folder, download_file_content
from utils.vectorstore import init_pinecone, get_or_create_index, get_embeddings

load_dotenv()

# Load environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")

# Initialize services
drive_service = get_drive_service(GOOGLE_API_KEY)
init_pinecone(PINECONE_API_KEY, PINECONE_ENV)
index = get_or_create_index("company-files")
embeddings = get_embeddings()

# Ingest pipeline
def ingest_drive_files():
    files = list_files_in_folder(drive_service, DRIVE_FOLDER_ID)
    for file in files:
        print(f"Processing: {file['name']}")
        text = download_file_content(drive_service, file["id"])

        # Split text
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = splitter.split_text(text)

        # Embed & store
        vectors = [
            (f"{file['id']}_{i}", embeddings.embed_query(chunk), {"text": chunk})
            for i, chunk in enumerate(docs)
        ]
        index.upsert(vectors)
        print(f"✅ Stored {len(vectors)} chunks from {file['name']}")

if __name__ == "__main__":
    ingest_drive_files()
