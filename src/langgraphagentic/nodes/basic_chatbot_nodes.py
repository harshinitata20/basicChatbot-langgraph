from src.langgraphagentic.state.state import State


class BasicChatbotNode:
    """A basic chatbot node that uses a language model to generate responses."""
    def __init__(self,model):
        self.llm=model

    def process(self, state:State)->dict:
        """Processes the input state and generates a response using the language model."""
        return{"messages": self.llm.invoke(state["messages"])}
    