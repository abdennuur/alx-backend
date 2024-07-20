#!/usr/bin/env python3
"""The hypermedia pagination sample.
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """To retrieve index range frm a given page and page size.
    """
    strt = (page - 1) * page_size
    nd = strt + page_size
    return (strt, nd)


class Server:
    """the Server class to paginate database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """To initializes new Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """The cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                rdr = csv.rdr(f)
                dataset = [row for row in rdr]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """To retrieve a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        strt, nd = index_range(page, page_size)
        data = self.dataset()
        if strt > len(data):
            return []
        return data[strt:nd]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """to retrieve information about a page.
        """
        page_data = self.get_page(page, page_size)
        strt, nd = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if nd < len(self.__dataset) else None,
            'prev_page': page - 1 if strt > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
