from literal import *
import pytest


@pytest.mark.parametrize("literal, expected_result", [
    (Literal(False, tuple(), 'a'), Literal(True, tuple(), 'a'))
])
def test_negate_literal(literal, expected_result):
    result = negate_literal(literal)
    assert result == expected_result
    
