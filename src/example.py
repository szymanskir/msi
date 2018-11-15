from .clause_parser import ClauseParser
from .resolution_method import resolution


clauses_list = ["~PIES(x) | WYJE(x)",
         "~POSIADA(x,y) | ~KOT(y) | ~POSIADA(x,z) | ~MYSZ(z)",
         "~KIEPSKO_SYPIA(x) | ~POSIADA(x,y) | ~WYJE(y)",
         "POSIADA(Janek,x) & [KOT(x) | PIES(x))]"]

thesis_input="KIEPSKO_SYPIA(Janek) & POSIADA(Janek,z) & MYSZ(z)",

clause_parser = ClauseParser()
parsed_clauses = clause_parser.parse_cnf_list(clauses_list)
parsed_thesis = clause_parser.parse_cnf(thesis_input)


print(resolution(parsed_clauses, parsed_thesis))
