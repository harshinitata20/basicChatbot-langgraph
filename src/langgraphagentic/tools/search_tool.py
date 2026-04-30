from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """Returns a list of tools to be used in the chatbot graph."""
    tools=[TavilySearchResults(max_results=2)]
    return tools

def create_tool_nodes(tools):
    """Creates ToolNode instances for each tool in the provided list."""
    return ToolNode(tools=tools)