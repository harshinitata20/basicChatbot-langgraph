from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

from typing import Annotated

class State(TypedDict):
    """State class to manage the state of the LangGraphAgenticAI application.
    This class uses TypedDict to define the structure of the state, which includes:
    - messages: A list of messages in the conversation.
    - graph: The current state of the graph.
    - user_inputs: A dictionary to store user inputs and selections.
    """

    messages: Annotated[list, add_messages]
    