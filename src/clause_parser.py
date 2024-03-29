from functools import reduce
from operator import or_
from typing import NamedTuple, Set

from .argument import Argument
from .clause import Clause
from .literal import Literal


class ClauseParser(NamedTuple):
    """Class responsible for parsing input data.
    """
    negate_marker: str = "~"
    or_splitter: str = " | "
    and_splitter: str = " & "
    arguments_open_bracket = "("
    arguments_close_bracket = ")"
    clause_open_bracket = "["
    clause_close_bracket = "]"

    def parse_cnf_list(self, clauses_list: list) -> Set[Clause]:
        """Parses list of sentences in CNF form.
        """
        return reduce(or_, (map(self.parse_cnf, clauses_list)))

    def parse_cnf(self, input_string: str) -> Set[Clause]:
        """Parses single sentence in CNF form.
        """
        clauses_list = input_string.split(self.and_splitter)
        return set(map(self.parse_clause, clauses_list))

    def parse_clause(self, input_string: str) -> Clause:
        """Parses single clause.
        """
        input_string = self.strip_brackets(input_string)
        literals_list = list(input_string.split(self.or_splitter))
        parsed_literals = frozenset(map(self.parse_literal, literals_list))
        return Clause(parsed_literals)

    def parse_literal(self, input_string: str) -> Literal:
        """Parses single literal.
        """
        negated = input_string.find(self.negate_marker) == 0

        if negated:
            input_string = input_string[1:]

        name_arguments = input_string.split(self.arguments_open_bracket)
        literal_name = name_arguments[0]
        arguments = (name_arguments[1][:-1]).split(",")
        parsed_arguments = tuple(map(self.parse_argument, arguments))

        return Literal(negated, parsed_arguments, literal_name)

    def strip_brackets(self, input_string: str) -> str:
        """Removes redundant brackets.
        """
        if input_string.find(self.clause_open_bracket) == 0:
            input_string = input_string[len(self.clause_open_bracket):-len(self.clause_close_bracket)]

        return input_string

    def parse_argument(self, input_string: str) -> Argument:
        """Parses single argument.
        Arguments starting with uppercase are treated as constants.
        Arguments starting with lowercase are treated as variables.
        """
        if input_string[0].isupper():
            return Argument(input_string, True)

        return Argument(input_string, False)
