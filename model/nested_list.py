from typing import List, Union

from .ordered_list_item import OrderedListItem


class NestedList():
    listItems: List[Union[dict, "OrderedListItem"]] = []

