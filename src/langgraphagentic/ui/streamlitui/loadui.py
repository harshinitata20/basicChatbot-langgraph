import streamlit as st
import os
from src.langgraphagentic.ui.uiconfig import UIConfig

class LoadStreamlitUI:
    def __init__(self):
        self.config = UIConfig()
        self.user_controls={}

    def load_streamlitui(self):
        st.set_page_config(page_title=self.config.get_page_title(), page_icon="🤖", layout="wide")
        st.header(self.config.get_header())

        with st.sidebar:
            llm_options = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_option()

            self.user_controls['llm_choice'] = st.selectbox("Select LLM", llm_options)

            if self.user_controls['llm_choice'] == "Groq":
                model_options = self.config.get_groq_model_option()
                self.user_controls['model_choice'] = st.selectbox("Select Groq Model", model_options)
                self.user_controls['groq_api_key'] = st.text_input("Enter Groq API Key", key="groq_api_key", type="password")

            self.user_controls['usecase_choice'] = st.selectbox("Select Use Case", usecase_options)

        return self.user_controls