"""Module to read and write list."""

import csv
import json
from pathlib import Path

SUPPORTED_FORMAT = ["csv", "json", "md"]


def read_list(list_file: str) -> list[dict]:
    """Read list file.

    Args:
        list_file (str): List file path.

    Returns:
        list[dict]: List of infomation dict.
    """
    list_fmt = list_file.split(".")[-1]
    assert list_fmt in SUPPORTED_FORMAT
    with Path(list_file).open("rt") as file:
        if list_fmt == "csv":
            reader = csv.DictReader(file)
            dict_list = list(reader)
        elif list_fmt == "json":
            dict_list = json.load(file)
        elif list_fmt == "md":
            msg = f"{list_file} is not supported format to read, only to write."
            raise NameError(msg)
    return dict_list


def write_list(info_list: list, output: str, index_key: str = "title", drop_keys: list[str] | None = None) -> None:
    """Write list of infomation.

    Args:
        info_list (list): List of info.
        output (str): Output path(csv or json file).
        index_key (str, optional): Key to be the title in md file. Defaults to "title".
        drop_keys (list[str] | None, optional): Drop keys in md file. Defaults to ["pdf_url"].
    """
    out_fmt = output.split(".")[-1]
    assert out_fmt in SUPPORTED_FORMAT
    with Path(output).open("wt", encoding="utf-8") as file:
        if out_fmt == "csv":
            writer = csv.writer(file)
            for i, info in enumerate(info_list):
                if i == 0:
                    columns = list(info.keys())
                    writer.writerow(columns)
                rows = [info.get(key, "") for key in columns]
                writer.writerow(rows)
        elif out_fmt == "json":
            json.dump(info_list, file, indent=4, ensure_ascii=False)
        elif out_fmt == "md":
            if drop_keys is None:
                drop_keys = []
            md_txt = ""
            for info in info_list:
                md_txt += f"### {info[index_key]}\n"
                for key, val in info.items():
                    if key in [index_key, *drop_keys] or val == "":
                        continue
                    md_txt += f"- {key}: {val}\n"
            file.write(md_txt)
