#!/usr/bin/env python3
"""
Module: 0. Simple helper function
"""


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
