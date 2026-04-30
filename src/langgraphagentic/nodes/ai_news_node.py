from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage


class AINewsNode:
    def __init__(self, llm):
        self.tavily = TavilyClient()
        self.llm = llm
        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        frequency = state["messages"][0].content.lower()
        self.state["frequency"] = frequency

        days_map = {"last 24 hours": 1, "last 7 days": 7, "last 30 days": 30}

        response = self.tavily.search(
            query="Top Artificial Intelligence news in India and across the globe",
            topic="news",
            days=days_map.get(frequency, 7),
            include_answer="advanced",
            max_results=10,
        )

        self.state["news_data"] = response.get("results", [])[:5]
        return state

    def summarize_news(self, state: dict) -> dict:
        news_items = self.state["news_data"]

        prompt_template = ChatPromptTemplate.from_messages([
            ("system",
             "You are a helpful assistant that summarizes news articles. "
             "For each news item provide:\n"
             "- A brief headline\n"
             "- A concise summary of the main points\n"
             "- A link to the original article\n"
             "- The date of publication\n"
             "- The news source name"),
            ("user", "Summarize the following news articles: {news_items}")
        ])

        chain = prompt_template | self.llm
        response = chain.invoke({"news_items": news_items})
        self.state["summary"] = response.content
        return state

    def save_results(self, state: dict) -> dict:
        frequency = self.state.get("frequency", "unknown")
        summary = self.state.get("summary", "No summary available.")
        file_name = f"ai_news_summary_{frequency.replace(' ', '_')}.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(summary)
        state["messages"] = [AIMessage(content=summary)]
        return state
