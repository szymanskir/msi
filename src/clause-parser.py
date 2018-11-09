from typing import NamedTuple

from clause import Clause
from constant import Constant
from literal import Literal
from variable import Variable


class ClauseParser(NamedTuple):
    negateCharacter: str = "/"
    orSplitter: str = " OR "

    def parse_clause(self, input_string: str):
        literals_list = input_string.split(self.orSplitter)
        parsed_literals = list(map(self.parse_literal, literals_list))
        return Clause(parsed_literals)

    def parse_literal(self, input_string):
        negated = input_string[0] == self.negateCharacter
        if negated:
            input_string = input_string[1:]

        name_arguments = input_string.split('(')
        literal_name = name_arguments[0]
        arguments = (name_arguments[1][:-1]).split(",")
        parsed_arguments = list(map(self.parse_argument, arguments))

        return Literal(negated, parsed_arguments, literal_name)

    @staticmethod
    def parse_argument(input_string):
        if input_string[0].isupper():
            return Constant(input_string[0], None)

        return Variable(input_string[0], None)
