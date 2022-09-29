#__main__.py

import sys
#import pathlib

#from symbol import file_input
from asyncore import read
from sitechecker.checker import site_is_online
from sitechecker.cli import display_check_result, read_user_cli_args

def main():
    user_args = read_user_cli_args()
    urls = user_args.urls
#    file_path = pathlib.Path(file)
    if not urls:
        print("Faltou colocar um URL. Caso precise de ajuda, após sitechecker digite --help.") #file=sys.stderr)
        #print("Faltou colocar um URL. Caso precise de ajuda, após sitechecker digite --help.",file=sys.stderr)
        sys.exit(1)
    _site_check(urls)

def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

#def get_websites_urls(user_args):
#    urls = user_args.urls
#    if user_args.input_file:
#        urls += read_urls_from_file(user_args.input_file)

#def read_urls_from_file(file):
#    file_path = pathlib.Path(file)
#    if file_path.is_file():
#        with file_path.open() as urls_file:
#            urls = [url.strip() for url in urls_file]
#            if urls:
#                return urls
#            print (f"Erro: o arquivo adicionado está vazio., {file}", file=sys.stderr)
#    else:
#        print("Erro: arquivo adicionado não encontrado.", file=sys.stderr) 
#    return[] 

if __name__ == "__main__":
    main()  