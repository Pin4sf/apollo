import logging
import os

from openai import OpenAI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
)

class GPT3Turbo:
    def __init__(self, open_api_key: str = OPENAI_API_KEY):
        self.model_name = "gpt-3.5-turbo"
        self.api_key = open_api_key
        self.client = OpenAI(api_key=open_api_key)
        logger.info(f"OpenAI {self.model_name} client loaded.")

    def generate(self, messages: list, max_tokens: int = 256) -> str:
        """
        Generates a completion from the GPT-3.5 Turbo model
        :param messages: A list of message objects for conversation format
        :param max_tokens: Maximum number of tokens in the completion
        :return: The stripped content of the completion generated by the GPT-3.5 Turbo model
        """
        try:
            logger.info("Generating")
            response = self.client.chat.completions.create(
                messages=messages,
                model="gpt-3.5-turbo",
                temperature=0,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            error_message = f"An error occurred during GPT-3.5 Turbo completion: {e}"
            logger.error(error_message)
            raise Exception(status_code=500, detail=error_message)
