#!/usr/bin/env python3

"""Generate list of papers."""

from pathlib import Path

import yaml
from fire import Fire
from trpy import crawlers
from trpy.list_io import write_list


def generate_paper_list(conf_file: str, output: str = "paper_list.csv", use_arxiv: bool = True) -> None:
    """Ganerate list of papers.

    Args:
        conf_file (str): Path to config.
        output (str): Output path.
        use_arxiv (bool): Add arXiv data. Defaults to True.
    """
    with Path(conf_file).open("rt") as file:
        config = yaml.safe_load(file)
    crawler = getattr(crawlers, config.get("type"))
    page_reader = crawler(url=config.get("url"))
    paper_list = page_reader.generate_list(
        filter_options=config.get("filter"),
        use_arxiv=use_arxiv,
    )
    write_list(info_list=paper_list, output=output)


def main() -> None:
    """Ganerate list of papers."""
    Fire(generate_paper_list)


if __name__ == "__main__":
    main()
