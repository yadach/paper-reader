"""Summarization modules."""

import os
from abc import ABCMeta
from abc import abstractmethod

from openai import OpenAI
from tqdm import tqdm


class BaseLLM(metaclass=ABCMeta):
    def __init__(self) -> None:
        """Initialize translator."""
        self.name = "BaseTranslator"

    def process(self, paper_list: list, in_key: str, out_key: str) -> list:
        """Translate paper list.

        Args:
            paper_list (list): List of paper information.
            in_key (str): Target key to be processed.
            out_key (str): Output key.

        Returns:
            list: Translated list of paper information.
        """
        if in_key is None:
            return paper_list
        if out_key is None:
            out_key = f"{in_key}_llm"
        for paper_info in tqdm(paper_list, desc="LLM processing"):
            paper_info[out_key] = self._process(paper_info[in_key]) if paper_info[in_key] != "" else ""
        return paper_list

    @abstractmethod
    def _process(self, text: str) -> str:
        """Translate text by using some APIs.

        Args:
            text (str): Input text to be processed.

        Returns:
            str: Translated text.
        """


class ChatGPT(BaseLLM):
    def __init__(
        self,
        prompt: dict,
        llm: str = "OpenAISummarizer",
        params: dict | None = None,
    ) -> None:
        """Bot with OpenAI API.

        Args:
            prompt (dict): Prompt.
            params (str, optional): Model name. Defaults to {"model": "gpt-3.5-turbo"}.
            llm (str): Name of LLM.
        """
        if params is None:
            params = {"model": "gpt-3.5-turbo"}
        super().__init__()
        self.name = llm
        self.prompt = prompt
        assert os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI()
        self.model = params.get("model")

    def _process(self, text: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                self.prompt,
                {
                    "role": "user",
                    "content": text,
                },
            ],
        )
        return completion.choices[0].message.content
