import streamlit as st
from src.langgraphagentic.ui.uiconfig import UIConfig


class LoadStreamlitUI:
    def __init__(self):
        self.config = UIConfig()
        self.user_controls = {}

    def load_streamlitui(self):
        st.set_page_config(page_title=self.config.get_page_title(), page_icon="🤖", layout="wide")
        st.header(self.config.get_header())

        with st.sidebar:
            llm_options = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_option()

            self.user_controls['llm_choice'] = st.selectbox("Select LLM", llm_options)
            self.user_controls['usecase_choice'] = st.selectbox("Select Use Case", usecase_options)

            if self.user_controls['llm_choice'] == "Groq":
                if self.user_controls['usecase_choice'] == "Chatbot with Web Search":
                    model_options = self.config.get_groq_tool_compatible_models()
                else:
                    model_options = self.config.get_groq_model_option()
                self.user_controls['model_choice'] = st.selectbox("Select Groq Model", model_options)
                self.user_controls['groq_api_key'] = st.text_input("Enter Groq API Key", key="groq_api_key", type="password")

            if self.user_controls['usecase_choice'] in ("Chatbot with Web Search", "AI News Summarizer"):
                self.user_controls["TAVILY API KEY"] = st.text_input("Enter TAVILY API Key", key="tavily_api_key", type="password")

            if self.user_controls['usecase_choice'] == "AI News Summarizer":
                st.subheader("AI News Explorer")
                st.selectbox(
                    "Select Time Frame",
                    ["Last 24 hours", "Last 7 days", "Last 30 days"],
                    key="news_time_frame",
                )
                if st.button("Fetch latest AI News", use_container_width=True):
                    st.session_state["fetch_news"] = True

        return self.user_controls
