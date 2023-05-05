from typing import Union
from uuid import UUID

from .grouping_factor import GroupingFactor


class SubjectGroupingFactor(GroupingFactor):
    """
    A factor used to subdivide the subject population for comparative analysis (e.g., treatment, sex, race, age).
    """
    subjectGroupingFactorId: Union[UUID, str] = None
    