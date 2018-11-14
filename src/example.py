from clauseparser import ClauseParser
from resolution_method import resolution


input_string = """/PIES(x) OR WYJE(x)
/POSIADA(x,y) OR /KOT(y) OR /POSIADA(x,z) OR /MYSZ(z)
/KIEPSKO_SYPIA(x) OR /POSIADA(x,y) OR /WYJE(y)
POSIADA(Janek,x) AND [KOT(x) OR PIES(x))]
/KIEPSKO_SYPIA(Janek) AND POSIADA(Janek,z) AND MYSZ(z)"""

thesis = "KIEPSKO_SYPIA(Janek) OR /POSIADA(Janek,z) OR /MYSZ(z)"

clause_parser = ClauseParser()
parsed_clauses = clause_parser.parse_cnf_list(input_string.split("\n"))
print('\n'.join(' '.join(map(str, sl)) for sl in parsed_clauses))

parsed_thesis = clause_parser.parse_clause(thesis)
print(parsed_thesis)

print(resolution(parsed_clauses,parsed_thesis))
