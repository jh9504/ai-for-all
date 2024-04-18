from openai import AsyncOpenAI
from openai import OpenAI

from doctor_assistant.app.generator.base import BaseGenerator


class GptGenerator(BaseGenerator):
    model = "gpt-3.5-turbo"
    api_key = ""

    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key
        
        self.client = OpenAI(
            api_key=self.api_key,
        )

        self.async_client = AsyncOpenAI(
            api_key=self.api_key,
        )
