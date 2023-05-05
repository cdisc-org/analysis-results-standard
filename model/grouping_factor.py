from typing import List, Union, Optional
from uuid import UUID

from .group import Group

class GroupingFactor():
    """
    A factor used to subdivide either the subject population or data records in an analysis dataset for analysis.
    """
    id: Union[UUID, str] = None
    dataDriven: bool = None
    label: Optional[str] = None
    groupingVariable: Optional[str] = None
    groups: List[Union[dict, Group]] = []
