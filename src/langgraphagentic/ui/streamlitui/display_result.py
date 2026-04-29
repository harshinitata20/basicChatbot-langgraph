import streamlit as st
from langchain_core.messages import HumanMessage


class DisplayResult:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display(self):
        with st.chat_message("assistant"):
            response = self.graph.invoke({"messages": [HumanMessage(content=self.user_message)]})
            ai_message = response["messages"][-1].content
            st.markdown(ai_message)
        return ai_message
