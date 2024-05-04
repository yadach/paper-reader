#!/usr/bin/env python3

"""Translate abstract of papers."""

from fire import Fire
from trpy import translators
from trpy.list_io import read_list
from trpy.list_io import write_list


def translate_abstract(
    list_file: str,
    output: str = "translated_list.csv",
    keys: list | None = None,
    translator: str = "OpenAITranslator",
    translator_params: dict | None = None,
) -> None:
    """Translate abstract in papers.

    Args:
        list_file (str): List file of papers.
        output (str, optional): Output path. Defaults to "translated_list.csv".
        keys (list | None, optional): Target keys to translate. Defaults to ["summary"].
        translator (str, optional): API for translation. Defaults to "OpenAITranslator".
        translator_params (dict | None, optional): Options of the API. Defaults to None.
    """
    if translator_params is None:
        translator_params = {"model": "gpt-3.5-turbo"}
    if keys is None:
        keys = ["summary"]
    paper_list = read_list(list_file)
    translator = getattr(translators, translator)(**translator_params)
    translated_paper_list = translator.translate(paper_list, keys=keys)
    write_list(info_list=translated_paper_list, output=output)


def main() -> None:
    """Translate abstract in papers."""
    Fire(translate_abstract)


if __name__ == "__main__":
    main()
