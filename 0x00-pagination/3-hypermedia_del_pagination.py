#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Implementing a method that returns a dict with the following
        key-value pairs:
        index: the current start
        """
        items = self.indexed_dataset()
        index = index if index else 0
        assert index is not None
        assert len(items.items()) > index >= 0
        assert index + page_size < len(items.items())

        data = []

        page_index = index  # * page_size
        next_index = None
        data_size = 0
        for i, item in items.items():
            if i >= index and data_size < page_size:
                data.append(item)
                data_size += 1
                continue
            if data_size == page_size:
                next_index = i
                break

        return dict(
            index=page_index,
            data=data,
            page_size=page_size,
            next_index=next_index,
        )
