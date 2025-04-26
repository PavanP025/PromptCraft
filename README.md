
# PromptCraft - AI Prompt Engineering Assistant 🤖

A sophisticated web application that helps users create effective, context-aware prompts for AI interactions across different sectors and AI tools.

## Core Features 🌟

- **Multi-Mode Interface**
  - Simple Mode: Quick prompt generation with direct scenario input
  - Detailed Mode: Advanced prompt creation with contextual parameters
  - Sector-Specific Mode: Tailored prompts for different industries
  - AI Tool-Specific Mode: Specialized prompts for various AI tools

- **Industry Sectors 🏢**
  - 🎬 Filmmaking
  - 💻 IT & Software Development
  - 📱 Social Media & Marketing
  - 🎨 Digital Art & Illustration
  - 🛍️ E-commerce & Branding
  - 🧑‍🏫 Education & Learning
  - ✍️ Writing & Content Creation

- **AI Tools Integration 🛠️**
  - 🤖 GPT Models
  - 🎨 Image Generation
  - 🎥 Video Generation
  - 🔊 Audio Generation
  - 👨‍💻 Development Tools

- **Smart Features**
  - Dynamic question sets based on sector/tool selection
  - Theme toggling (Light/Dark mode)
  - Responsive design for all devices
  - Context-aware prompt generation

## Technical Stack 💻

- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript, CSS
- **AI Integration**: OpenAI GPT-3.5 Turbo
- **Document Processing**: 
  - LangChain for RAG implementation
  - ChromaDB for vector storage
  - HuggingFace Embeddings
  - PyPDF for document parsing

## Getting Started 🚀

1. Set up your environment variables:
   ```
   OPENAI_API_KEY=your_api_key_here
   FLASK_SECRET_KEY=your_secret_key_here
   ```

2. Run the application:
   ```
   python main.py
   ```
   The application will be available at `http://0.0.0.0:5000`

## Project Structure 📁

```
├── attached_assets/     # PDF resources for different sectors and tools
├── data/               # Storage for processed data
├── static/            # Static assets
├── templates/         # HTML templates
│   ├── index.html    # Main application interface
│   ├── sectors.html  # Sector selection page
│   └── ai_tools.html # AI tools selection page
├── main.py           # Flask application
└── rag_builder.py    # RAG system implementation
```

## Features in Detail 📋

### Simple Mode
- Quick prompt generation with minimal input
- Direct scenario description
- Instant prompt templates

### Detailed Mode
- Comprehensive questionnaire
- Task specification
- Audience level selection
- Goal definition
- Response type customization

### RAG System
- Processes sector-specific documents
- Contextual prompt enhancement
- Dynamic knowledge integration

## License 📄

[MIT License](LICENSE)

## Acknowledgments 🙏

- OpenAI for GPT API
- LangChain community
- All contributors
