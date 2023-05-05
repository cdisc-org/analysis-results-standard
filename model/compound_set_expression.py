from typing import List, Union

from .compound_expression import CompoundExpression
from .ars_enums import LogicalOperator

class CompoundSetExpression(CompoundExpression):
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[str] = []
