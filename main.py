import click
import logging

from src.clause_parser import ClauseParser
from src.resolution_method import resolution
from src.tree_visualizer import display_resolution_tree


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--visualize', is_flag=True)
def main(input_file, visualize):
    """Command line tool for performing a proof
    using the resolutions method.

    Arguments
    ---------
        input_file - input file containing the knowledge base and the
        negated thesis in clause form. The knowledge base and the
        thesis are separated by '---'

        visualize - specifies if the resolution tree should be displayed
    """
    logging.info('Reading lines...')

    with open(input_file) as f:
        content = f.read()

    clauses, thesis = content.split('---\n')

    logging.info('Parsing clauses...')
    parser = ClauseParser()
    parsed_clauses = parser.parse_cnf_list(clauses.splitlines())
    parsed_thesis = parser.parse_cnf_list(thesis.splitlines())

    result, tree = resolution(parsed_clauses, parsed_thesis)

    if visualize:
        display_resolution_tree(tree)

    logging.info(f'The thesis is {result}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
