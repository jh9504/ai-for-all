import os

from dotenv import load_dotenv

from doctor_assistant.app.generator.gpt3 import GptGenerator
from doctor_assistant.app.generator.prompts.summarize import SUMMARIZATION_PROMPT

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

doctor = GptGenerator(api_key=api_key)


def summarize(symptom: str, example_format: str):
    prompt = SUMMARIZATION_PROMPT.format(symptom=symptom, example_format=example_format)
    summary = doctor.generate(prompt=prompt)
    return summary
