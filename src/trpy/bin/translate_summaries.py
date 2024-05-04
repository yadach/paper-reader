#!/usr/bin/env python3

# Translate abstract of papers.

import csv

from fire import Fire
from trpy import translators
from trpy.list_writer import write_list


def translate_abstract(
    list_file: str,
    output: str = "translated_list.csv",
    keys: list = ["summary"],
    translator: str = "OpenAITranslator",
    translator_params: dict = {"model": "gpt-3.5-turbo"},
) -> None:
    with open(list_file, "rt") as file:
        reader = csv.DictReader(file)
        paper_list = [row_dict for row_dict in reader]
    translator = getattr(translators, translator)(**translator_params)
    translated_paper_list = translator.translate(paper_list, keys=keys)
    write_list(info_list=translated_paper_list, output=output)


def main():
    Fire(translate_abstract)


if __name__ == "__main__":
    main()
