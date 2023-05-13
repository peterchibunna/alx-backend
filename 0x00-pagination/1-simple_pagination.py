import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Documentation:
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start_index = page_size * (page - 1)
    end_index = page_size * page
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
        start_index = page_size * (page - 1)
        end_index = page_size * page
        if type(page) == int and type(page_size) == int and page > 0 and \
                page_size > 0:
            start, end = index_range(page, page_size)
            data = self.dataset()
            if start > len(data):
                return []
            return data[start:end]
        raise AssertionError
