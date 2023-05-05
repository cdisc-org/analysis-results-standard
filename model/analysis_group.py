from typing import List, Union
from uuid import UUID

from .group import Group


class AnalysisGroup(Group):
    """
    A subdivision of the subject population based on a defined factor (e.g., subjects whose treatment is Drug A,
    subjects whose gender is male).
    """
    analysisGroupId: Union[UUID, str] = None
