"""Translator modules."""

import os
from abc import ABCMeta
from abc import abstractmethod

from openai import OpenAI
from tqdm import tqdm


class BaseTranslator(metaclass=ABCMeta):
    def __init__(self) -> None:
        """Initialize translator."""
        self.name = "BaseTranslator"

    def translate(self, paper_list: list, keys: list) -> list:
        """Translate paper list.

        Args:
            paper_list (list): List of paper information.
            keys (list): Target keys to translate.

        Returns:
            list: Translated list of paper information.
        """
        for paper_info in tqdm(paper_list):
            for key in keys:
                paper_info[f"{key}_ja"] = self._translate(paper_info[key]) if paper_info[key] != "" else ""
        return paper_list

    @abstractmethod
    def _translate(self, text: str) -> str:
        """Translate text by using some APIs.

        Args:
            text (str): Input text to translate.

        Returns:
            str: Translated text.
        """


class OpenAITranslator(BaseTranslator):
    def __init__(self, model: str = "gpt-3.5-turbo") -> None:
        """Translate with OpenAI API.

        Args:
            model (str, optional): Model name. Defaults to "gpt-3.5-turbo".
        """
        super().__init__()
        self.name = "OpenAITranslator"
        assert os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI()
        self.model = model

    def _translate(self, text: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional translator. Translate the user's English input into Japanese.",
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
        )
        return completion.choices[0].message.content
