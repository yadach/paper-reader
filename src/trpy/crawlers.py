"""Paper List Page Crawlers."""

import copy
import re
from abc import ABCMeta
from abc import abstractmethod

import arxiv
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class BaseCrawler(metaclass=ABCMeta):
    def __init__(
        self,
        url: str,
    ) -> None:
        """Reader class.

        Args:
            url (str): URL of paper list.
        """
        self.url = url
        self.paper_list_base = None
        self.paper_list = None
        self.arxiv_client = arxiv.Client()
        self.arxiv_keys = ["entry_id", "pdf_url", "summary"]

    @abstractmethod
    def get_list(self) -> list:
        """Get paper list.

        Returns
            list: List of paper information.
        """

    def generate_list(self, filter_options: dict, use_arxiv: bool = True) -> list[dict]:
        """Generate list of papers.

        Args:
            filter_options (dict): Options of filter. egs. {"target": "title", "keyword": "Detection"}
            use_arxiv (bool, optional): Add arXiv data. Defaults to True.

        Returns:
            list[dict]: List of paper information.
        """
        paper_list = self.get_list()
        paper_list = self.filter(paper_list=paper_list, **filter_options)
        return self.add_arxiv_info(paper_list=paper_list) if use_arxiv else paper_list

    def filter(self, paper_list: list[dict], target: str, keyword: str) -> list[dict]:
        """Filter list.

        Args:
            paper_list (list[dict]): List of paper information.
            target (str): Key to search.
            keyword (str): Keywords to be searched.

        Returns:
            list[dict]: Filterd list of information dict.
        """
        filtered_paper_list = []
        for paper_info in paper_list:
            if keyword in paper_info.get(target, ""):
                filtered_paper_list += [paper_info]
        self.paper_list = filtered_paper_list
        return filtered_paper_list

    def add_arxiv_info(self, paper_list: list[dict]) -> list[dict]:
        """Add arXiv data.

        Args:
            paper_list (list[dict]): List of paper information.

        Returns:
            list[dict]: Updated list of paper information.
        """
        arxived_paper_list = [
            self._search_on_arxiv(paper_info) for paper_info in tqdm(paper_list, desc="Searching in arXiv")
        ]
        self.paper_list = arxived_paper_list
        return arxived_paper_list

    def _search_on_arxiv(self, info_dict: dict) -> dict:
        arxived_info_dict = copy.deepcopy(info_dict)
        search = arxiv.Search(
            query=info_dict.get("title"),
            max_results=1,
            sort_by=arxiv.SortCriterion.Relevance,
        )
        for r in self.arxiv_client.results(search):
            for key in self.arxiv_keys:
                val = getattr(r, key).replace("\n", " ")  # remove line breaks
                arxived_info_dict[key] = val if r.title == info_dict.get("title") else ""
        return arxived_info_dict


class CVPR2024Crawler(BaseCrawler):
    def __init__(
        self,
        url: str,
    ) -> None:
        """Reader class for CVPR2024.

        Args:
            url (str): URL of paper list.
        """
        super().__init__(url=url)

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
        self.paper_list_base = paper_list
        self.paper_list = paper_list
        return paper_list
