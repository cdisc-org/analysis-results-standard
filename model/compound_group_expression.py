from typing import List, Union

from ars_enums import LogicalOperator

class CompoundGroupExpression():
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[str]= []
