from typing import List, Union
from uuid import UUID

from .data_group import DataGroup

class DataGroupingFactor():
    id: Union[UUID, str] = None
    dataDriven: bool
    groups: List[Union[dict, DataGroup]] = []
