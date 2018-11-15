import pytest

from src.clause_parser import *

@pytest.mark.parametrize("input_string, expected_result", [
    ("Constant", Argument("Constant", True)),
    ("variable", Argument("variable", False))
])
def test_parse_argument(input_string, expected_result):
    clause_parser = ClauseParser()
    result = clause_parser.parse_argument(input_string)
    assert result == expected_result


@pytest.mark.parametrize("input_string, expected_result", [
    ("[abc]", "abc")
])
def test_strip_brackets(input_string, expected_result):
    clause_parser = ClauseParser()
    result = clause_parser.strip_brackets(input_string)
    assert result == expected_result


@pytest.mark.parametrize("input_string, expected_result", [
    ("~PIES(x)", Literal(True, (Argument("x", False),), "PIES")),
    ("PIES(x,y)", Literal(False, (Argument("x", False), Argument("y", False)), "PIES"))
])
def test_parse_literal(input_string, expected_result):
    clause_parser = ClauseParser()
    result = clause_parser.parse_literal(input_string)
    assert result == expected_result


@pytest.mark.parametrize("input_string, expected_result", [
    ("~PIES(x) | KOT(y)", Clause(frozenset([
        Literal(True, (Argument("x", False),), "PIES"),
        Literal(False, (Argument("y", False),), "KOT")
    ])))
])
def test_parse_clause(input_string, expected_result):
    clause_parser = ClauseParser()
    result = clause_parser.parse_clause(input_string)
    assert result == expected_result
