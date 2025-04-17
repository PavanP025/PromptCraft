
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import os

def build_rag_db():
    # Initialize the embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    
    # Load and process PDFs
    pdf_dir = "attached_assets"
    documents = []
    
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith('.pdf'):
            loader = PyPDFLoader(os.path.join(pdf_dir, pdf_file))
            documents.extend(loader.load())
    
    # Split documents into chunks
    chunks = text_splitter.split_documents(documents)
    
    # Create and persist vector store
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="data/chroma_db"
    )
    db.persist()
    
    return len(chunks)

if __name__ == "__main__":
    chunk_count = build_rag_db()
    print(f"RAG database built successfully with {chunk_count} chunks!")
