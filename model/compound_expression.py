from typing import List, Union

from .ars_enums import LogicalOperator
from .where_clause import WhereClause

class CompoundExpression():
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[Union[dict, WhereClause]] = []
