from typing import Union, Optional
from uuid import UUID

from .compound_set_expression import CompoundSetExpression
from .where_clause import WhereClause

class AnalysisSet(WhereClause):
    """
    A set of subjects whose data are to be included in the main analyses. This should be defined in the statistical
    section of the protocol. NOTE: There are a number of potential analysis sets, including, for example, the set
    based upon the intent-to-treat principle. [ICH E9]
    """
    analysisSetid: Union[UUID, str] = None
    label: Optional[str] = None
    compoundExpression: Optional[Union[dict, CompoundSetExpression]] = None

