#!/usr/bin/env python3
'''
fuction file
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """_summary_

    Args:
        page (int): _Current Page_
        page_size (int): _Numbers of items on per page _

    Returns:
        Tuple[int, int]: _Current items, The end of items_
    """
    return ((page_size * (page - 1)), page_size * page)
