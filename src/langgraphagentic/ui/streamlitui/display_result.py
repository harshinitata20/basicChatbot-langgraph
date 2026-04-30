import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


class DisplayResult:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display(self):
        if self.usecase == "Basic Chatbot":
            with st.chat_message("assistant"):
                response = self.graph.invoke({"messages": [HumanMessage(content=self.user_message)]})
                ai_message = response["messages"][-1].content
                st.markdown(ai_message)
            return ai_message

        elif self.usecase == "Chatbot with Web Search":
            ai_message = ""
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = self.graph.invoke({"messages": [HumanMessage(content=self.user_message)]})

                for msg in response["messages"]:
                    if isinstance(msg, AIMessage) and msg.tool_calls:
                        tool_names = [tc["name"] for tc in msg.tool_calls]
                        st.info(f"Tools called: {', '.join(tool_names)}")
                    elif isinstance(msg, ToolMessage):
                        with st.expander("Tool result"):
                            st.markdown(msg.content)

                final_msg = next(
                    (m for m in reversed(response["messages"]) if isinstance(m, AIMessage) and m.content),
                    None,
                )
                if final_msg:
                    ai_message = final_msg.content
                    st.markdown(ai_message)

            return ai_message
