#!/usr/bin/env python3

'''
2. Hypermedia pagination
'''


import csv
import math
from typing import List, Tuple


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
        '''
        Func return list of baby names or assert error
        '''
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise AssertionError
        if page <= 0 or page_size <= 0:
            raise AssertionError
        pagination_indexes = index_range(page, page_size)
        data_set = self.dataset()
        return data_set[pagination_indexes[0]: pagination_indexes[1]]

    def get_hyper(self, page: int, page_size: int) -> dict:
        """
        Func that retuns a dictionary of:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        dataset_records = self.get_page(page, page_size)

        page_dict = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(dataset_records),
            'page': page,
            'data': dataset_records,
            'next_page': page + 1 if (page + 1) <= page_dict else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': page_dict
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Func return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)
