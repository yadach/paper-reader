#!/usr/bin/env python3

"""Generate list of papers."""

import argparse

import yaml
from fire import Fire
from trpy import reader
from trpy.list_writer import write_list


def generate_paper_list(conf_file: str, output: str = "paper_list.csv") -> None:
    """Ganerate list of papers.

    Args:
        conf_file (str): Path to config.
        output (str): Output path.
    """
    with open(conf_file) as file:
        config = yaml.safe_load(file)
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
        "--output", type=str, default="paper_list.csv", help="Output file path."
    )
    return parser.parse_args()


def main():
    Fire(generate_paper_list)


if __name__ == "__main__":
    args = get_arguments()
    generate_paper_list(args.conf, args.output)
