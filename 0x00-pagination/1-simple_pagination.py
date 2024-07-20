#!/usr/bin/env python3
"""THE Simple pagination sample.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """TO Retrieve index range from  given page and page size.
    """
    strt = (page - 1) * page_size
    nd = strt + page_size
    return (strt, nd)


class Server:
    """The server class to paginate a database of a popular baby names.
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
                rdr = csv.reader(f)
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
