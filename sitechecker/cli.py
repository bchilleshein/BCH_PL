# cli.py

import argparse
#import csv

def read_user_cli_args():
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste a disponibilidade de uma URL."
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Insira um ou mais URLs.",
    )
#    parser.add_argument(
#        "-f",
#        "--input-file",
#        metavar="FILE",
#        type=csv,
#        default="",
#        help="Leia URLs de um arquivo.",
#    )
    return parser.parse_args()
        
def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(f'O status da "{url}" é:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Erro: "{error}"')            