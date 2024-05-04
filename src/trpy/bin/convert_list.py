#!/usr/bin/env python3

"""Convert list of papers."""

from fire import Fire
from trpy.list_io import read_list
from trpy.list_io import write_list


def convert_list(list_file: str, output: str = "converted_list.md") -> None:
    """Convert list of papers.

    Args:
        list_file (str): Path to list file.
        output (str): Output path.
    """
    info_list = read_list(list_file)
    write_list(info_list=info_list, output=output, drop_keys=["summary", "pdf_url"])


def main() -> None:
    """Convert list of papers."""
    Fire(convert_list)


if __name__ == "__main__":
    main()
