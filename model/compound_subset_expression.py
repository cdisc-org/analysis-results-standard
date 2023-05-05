from typing import List, Union, Optional
from uuid import UUID

from .ars_enums import LogicalOperator
from .where_clause import WhereClause


class CompoundSubsetExpression():
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[WhereClause] = []
