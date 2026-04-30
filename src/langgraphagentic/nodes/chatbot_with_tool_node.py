from src.langgraphagentic.state.state import State

class ChatbotWithToolNode:
    """A node that represents a chatbot with tool integration."""
    def __init__(self,model):
        self.llm=model

    def process(self, state: State)->dict:
        """Processes the input state and returns a response."""
        user_input=state["messages"][-1] if state["messages"] else ""
        llm_response=self.llm.invoke([{"role": "user", "content": user_input}])

        tools_response = f"Tools have been invoked based on the user input: {user_input}"

        return{"messages": [llm_response, tools_response]}
    
    def create_chatbot(self, tools):
        """Creates a chatbot node with tool integration."""
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node