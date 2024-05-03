import csv
import json


def write_list(info_list: list, output: str) -> None:
    """Write list of infomation.

    Args:
        info_list (list): List of info.
        output (str): Output path(csv or json file).
    """
    with open(output, "wt", encoding="utf-8") as file:
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
            raise NameError(
                f"{output} is not supported format, only support .csv and .json format."
            )
    print("hoge")
