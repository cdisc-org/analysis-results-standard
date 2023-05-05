from typing import Union
from uuid import UUID


class DataGroup():
    """
    A subdivision of the analysis dataset records based on a defined factor.
    """
    dataGroupid: Union[UUID, str]
