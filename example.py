from src.clause_parser import ClauseParser
from src.resolution_method import resolution
from src.tree_visualizer import display_resolution_tree


clauses_list = ["~PIES(x) | WYJE(x)",
         "~POSIADA(x,y) | ~KOT(y) | ~POSIADA(x,z) | ~MYSZ(z)",
         "~KIEPSKO_SYPIA(x) | ~POSIADA(x,y) | ~WYJE(y)",
         "POSIADA(Janek,x) & [KOT(x) | PIES(x))]"]

thesis_input="KIEPSKO_SYPIA(Janek) & POSIADA(Janek,z) & MYSZ(z)"

clause_parser = ClauseParser()
parsed_clauses = clause_parser.parse_cnf_list(clauses_list)
parsed_thesis = clause_parser.parse_cnf(thesis_input)


result, tree = resolution(parsed_clauses, parsed_thesis)
display_resolution_tree(tree)
print(result)
