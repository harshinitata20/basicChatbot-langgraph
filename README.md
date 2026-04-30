# LangGraph Agentic AI Chatbot

A stateful chatbot built with LangGraph and Streamlit, powered by Groq LLMs. Supports both a basic conversational mode and a web-search-enabled agentic mode using Tavily.

## Features

- Stateful conversation graph using LangGraph
- Groq LLM backend with selectable models
- Streamlit UI with persistent chat history
- **Basic Chatbot** — direct LLM conversation
- **Chatbot with Web Search** — agentic loop with Tavily search tool, showing tool calls and results inline
- Modular architecture (nodes, state, graph, UI layers)

## Project Structure

```
BasicChatbot/
├── app.py                              # Streamlit entry point
├── requirements.txt
└── src/
    └── langgraphagentic/
        ├── graph/
        │   └── graph_builder.py        # LangGraph state machine
        ├── llms/
        │   └── groqllm.py              # Groq LLM wrapper
        ├── nodes/
        │   ├── basic_chatbot_nodes.py  # Basic chatbot node
        │   └── chatbot_with_tool_node.py  # Tool-enabled chatbot node
        ├── state/
        │   └── state.py                # Conversation state definition
        ├── tools/
        │   └── search_tool.py          # Tavily web search tool
        └── ui/
            ├── uiconfig.ini            # UI configuration
            ├── uiconfig.py             # Config reader
            └── streamlitui/
                ├── loadui.py           # Sidebar and layout
                └── display_result.py   # Chat display logic
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

### 4. Get API keys

- **Groq API key** — sign up at [console.groq.com](https://console.groq.com) (free)
- **Tavily API key** — sign up at [tavily.com](https://tavily.com) (free tier available, required for web search use case only)

## Running the App

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

## Usage

### Basic Chatbot

1. In the sidebar, select **Groq** as the LLM
2. Select **Basic Chatbot** as the use case
3. Choose any model from the dropdown
4. Paste your Groq API key
5. Type a message and press Enter

### Chatbot with Web Search

1. In the sidebar, select **Groq** as the LLM
2. Select **Chatbot with Web Search** as the use case
3. Choose a model (only tool-compatible models are shown)
4. Paste your Groq API key
5. Paste your Tavily API key
6. Ask anything — the agent will search the web and show tool results inline

## Supported Models

| Model | Basic Chatbot | Web Search |
|---|---|---|
| `llama-3.1-8b-instant` | Yes | Yes |
| `llama-3.3-70b-versatile` | Yes | Yes |
| `meta-llama/llama-4-scout-17b-16e-instruct` | Yes | No* |

> \* llama-4-scout has a built-in `brave_search` tool on Groq that conflicts with custom tool binding. It is automatically hidden when the Web Search use case is selected.

## Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph) — stateful agent graph
- [LangChain Groq](https://python.langchain.com/docs/integrations/chat/groq/) — Groq LLM integration
- [LangChain Community](https://python.langchain.com/docs/integrations/tools/tavily_search/) — Tavily search tool
- [Streamlit](https://streamlit.io) — web UI
- [Tavily](https://tavily.com) — web search API
