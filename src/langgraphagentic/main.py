import os
import streamlit as st

from src.langgraphagentic.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagentic.llms.groqllm import GroqLLM
from src.langgraphagentic.graph.graph_builder import GraphBuilder
from src.langgraphagentic.ui.streamlitui.display_result import DisplayResult


def load_langgraph_agenticai_app():
    ui = LoadStreamlitUI()
    user_inputs = ui.load_streamlitui()

    if not user_inputs:
        st.error("Failed to capture user inputs. Please try again.")
        return

    usecase = user_inputs.get('usecase_choice', '')

    if usecase == "AI News Summarizer":
        if st.session_state.get("fetch_news"):
            st.session_state["fetch_news"] = False
            time_frame = st.session_state.get("news_time_frame", "Last 7 days")

            tavily_key = user_inputs.get("TAVILY API KEY", "")
            if not tavily_key:
                st.error("Tavily API key is required. Please enter it in the sidebar.")
                return
            os.environ["TAVILY_API_KEY"] = tavily_key

            try:
                obj_llm_config = GroqLLM(user_controls_input=user_inputs)
                model = obj_llm_config.get_llm_model()
                if not model:
                    st.error("Failed to initialize the LLM model. Please check your API key and model selection.")
                    return

                graph_builder = GraphBuilder(model=model)
                graph = graph_builder.setup_graph(usecase=usecase)
                DisplayResult(usecase, graph, time_frame).display()
            except Exception as e:
                st.error(f"Error fetching news: {str(e)}")
        return

    # Chatbot use cases
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_message = st.chat_input("Enter your message here:")
    if user_message:
        with st.chat_message("user"):
            st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

        try:
            obj_llm_config = GroqLLM(user_controls_input=user_inputs)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Failed to initialize the LLM model. Please check your API key and model selection.")
                return

            if not usecase:
                st.error("No use case selected. Please select a use case from the sidebar.")
                return

            if usecase == "Chatbot with Web Search":
                tavily_key = user_inputs.get("TAVILY API KEY", "")
                if not tavily_key:
                    st.error("Tavily API key is required for web search. Please enter it in the sidebar.")
                    return
                os.environ["TAVILY_API_KEY"] = tavily_key

            graph_builder = GraphBuilder(model=model)
            try:
                graph = graph_builder.setup_graph(usecase=usecase)
                ai_response = DisplayResult(usecase, graph, user_message).display()
                if ai_response:
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})
            except Exception as e:
                st.error(f"Graph error: {str(e)}")
                return
        except Exception as e:
            st.error(f"LLM error: {str(e)}")
            return
