#!/usr/bin/env python3
"""The deletion-resilient hypermedia pagination
"""
import csv
from typing import Dict, List


class Server:
    """The erver class to paginate database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """The initialize new Server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """The cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as ff:
                reader = csv.reader(ff)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """The dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """To retrieve info about a page frm a given index and with a
        specified size.
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        page_data = []
        data_cnt = 0
        next_index = None
        start = index if index else 0
        for ix, item in data.items():
            if ix >= start and data_cnt < page_size:
                page_data.append(item)
                data_cnt += 1
                continue
            if data_cnt == page_size:
                next_index = ix
                break
        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
        return page_info
