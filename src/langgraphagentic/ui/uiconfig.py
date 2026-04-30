from configparser import ConfigParser
import os

class UIConfig:
    def __init__(self):
        self.config = ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), "uiconfig.ini")
        self.config.read(config_path)

    def get_llm_option(self):
        return [x.strip() for x in self.config["DEFAULT"].get("LLM_OPTION", "Groq").split(",")]

    def get_usecase_option(self):
        return [x.strip() for x in self.config["DEFAULT"].get("USECASE_OPTIONS", "Basic Chatbot").split(",")]

    def get_groq_model_option(self):
        return [x.strip() for x in self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS", "llama3-8b-8192").split(",")]

    def get_groq_tool_compatible_models(self):
        return [x.strip() for x in self.config["DEFAULT"].get("GROQ_TOOL_COMPATIBLE_MODELS", "llama-3.1-8b-instant").split(",")]

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "LangGraphAgentic")

    def get_header(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "LangGraphAgentic")
    
