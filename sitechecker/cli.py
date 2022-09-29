# cli.py

import argparse
import pathlib
import sys

def read_user_cli_args():
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste a disponibilidade de uma URL"
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
    return parser.parse_args()

def get_websites_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += read_urls_from_file(user_args.input_file)

def read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print (f"Erro: o arquivo adicionado está vazio, {file}", file=sys.stderr)
    else:
        print("Erro: arquivo adicionado não encontrado", file=sys.stderr) 
    return[]           

def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(f'O status da "{url}" é:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Erro: "{error}"')            