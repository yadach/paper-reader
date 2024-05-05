#!/usr/bin/env python3

"""Translate abstract of papers."""

from pathlib import Path

import yaml
from fire import Fire
from trpy import llms
from trpy.list_io import read_list
from trpy.list_io import write_list


def summarize_abstract(  # noqa: PLR0913
    list_file: str,
    in_key: str,
    out_key: str = "要約",
    prompt_conf: str = "confs/prompt/summarize_abstruct.yaml",
    output: str | None = None,
    drop_keys: list[str] | None = None,
) -> None:
    """Summarize abstract of papers.

    Args:
        list_file (str): Path to list file.
        in_key (str): Input key to be processed.
        out_key (str, optional): Output key. Defaults to "要約".
        prompt_conf (str, optional): Prompt config file. Defaults to "confs/prompt/summarize_abstruct.yaml".
        output (str | None, optional): Output file. Defaults to None.
        drop_keys (list[str] | None, optional): Drop keys. Defaults to None.
    """
    with Path(prompt_conf).open("rt") as file:
        config = yaml.safe_load(file)
    paper_list = read_list(list_file)
    llm = getattr(llms, config.get("llm"))(**config)
    translated_paper_list = llm.process(paper_list, in_key=in_key, out_key=out_key)
    if output is None:
        in_fmt = list_file.split(".")[-1]
        output = list_file.replace(in_fmt, "md")
    write_list(info_list=translated_paper_list, output=output, drop_keys=drop_keys)


def main() -> None:
    """Translate abstract in papers."""
    Fire(summarize_abstract)


if __name__ == "__main__":
    main()
