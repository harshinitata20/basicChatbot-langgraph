from langgraph.graph import StateGraph
from src.langgraphagentic.state.state import State
from langgraph.graph import START, END
from src.langgraphagentic.nodes.basic_chatbot_nodes import BasicChatbotNode

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

    def setup_graph(self, usecase):
        """Sets up the graph by building the basic chatbot graph and returns compiled graph."""
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()
