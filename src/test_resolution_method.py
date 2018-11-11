import pytest

from resolution_method import *
from clause import Clause 
from argument import Argument
from literal import Literal


@pytest.mark.parametrize("clause_i, clause_j, expected_result", [
    (
        Clause(
            (
                Literal(True, (Argument('X', False), ), 'pies'),
                Literal(False, (Argument('X', False), ), 'wyje')
            )
        ),

        Clause(
            (
                Literal(False, (Argument('a', False), ), 'kot'),
                Literal(False, (Argument('a', False), ), 'pies')
            )
        ),

        [Clause(
            (
                Literal(False, (Argument('a', False), ), 'kot'),
                Literal(False, (Argument('a', False), ), 'wyje')
            )
        )],
        
    )
])
def test_resolve(clause_i: Clause, clause_j: Clause, expected_result: List[Clause]):
    result = resolve(clause_i, clause_j)
    assert result == expected_result
    
