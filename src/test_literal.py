from literal import *
import pytest


@pytest.mark.parametrize("literal, expected_result", [
    (Literal(False, tuple(), 'a'), Literal(True, tuple(), 'a')),
    (Literal(False, (1,2), 'a'), Literal(True, (1,2), 'a')),
    (Literal(True, (1,2), 'a'), Literal(False, (1,2), 'a')),
])
def test_negate_literal(literal, expected_result):
    result = negate_literal(literal)
    assert result == expected_result


@pytest.mark.parametrize("argument, from_argument, to_argument, expected_result", [
    (Argument('X', False),
     Argument('X', False),
     Argument('John', True),
     Argument('John', True)
    ),
])
def test_substitute_argument(argument, from_argument, to_argument, expected_result):
    result = substitute_argument(argument, from_argument, to_argument)
    assert result == expected_result
    

@pytest.mark.parametrize("literal, from_argument, to_argument, expected_result", [
    (Literal(True, (Argument('X', False),), 'R'),
     Argument('X', False),
     Argument('John', True),
     Literal(True, (Argument('John', True),), 'R')
    ),

    (Literal(True, (Argument('X', False), Argument('Y', False))),
     Argument('X', False),
     Argument('John', True),
     Literal(True, (Argument('John', True), Argument('Y', False)))
    ),

    (Literal(True, (Argument('Y', False), Argument('X', False))),
     Argument('X', False),
     Argument('John', True),
     Literal(True, (Argument('Y', False), Argument('John', True)))
    ),
])
def test_substitute_literal(literal, from_argument, to_argument, expected_result):
    result = substitute_literal(literal, from_argument, to_argument)
    assert result == expected_result
    

@pytest.mark.parametrize("literal1, literal2, expected_transformation", [
    (Literal(True, (Argument('X', False),)),
     Literal(True, (Argument('John', True),)),
     {Argument('X', False): Argument('John', True)}
    ),

    
    (Literal(True, (Argument('John', True),)),
     Literal(True, (Argument('John', True),)),
     dict()
    ),


    (Literal(True, (Argument('Mary', True),)),
     Literal(True, (Argument('John', True),)),
     None
    ),

    (Literal(True, (Argument('John', True),)),
     Literal(True, (Argument('X', False),)),
     {Argument('X', False): Argument('John', True)}
    ),

    (Literal(True, (Argument('Y', False),)),
     Literal(True, (Argument('X', False),)),
     {Argument('Y', False): Argument('X', False)}
    ),

    (Literal(True, (Argument('X', False),)),
     Literal(True, (Argument('Y', False),)),
     {Argument('X', False): Argument('Y', False)}
    ),

    (Literal(True, (Argument('Y', False), Argument('John', True))),
     Literal(True, (Argument('Mary', True), Argument('X', False))),
     {
         Argument('Y', False): Argument('Mary', True),
         Argument('X', False): Argument('John', True)
     }
    ),

    (Literal(True, (Argument('Y', False), Argument('John', True))),
     Literal(True, (Argument('Mary', True), Argument('X', False))),
     {
         Argument('X', False): Argument('John', True),
         Argument('Y', False): Argument('Mary', True)
     }
    )
])
def test_find_transformation(literal1, literal2, expected_transformation):
    result = find_transformation(literal1, literal2)
    assert result == expected_transformation 
    
