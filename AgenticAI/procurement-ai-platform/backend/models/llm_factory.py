from backend.models.openrouter import OpenRouterLLM


class LLMFactory:

    @staticmethod
    def get():
        return OpenRouterLLM()