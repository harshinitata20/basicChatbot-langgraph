from langgraph.graph import StateGraph
from src.langgraphagentic.state.state import State
from langgraph.graph import START, END
from src.langgraphagentic.nodes.basic_chatbot_nodes import BasicChatbotNode
from src.langgraphagentic.tools.search_tool import get_tools, create_tool_nodes
from src.langgraphagentic.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from langgraph.prebuilt import ToolNode, tools_condition
class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder= StateGraph(State)

    def basic_chatbot_build_graph(self):
        """Builds a basic chatbot graph using the provided LLM model."""
        self.basic_chatbot_node=BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools(self):
        """Builds a chatbot with tools graph using the provided LLM model."""
        tools=get_tools()
        tool_nodes=create_tool_nodes(tools)

        llm=self.llm

        obj_chatbot_with_tool_node=ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_tool_node.create_chatbot(tools)
        

        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_nodes)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        
    def setup_graph(self, usecase):
        """Sets up the graph by building the basic chatbot graph and returns compiled graph."""
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot with Web Search":
            self.chatbot_with_tools()
        return self.graph_builder.compile()
