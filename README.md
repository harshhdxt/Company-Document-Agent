# Company Docs Chatbot (Google Drive + Pinecone + Gemini)

A chatbot that can answer questions from your company's documents stored in Google Drive.
Automatically watches for file updates, embeds them using Google Gemini, stores in Pinecone, and retrieves relevant context during chat.

---

## **Features**
- Watches a Google Drive folder for new or updated files
- Downloads and splits text into chunks
- Embeds text with Google Gemini
- Stores embeddings in Pinecone vector store
- Chat interface with retrieval-augmented generation

---

## **Setup**
### 1. Create Google Cloud Project
- Enable Google Drive API
- Enable Google Generative AI API
- Get your API key from [Google AI Studio](https://aistudio.google.com/)

### 2. Setup Pinecone
- Sign up at [Pinecone.io](https://www.pinecone.io/)
- Create an API key
- Create an index named `company-files`

### 3. Environment Variables
Copy `.env.example` → `.env` and fill in your keys:
```env
GOOGLE_API_KEY=your_google_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENV=us-east1-gcp
DRIVE_FOLDER_ID=your_drive_folder_id_here
