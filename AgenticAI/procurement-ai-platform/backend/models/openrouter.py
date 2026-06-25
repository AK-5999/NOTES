from langchain_openai import ChatOpenAI

from backend.core.config import settings
from backend.models.base import BaseLLM


class OpenRouterLLM(BaseLLM):

    def __init__(self):
        self.llm = ChatOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.OPENROUTER_API_KEY,
            model=settings.OPENROUTER_MODEL,
            temperature=0,
        )

    async def invoke(self, prompt: str):
        response = await self.llm.ainvoke(prompt)
        return response.content