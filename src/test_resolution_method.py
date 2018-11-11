import pytest

from typing import Set

from resolution_method import *
from clause import Clause 
from argument import Argument
from literal import Literal


@pytest.mark.parametrize("clause_i, clause_j, expected_result", [
    (
        Clause(
            frozenset([
                Literal(True, (Argument('X', False), ), 'pies'),
                Literal(False, (Argument('X', False), ), 'wyje')
            ])
        ),

        Clause(
            frozenset([
                Literal(False, (Argument('a', False), ), 'kot'),
                Literal(False, (Argument('a', False), ), 'pies')
            ])
        ),

        {Clause(
            frozenset([
                Literal(False, (Argument('a', False), ), 'kot'),
                Literal(False, (Argument('a', False), ), 'wyje')
            ])
        )},
        
    )
])
def test_resolve(clause_i: Clause, clause_j: Clause, expected_result: Set[Clause]):
    result = resolve(clause_i, clause_j)
    assert result == expected_result
    



@pytest.mark.parametrize("knowledge_base, thesis, expected_result", [
    (
        {
            Clause(
                frozenset([
                    Literal(True, (Argument('X', False), Argument('history', True)), 'pass'),
                    Literal(True, (Argument('X', False), Argument('lottery', True)), 'win'),
                    Literal(False, (Argument('X', False),), 'happy')
                ])
            ),

            Clause(
                frozenset([
                    Literal(True, (Argument('Y', False),), 'studies'),
                    Literal(False, (Argument('Y', False), Argument('Z', False)), 'pass')
                ])
            ),

            Clause(
                frozenset([
                    Literal(True, (Argument('W', False),), 'lucky'),
                    Literal(False, (Argument('W', False), Argument('V', False)), 'pass')
                ])
            ),

            Clause(
                frozenset([
                    Literal(True, (Argument('John', True),), 'studies'),
                ])
            ),

            Clause(
                frozenset([
                    Literal(False, (Argument('John', True),), 'lucky'),
                ])
            ),

            Clause(
                frozenset([
                    Literal(True, (Argument('U', False),), 'lucky'),
                    Literal(False, (Argument('U', False), Argument('lottery', True)), 'win')
                ])
            ),
        },
        
        Clause(
            frozenset([
                Literal(False, (Argument('John', True),), 'happy'),
            ])
        ),

        True
    )
])
def test_resolution(knowledge_base: Set[Clause], thesis:Clause, expected_result: bool):
    result = resolution(knowledge_base, thesis)
    assert result == expected_result
