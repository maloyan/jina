"""Argparser module for pinging"""
from jina.parsers.base import set_base_parser


def set_new_project_parser(parser=None):
    """Set the parser for `ping`

    :param parser: an existing parser to build upon
    :return: the parser
    """
    if not parser:
        parser = set_base_parser()

    parser.add_argument(
        'name', type=str, help='The name of the project', default='hello-jina'
    )
    return parser
