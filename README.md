
# AI Prompt Generator 🤖

A web-based tool for generating effective AI prompts using OpenAI's GPT models. This application helps users create well-structured prompts for better AI interactions.

## Features 🌟

- **Dual Mode Interface**
  - Simple Mode: Quick prompt generation with scenario description
  - Detailed Mode: Comprehensive prompt creation with specific parameters

- **Customization Options**
  - Task specification
  - Audience expertise level selection
  - Goal definition
  - Response type preference

- **RAG Integration**
  - Built-in Retrieval Augmented Generation (RAG) system
  - PDF document processing capabilities
  - Efficient text chunking and embedding

## Tech Stack 💻

- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript, CSS
- **AI Integration**: OpenAI GPT-3.5 Turbo
- **RAG Components**: 
  - LangChain
  - ChromaDB
  - HuggingFace Embeddings
  - PyPDF

## Getting Started 🚀

1. Clone the repository
2. Set up your OpenAI API key in the environment variables
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```
   The application will be available at `http://127.0.0.1:5000`

## Usage Guide 📖

1. **Simple Mode**
   - Enter your scenario description
   - Click "Generate Prompt"
   - Get your customized prompt template

2. **Detailed Mode**
   - Specify the task details
   - Select expertise level
   - Choose your goal
   - Pick preferred response type
   - Generate your specialized prompt

## RAG System Usage 📚

To use the RAG system:
1. Place PDF documents in the `attached_assets` directory
2. Run the RAG builder:
   ```bash
   python rag_builder.py
   ```
3. The system will process and index your documents for enhanced prompt generation

## Contributing 🤝

Feel free to submit issues and enhancement requests!

## License 📄

[MIT License](LICENSE)

## Acknowledgments 🙏

- OpenAI for GPT API
- LangChain community
- All contributors and users of this tool
