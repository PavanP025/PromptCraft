
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import os

def build_category_rag_db(category_type, category_name):
    # Initialize the embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    
    # Define paths
    base_pdf_dir = "attached_assets"
    category_pdf_dir = os.path.join(base_pdf_dir, category_type, category_name)
    common_pdfs = [
        "Prompt-Engineering-A-Blueprint-for-AI-Excellence.pdf",
        "THE PROMPT ENGINEERING GUIDE V2.pdf"
    ]
    
    # Load and process PDFs
    documents = []
    
    # Load category-specific PDFs
    if os.path.exists(category_pdf_dir):
        for pdf_file in os.listdir(category_pdf_dir):
            if pdf_file.endswith('.pdf'):
                loader = PyPDFLoader(os.path.join(category_pdf_dir, pdf_file))
                documents.extend(loader.load())
    
    # Load common PDFs
    for common_pdf in common_pdfs:
        common_pdf_path = os.path.join(base_pdf_dir, common_pdf)
        if os.path.exists(common_pdf_path):
            loader = PyPDFLoader(common_pdf_path)
            documents.extend(loader.load())
    
    # Split documents into chunks
    chunks = text_splitter.split_documents(documents)
    
    # Create directory for database
    db_dir = f"data/chroma_db_{category_type}_{category_name}"
    os.makedirs(db_dir, exist_ok=True)
    
    # Create and persist vector store
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_dir
    )
    db.persist()
    
    return len(chunks)

def build_all_rags():
    # Define categories
    sectors = ['filmmaking', 'it', 'social', 'art', 'ecommerce', 'education', 'writing']
    ai_tools = ['gpt', 'dalle', 'runway', 'elevenlabs', 'copilot']
    
    total_chunks = 0
    
    # Build RAG for each sector
    for sector in sectors:
        chunks = build_category_rag_db('sectors', sector)
        print(f"Built RAG for sector '{sector}' with {chunks} chunks")
        total_chunks += chunks
    
    # Build RAG for each AI tool
    for tool in ai_tools:
        chunks = build_category_rag_db('ai_tools', tool)
        print(f"Built RAG for AI tool '{tool}' with {chunks} chunks")
        total_chunks += chunks
    
    return total_chunks

if __name__ == "__main__":
    total_chunks = build_all_rags()
    print(f"All RAG databases built successfully with total {total_chunks} chunks!")
