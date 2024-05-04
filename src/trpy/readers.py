"""Paper List Page Crawlers."""

import re
from abc import ABCMeta
from abc import abstractmethod

import requests
from bs4 import BeautifulSoup


class BaseReader(metaclass=ABCMeta):
    def __init__(
        self,
        url: str,
    ) -> None:
        """Reader class.

        Args:
            url (str): URL of paper list.
        """
        self.url = url
        self.paper_list = None

    @abstractmethod
    def get_list(self) -> list:
        """Get paper list.

        Returns
            list: List of paper information.
        """

    def filter(self, target: str, keyword: str) -> dict:
        """Filter list.

        Args:
            target (str): Key to search.
            keyword (str): Keywords to be searched.

        Returns:
            dict: _description_
        """
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
    ) -> None:
        """Reader class for CVPR2024.

        Args:
            url (str): URL of paper list.
        """
        super().__init__(url=url)
        self.url = url

    def get_list(self) -> list:
        """Get list of papers.

        Returns
            list: List of paper information.
        """
        res = requests.get(self.url, timeout=10)
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
