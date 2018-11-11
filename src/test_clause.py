from clause import *
from argument import Argument
import pytest


@pytest.mark.parametrize("clause, expected_result", [
    (
        Clause(
            frozenset([
                Literal(False, (Argument('John', True), ), 'L'),
                Literal(True, (Argument('X', True), ), 'R')
            ])
        ),
        frozenset([
            Clause(
                frozenset([Literal(True, (Argument('John', True), ), 'L')])
            ),

            Clause(
                frozenset([Literal(False, (Argument('X', True), ), 'R')])
            )
        ])
    ),

    (
        Clause(
            frozenset([
                Literal(True, (Argument('X', True), ), 'R')
            ])
        ),
        frozenset([
            Clause(
                frozenset([Literal(False, (Argument('X', True), ), 'R')])
            )
        ])
    ),
    
])
def test_negate_clause(clause, expected_result):
    result = negate_clause(clause)
    assert len(result) == len(expected_result)
    assert result == expected_result


@pytest.mark.parametrize("clause, transformation, expected_result", [
    (
        Clause(
            frozenset([
                Literal(False, (Argument('X', False), ), 'L'),
                Literal(True, (Argument('X', False), ), 'R')
            ])
        ),
        {Argument('X', False): Argument('John', True)},
        Clause(
            frozenset([
                Literal(False, (Argument('John', True), ), 'L'),
                Literal(True, (Argument('John', True), ), 'R')
            ])
        ),
    ),
    
    (
        Clause(
            frozenset([
                Literal(False, (Argument('X', False), ), 'L'),
                Literal(True, (Argument('Y', False), ), 'R')
            ])
        ),
        {
            Argument('X', False): Argument('John', True),
            Argument('Y', False): Argument('Mary', True),
        },
        Clause(
            frozenset([
                Literal(False, (Argument('John', True), ), 'L'),
                Literal(True, (Argument('Mary', True), ), 'R')
            ])
        ),
    )
])
def test_substitute(clause: Clause, transformation, expected_result):
    result = subsitute(clause, transformation)
    assert result == expected_result


@pytest.mark.parametrize("clause_i, clause_j, expected_result",[
        (
            Clause(
                frozenset([
                    Literal(False, (Argument('X', False), ), 'L'),
                    Literal(True, (Argument('Y', False), ), 'R')
                ])
            ),

            Clause(
                frozenset([
                    Literal(True, (Argument('X', False), ), 'L'),
                ])
            ),

            Clause(
                frozenset([
                    Literal(True, (Argument('Y', False), ), 'R'),
                ])
            )
        ),

        (
            Clause(
                frozenset([
                    Literal(False, (Argument('X', False), ), 'L'),
                    Literal(True, (Argument('Y', False), ), 'R')
                ])
            ),

            Clause(
                frozenset([
                    Literal(False, (Argument('X', False), ), 'L'),
                ])
            ),

            Clause(
                frozenset([
                    Literal(False, (Argument('X', False), ), 'L'),
                    Literal(True, (Argument('Y', False), ), 'R')
                ])
            )
        ),

])
def test_combine(clause_i: Clause, clause_j: Clause, expected_result: Clause):
    result = combine(clause_i, clause_j)
    assert result == expected_result
