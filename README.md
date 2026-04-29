# LangGraph Agentic AI Chatbot

A stateful chatbot built with LangGraph and Streamlit, powered by Groq LLMs.

## Features

- Stateful conversation graph using LangGraph
- Groq LLM backend with selectable models
- Streamlit UI with persistent chat history
- Modular architecture (nodes, state, graph, UI layers)

## Project Structure

```
BasicChatbot/
├── app.py                          # Streamlit entry point
├── requirements.txt
└── src/
    └── langgraphagentic/
        ├── graph/
        │   └── graph_builder.py    # LangGraph state machine
        ├── llms/
        │   └── groqllm.py          # Groq LLM wrapper
        ├── nodes/
        │   └── basic_chatbot_nodes.py  # Chatbot node logic
        ├── state/
        │   └── state.py            # Conversation state definition
        └── ui/
            ├── uiconfig.ini        # UI configuration
            ├── uiconfig.py         # Config reader
            └── streamlitui/
                ├── loadui.py       # Sidebar and layout
                └── display_result.py  # Chat display
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/harshinitata20/basicChatbot-langgraph.git
cd basicChatbot-langgraph
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get a Groq API key

Sign up at [console.groq.com](https://console.groq.com) and create a free API key.

## Running the App

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

## Usage

1. In the sidebar, select **Groq** as the LLM
2. Choose a model (e.g. `llama-3.1-8b-instant`)
3. Paste your Groq API key
4. Select the **Basic Chatbot** use case
5. Type a message in the chat input and press Enter

## Supported Models

| Model | Speed |
|---|---|
| `llama-3.1-8b-instant` | Fastest |
| `llama-3.3-70b-versatile` | Most capable |
| `meta-llama/llama-4-scout-17b-16e-instruct` | Latest (Llama 4) |

## Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph) — stateful agent graph
- [LangChain Groq](https://python.langchain.com/docs/integrations/chat/groq/) — Groq LLM integration
- [Streamlit](https://streamlit.io) — web UI
