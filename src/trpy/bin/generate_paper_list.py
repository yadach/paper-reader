#!/usr/bin/env python3

"""Generate list of papers."""

from pathlib import Path

import yaml
from fire import Fire
from trpy import readers
from trpy.list_writer import write_list


def generate_paper_list(conf_file: str, output: str = "paper_list.csv") -> None:
    """Ganerate list of papers.

    Args:
        conf_file (str): Path to config.
        output (str): Output path.
    """
    with Path(conf_file).open("rt") as file:
        config = yaml.safe_load(file)
    reader_class = getattr(readers, config.get("type"))
    page_reader = reader_class(**config)
    paper_list = page_reader.filter(**config.get("filter"))
    write_list(info_list=paper_list, output=output)


def main() -> None:
    """Ganerate list of papers."""
    Fire(generate_paper_list)


if __name__ == "__main__":
    main()
