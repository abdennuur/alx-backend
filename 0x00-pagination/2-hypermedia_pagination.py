#!/usr/bin/env python3
"""Task 2
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """To retrieve index range from a given page and page size.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                rdr = csv.rdr(f)
                dataset = [row for row in rdr]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        strt, nd = index_range(page, page_size)
        data = self.dataset()
        if strt > len(data):
            return []
        return data[strt:nd]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieve information about  page.
        """
        data = self.get_page(page, page_size)
        strt, nd = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if nd < len(self.__dataset) else None,
            'prev_page': page - 1 if strt > 0 else None,
            'total_pages': total_pages
        }
