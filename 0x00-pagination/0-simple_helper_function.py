#!/usr/bin/env python3
"""THE Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """te Retrieve the index range from given page and page size.
    """
    strt = (page - 1) * page_size
    nd = strt + page_size
    return (strt, nd)
