#!/usr/bin/env python3

"""Script for searching papers."""

import csv
from pathlib import Path

import arxiv
from fire import Fire
from tqdm import tqdm
from trpy.list_writer import write_list


def search_on_arxiv(
    list_file: str,
    output: str = "arxiv_list.csv",
    keys: list | None = None,
) -> None:
    """Search paper and add information from arXiv.

    Args:
        list_file (str): List file of papers.
        output (str, optional): Output path. Defaults to "arxiv_list.csv".
        keys (list, optional): Keys of target. Defaults to ["entry_id", "pdf_url", "summary"].
    """
    if keys is None:
        keys = ["entry_id", "pdf_url", "summary"]
    with Path(list_file).open("rt") as file:
        reader = csv.DictReader(file)
        paper_list = list(reader)

    client = arxiv.Client()
    for paper_info in tqdm(paper_list):
        search = arxiv.Search(
            query=paper_info.get("title"),
            max_results=1,
            sort_by=arxiv.SortCriterion.Relevance,
        )
        for r in client.results(search):
            for key in keys:
                val = getattr(r, key).replace("\n", " ")  # remove line breaks
                paper_info[key] = val if r.title == paper_info.get("title") else ""
    write_list(info_list=paper_list, output=output)


def main() -> None:
    """Search paper and add information from arXiv."""
    Fire(search_on_arxiv)


if __name__ == "__main__":
    main()
