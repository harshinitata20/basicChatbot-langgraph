from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from src.langgraphagentic.state.state import State
from src.langgraphagentic.nodes.basic_chatbot_nodes import BasicChatbotNode
from src.langgraphagentic.tools.search_tool import get_tools, create_tool_nodes
from src.langgraphagentic.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphagentic.nodes.ai_news_node import AINewsNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools(self):
        tools = get_tools()
        tool_nodes = create_tool_nodes(tools)
        obj_chatbot_with_tool_node = ChatbotWithToolNode(self.llm)
        chatbot_node = obj_chatbot_with_tool_node.create_chatbot(tools)

        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_nodes)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")

    def ai_news_builder_graph(self):
        ai_news_node = AINewsNode(self.llm)

        self.graph_builder.add_node("fetch_news", ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news", ai_news_node.summarize_news)
        self.graph_builder.add_node("save_results", ai_news_node.save_results)

        self.graph_builder.add_edge(START, "fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize_news")
        self.graph_builder.add_edge("summarize_news", "save_results")
        self.graph_builder.add_edge("save_results", END)

    def setup_graph(self, usecase):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Web Search":
            self.chatbot_with_tools()
        elif usecase == "AI News Summarizer":
            self.ai_news_builder_graph()
        return self.graph_builder.compile()
