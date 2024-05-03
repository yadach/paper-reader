import re
from abc import ABCMeta
from abc import abstractmethod
from typing import Any

import requests
from bs4 import BeautifulSoup


class BaseReader(metaclass=ABCMeta):
    def __init__(
        self,
        url: str,
        **kwargs: dict[str, Any],
    ) -> None:
        self.url = url
        self.paper_list = None

    @abstractmethod
    def get_list(self) -> list:
        """Get paper list.

        Returns:
            list: List of paper information.
        """
        pass

    def filter(self, target: str, keyword: str) -> dict:
        if self.paper_list is None:
            self.paper_list = self.get_list()
        filtered_list = []
        for paper_info in self.paper_list:
            if keyword in paper_info.get(target, ""):
                filtered_list += [paper_info]

        return filtered_list


class CVPR2024Reader(BaseReader):
    def __init__(
        self,
        url: str,
        **kwargs: dict[str, Any],
    ) -> None:
        super().__init__(url=url, **kwargs)
        self.url = url

    def get_list(self) -> list:
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, "html.parser")
        table = soup.find("table")
        contents = table.find_all("tr")
        paper_list = []
        for info in contents:
            title = info.find("strong")
            if title is None:
                title = info.find("a")
            if title is None:
                continue
            authers = info.find("i").string.split("\n")[2]
            authers = re.sub(" +", " ", authers)[1:]
            paper_info = {
                "title": title.string,
                "authers": authers,
                "url": title.attrs.get("href", ""),
            }
            paper_list += [paper_info]
        self.paper_list = paper_list
        return paper_list
