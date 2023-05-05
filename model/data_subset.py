from typing import Union, Optional
from uuid import UUID

from .compound_subset_expression import CompoundSubsetExpression

class DataSubset():
    id: Union[UUID, str] = None
    label: Optional[str] = None
    compoundExpression: Optional[Union[dict, CompoundSubsetExpression]] = None

