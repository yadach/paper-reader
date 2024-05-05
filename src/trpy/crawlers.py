"""Paper List Page Crawlers."""

import copy
import re
from abc import ABCMeta
from abc import abstractmethod

import arxiv
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from trpy import translators


class BaseCrawler(metaclass=ABCMeta):
    def __init__(
        self,
        url: str,
        filter_op: dict,
        arxiv_op: dict,
        translate_op: dict,
    ) -> None:
        """BaseCrawler class.

        Args:
            url (str): URL of paper list.
            filter_op (dict): Filter options.
            arxiv_op (dict): arXiv options.
            translate_op (dict): Translation options.
        """
        self.url = url
        self.filter_op = filter_op
        self.arxiv_op = arxiv_op
        self.translate_op = translate_op
        self.paper_list_base = None
        self.paper_list = None

        self.arxiv_client = arxiv.Client()
        self._set_translator(translate_op)

    @abstractmethod
    def get_list(self) -> list:
        """Get paper list.

        Returns
            list: List of paper information.
        """

    def generate_list(
        self,
        filter_op: dict | None = None,
        arxiv_op: dict | None = None,
        translate_op: dict | None = None,
    ) -> list[dict]:
        """Generate list of papers.

        Args:
            filter_op (dict | None, optional): Options of filter. Defaults to None.
            arxiv_op (dict | None, optional): Options of arxiv. Defaults to None.
            translate_op (dict | None, optional): Options of translation. Defaults to None.

        Returns:
            list[dict]: List of paper information.
        """
        if filter_op is None:
            filter_op = self.filter_op
        if arxiv_op is None:
            arxiv_op = self.arxiv_op
        if translate_op is None:
            translate_op = self.translate_op
        paper_list = self.get_list()
        paper_list = self.filter(paper_list=paper_list, **filter_op)
        paper_list = self.add_arxiv_info(paper_list=paper_list, **arxiv_op)
        return self.translate(paper_list=paper_list, **translate_op)

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

    def add_arxiv_info(self, paper_list: list[dict], keys: list, use: bool = True) -> list[dict]:
        """Add arXiv data.

        Args:
            paper_list (list[dict]): List of paper information.
            keys (list): Key to add in info.
            use (bool, optional): Use arXiv information. Defaults to True.

        Returns:
            list[dict]: List of paper information.s
        """
        if use:
            arxived_paper_list = [
                self._search_on_arxiv(paper_info, keys=keys)
                for paper_info in tqdm(paper_list, desc="Searching in arXiv")
            ]
            self.paper_list = arxived_paper_list
            return arxived_paper_list
        self.paper_list = paper_list
        return paper_list

    def _search_on_arxiv(self, info_dict: dict, keys: list | None = None) -> dict:
        if keys is None:
            keys = []
        arxived_info_dict = copy.deepcopy(info_dict)
        search = arxiv.Search(
            query=info_dict.get("title"),
            max_results=1,
            sort_by=arxiv.SortCriterion.Relevance,
        )
        for r in self.arxiv_client.results(search):
            for key in keys:
                val = getattr(r, key).replace("\n", " ")  # remove line breaks
                arxived_info_dict[key] = val if r.title == info_dict.get("title") else ""
        return arxived_info_dict

    def translate(
        self,
        paper_list: list[dict],
        keys: list[str] | None = None,
        translator: str | None = None,
        options: dict | None = None,
    ) -> list[dict]:
        """Translate information.

        Args:
            paper_list (list[dict]): List of paper information.
            keys (list[str] | None, optional): Key to translate. Defaults to None.
            translator (str): API to translator. Defaults to None.
            options (dict): Translator options. Defaults to None.

        Returns:
            list[dict]: Translated list of paper information.
        """
        if keys is None:
            keys = []
        if translator is not None:
            self._set_translator(translate_op={"translator": translator, "options": options})
        return self.translator.translate(paper_list=paper_list, keys=keys)

    def _set_translator(self, translate_op: dict) -> None:
        self.translator = getattr(translators, translate_op.get("translator"))(**translate_op.get("options"))


class CVPR2024Crawler(BaseCrawler):
    def __init__(
        self,
        url: str,
        filter_op: dict,
        arxiv_op: dict,
        translate_op: dict,
    ) -> None:
        """Crawler class for CVPR2024.

        Args:
            url (str): URL of paper list.
            filter_op (dict): Filter options.
            arxiv_op (dict): arXiv options.
            translate_op (dict): Translation options.
        """
        super().__init__(
            url=url,
            filter_op=filter_op,
            arxiv_op=arxiv_op,
            translate_op=translate_op,
        )

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
