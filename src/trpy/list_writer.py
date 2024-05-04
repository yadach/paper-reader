"""Module for writing list."""

import csv
import json
from pathlib import Path


def write_list(info_list: list, output: str) -> None:
    """Write list of infomation.

    Args:
        info_list (list): List of info.
        output (str): Output path(csv or json file).
    """
    with Path(output).open("wt", encoding="utf-8") as file:
        if output.endswith("csv"):
            writer = csv.writer(file)
            for i, info in enumerate(info_list):
                if i == 0:
                    columns = list(info.keys())
                    writer.writerow(columns)
                rows = [info.get(key, "") for key in columns]
                writer.writerow(rows)
        elif output.endswith("json"):
            json.dump(info_list, file, indent=4, ensure_ascii=False)
        else:
            msg = f"{output} is not supported format, only support .csv and .json format."
            raise NameError(msg)
