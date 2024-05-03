#!/usr/bin/env python3

"""Generate list of papers."""

import argparse

import yaml
from trpy import reader
from trpy.list_writer import write_list


def main(config: dict, output: str) -> None:
    """Ganerate list of papers.

    Args:
        config (dict): Path to config.
        output (str): Output path.
    """
    reader_class = getattr(reader, config.get("type"))
    page_reader = reader_class(**config)
    paper_list = page_reader.filter(**config.get("filter"))
    write_list(info_list=paper_list, output=output)


def get_arguments():
    # Make parser object
    parser = argparse.ArgumentParser(
        description=__doc__,
    )
    parser.add_argument(
        "--conf", type=str, default="confs/cvpr2024.yaml", help="Path to config file."
    )
    parser.add_argument(
        "--output", type=str, default="output.csv", help="Output file path."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_arguments()
    with open(args.conf) as file:
        config = yaml.safe_load(file)
    main(config, args.output)
