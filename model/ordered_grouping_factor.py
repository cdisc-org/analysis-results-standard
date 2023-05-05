from typing import List, Union, Optional

from .data_grouping_factor import DataGroupingFactor

class OrderedGroupingFactor():
    order: int = None
    groupingId: Optional[str] = None
    dataGrouping: Optional[Union[dict, DataGroupingFactor]] = None