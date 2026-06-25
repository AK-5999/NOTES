from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    async def invoke(self, prompt: str):
        pass