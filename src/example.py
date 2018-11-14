from .clause_parser import ClauseParser
from .resolution_method import resolution


clauses_list = ["/PIES(x) OR WYJE(x)",
         "/POSIADA(x,y) OR /KOT(y) OR /POSIADA(x,z) OR /MYSZ(z)",
         "/KIEPSKO_SYPIA(x) OR /POSIADA(x,y) OR /WYJE(y)",
         "POSIADA(Janek,x) AND [KOT(x) OR PIES(x))]"]

thesis_input="KIEPSKO_SYPIA(Janek) AND POSIADA(Janek,z) AND MYSZ(z)",

clause_parser = ClauseParser()
parsed_clauses = clause_parser.parse_cnf_list(clauses_list)
parsed_thesis = clause_parser.parse_cnf(thesis_input)


print(resolution(parsed_clauses, parsed_thesis))
