#!/usr/bin/env python3
"""
Module: 2. Hypermedia pagination
"""
import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """Documentation:
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start_index = page_size * (page - 1)
    end_index = page_size + start_index
    return start_index, end_index


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
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implement a simple pagination of data
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index > len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Implement a Hypermedia pagination of data
        """
        try:
            dataset_size = len(self.dataset())
        except TypeError:
            dataset_size = 0
        data = self.get_page(page, page_size)
        start_index, end_index = index_range(page=page, page_size=page_size)
        total_pages = math.ceil(dataset_size / page_size)
        next_page = page + 1 if end_index < total_pages else None
        prev_page = page - 1 if start_index > 0 else None
        return dict(
            page_size=len(data),
            page=page,
            data=data,
            next_page=next_page,
            prev_page=prev_page,
            total_pages=total_pages
        )
