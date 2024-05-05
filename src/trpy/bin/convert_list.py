#!/usr/bin/env python3

"""Convert list of papers."""

from fire import Fire
from trpy.list_io import read_list
from trpy.list_io import write_list


def convert_list(list_file: str, output: str, drop_keys: list[dict] | None = None) -> None:
    """Convert list of papers.

    Args:
        list_file (str): Path to list file.
        output (str): Output path.
        drop_keys (list[dict] | None, optional): Drop keys. Defaults to [].
    """
    if drop_keys is None:
        drop_keys = []
    info_list = read_list(list_file)
    write_list(info_list=info_list, output=output, drop_keys=drop_keys)


def convert_to_md(list_file: str, drop_keys: list[dict] | None = None) -> None:
    """Convert list to markdown format.

    Args:
        list_file (str): Path to list file.
        drop_keys (list[dict] | None, optional): Drop keys. Defaults to ["summary", "pdf_url"].
    """
    if drop_keys is None:
        drop_keys = ["summary", "pdf_url"]
    in_fmt = list_file.split(".")[-1]
    output = in_fmt.replace(in_fmt, "md")
    convert_list(list_file=list_file, output=output, drop_keys=drop_keys)


def main() -> None:
    """Convert list of papers."""
    Fire(convert_list)


def conv2md() -> None:
    """Convert list to markdown format."""
    Fire(convert_to_md)


if __name__ == "__main__":
    main()
