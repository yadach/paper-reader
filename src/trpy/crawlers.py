"""Paper List Page Crawlers."""

import copy
import re
from abc import ABCMeta
from abc import abstractmethod
from pathlib import Path

import arxiv
import requests
import yaml
from bs4 import BeautifulSoup
from tqdm import tqdm

from trpy import llms


class BaseCrawler(metaclass=ABCMeta):
    def __init__(
        self,
        url: str,
        filter_op: dict,
        arxiv_op: dict,
        llm_op: dict,
    ) -> None:
        """BaseCrawler class.

        Args:
            url (str): URL of paper list.
            filter_op (dict): Filter options.
            arxiv_op (dict): arXiv options.
            llm_op (dict): LLM processing options.
        """
        self.url = url
        self.filter_op = filter_op
        self.arxiv_op = arxiv_op
        self.llm_op = llm_op
        self.paper_list_base = None
        self.paper_list = None

        self.arxiv_client = arxiv.Client()
        self._set_llm(llm_op)

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
        llm_op: dict | None = None,
    ) -> list[dict]:
        """Generate list of papers.

        Args:
            filter_op (dict | None, optional): Options of filter. Defaults to None.
            arxiv_op (dict | None, optional): Options of arxiv. Defaults to None.
            llm_op (dict | None, optional): Options of LLM processing. Defaults to None.

        Returns:
            list[dict]: List of paper information.
        """
        if filter_op is None:
            filter_op = self.filter_op
        if arxiv_op is None:
            arxiv_op = self.arxiv_op
        if llm_op is None:
            llm_op = self.llm_op
        paper_list = self.get_list()
        paper_list = self.filter(paper_list=paper_list, **filter_op)
        paper_list = self.add_arxiv_info(paper_list=paper_list, **arxiv_op)
        return self.llm_process(paper_list=paper_list, **llm_op)

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
            max_results=10,
            sort_by=arxiv.SortCriterion.Relevance,
        )
        for key in keys:
            arxived_info_dict[key] = ""
        for r in self.arxiv_client.results(search):
            if r.title == info_dict.get("title"):
                for key in keys:
                    val = getattr(r, key).replace("\n", " ")  # remove line breaks
                    arxived_info_dict[key] = val
                break
        return arxived_info_dict

    def llm_process(
        self,
        paper_list: list[dict],
        in_key: str | None = None,
        out_key: str | None = None,
        **kwargs: any,  # noqa: ARG002
    ) -> list[dict]:
        """Process paper list.

        Args:
            paper_list (list): List of paper information.
            in_key (str): Target key to be processed.
            out_key (str): Output key.
            kwargs (any): Other options.

        Returns:
            list: Translated list of paper information.
        """
        if in_key is None:
            return paper_list
        if out_key is None:
            out_key = f"{in_key}_llm"
        return self.llm.process(paper_list=paper_list, in_key=in_key, out_key=out_key)

    def _set_llm(self, llm_op: dict) -> None:
        if isinstance(llm_op.get("config"), str):
            with Path(llm_op.get("config")).open("rt") as file:
                llm_config = yaml.safe_load(file)
        else:
            llm_config = llm_op.get("config")
        self.llm = getattr(llms, llm_config.get("llm"))(**llm_config)


class CVPR2024Crawler(BaseCrawler):
    def __init__(
        self,
        url: str,
        filter_op: dict,
        arxiv_op: dict,
        llm_op: dict,
    ) -> None:
        """Crawler for CVPR2024.

        Args:
            url (str): URL of paper list.
            filter_op (dict): Filter options.
            arxiv_op (dict): arXiv options.
            llm_op (dict): LLM processing options.
        """
        super().__init__(
            url=url,
            filter_op=filter_op,
            arxiv_op=arxiv_op,
            llm_op=llm_op,
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
