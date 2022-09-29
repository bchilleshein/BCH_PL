**VERIFICANDO A CONECTIVIDADE DE URLs**</br></br>

Este projeto de python visa identificar se um URL está online ou offline, retornando uma mensagem para o usuário.

Ele é composto pela pasta **sitechecker** que contém 4 arquivos de código (**__init__.py**, **__main__.py**, **checker.py** e **cli.py**), pelo **.gitignore**, pelo **requirements.txt**, além deste arquivo (**README.md**).</br></br>


**INSTRUÇÕES**</br></br>


**1.** Para iniciar esta aplicação, recomenda-se utilizar um ambiente virtual (venv). Para isso, você deve abrir um terminal no programa de sua preferência e rodar os comandos:

```
cd meuprojeto
python -m venv venv
source venv/Scripts/activate
```

**Entendendo um pouco melhor**</br> O **cd meuprojeto** abre uma pasta chamada meuprojeto; o **python -m venv venv** cria o ambiente virtual; e o **source venv/Scripts/activate** ativa o ambiente virtual criado - isso para o Windows.</br></br>
**Observação**</br> Você já deve ter criado a pasta meuprojeto.</br></br>


**2.** Para organizar o seu projeto, você deve criar uma pasta para armazenar os seus códigos. Basta você digitar no seu terminal:

```mkdir sitechecker```

Dentro dessa pasta você gera os arquivos **__init__.py**, **__main__.py**, **checker.py** e **cli.py**, a partir de:

```
touch sitechecker/__init__.py
touch sitechecker/__main__.py
touch sitechecker/checker.py
touch sitechecker/cli.py
```

Agora, você deve montar os seus códigos.</br></br>


**3.** O arquivo **checker.py** é responsável por fornecer as principais funcionalidades da aplicação. Então, abra ele no seu editor de código e adicione o código responsável por verificar a conectividade do site.


```
# checker.py

from http.client import HTTPConnection
from urllib.parse import urlparse

def site_is_online(url, timeout=2):
    """Return True if the target URL is online.

    Raise an exception otherwise.
    """
    # Defines a generic Exception as placeholder
    error = Exception("Ops, algo deu errado.")
    # Parses URL and finds host
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    # Starts a for loop using HTTP and HTTPs ports
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error
```


**Entendendo um pouco melhor**</br> 
A função site_is_online faz uma solicitação de conexão ao URL para ver se ele está online. Se estiver, retorna True, senão gera uma exceção/erro que exibe o problema encontrado.</br></br>


**4.** O arquivo **cli.py** é responsável por conter as linhas de comando da aplicação. Ou seja, como devem ser os comandos que você dá para que o projeto funcione adequadamente. Para inserir essas configurações, abra o arquivo no seu editor e adicione o código abaixo.


```
# cli.py

import argparse

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
    return parser.parse_args()
        
def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(f'O status da "{url}" é:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \nErro: "{error}".')
```  


**Entendendo um pouco melhor**</br> 
Neste, como mencionado acima, você define como devem ser os comandos que o usuário vai colocar para fazer com que a funcionalidade rode e ele receba algum resultado. Então, você diz que ele deve inserir -u ou --urls e que deve ser um texto. Caso o site esteja online, ele recebe uma mensagem dizendo "O status da "url" é: "Online!" 👍" ou, caso esteja offline, recebe "O status da "url" é: "Offline?" 👎 Erro: "tipo de erro"."  

**Observação**</br> Você vai observar que o código aqui exposto e o fornecido no arquivo **cli.py** são um pouco diferentes. No código do arquivo há linhas com #, que são um outro argumento para tentar ler e verificar a conectividade de uma lista de URLs em um arquivo. Ressalta-se, no entanto, que para que esse tipo de análise seja possível, outras alterações devem ser feitas nos códigos. Inclusive, se você retirar os #, e tentar ler um arquivo por meio de cat (nome_do_arquivo.extensão), ele consegue ler os URLs, mas quando vai realizar a análise, ele não roda.</br></br>


**5.** Para que a aplicação funcione corretamente, você deve escrever um código que conecte os códigos anteriores. Esse código deve ficar armazenado no arquivo **__main__.py**. Assim, abra-o no seu editor e insira as linhas abaixo:


```
#__main__.py

import sys

from asyncore import read
from sitechecker.checker import site_is_online
from sitechecker.cli import display_check_result, read_user_cli_args

def main():
    user_args = read_user_cli_args()
    urls = user_args.urls
    if not urls:
        print("Faltou colocar um URL. Caso precise de ajuda, após sitechecker digite --help.")
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

if __name__ == "__main__":
    main()
```


**Entendendo um pouco melhor**</br> 
Você define 3 funções que puxam informações deste e dos outros arquivos. Na def main(), por exemplo, você chama read_user_cli_args() para analisar os argumentos da linha de comando (aquilo que você insere) e armazena na variável user_args local. Então, ele vai verificar se você esqueceu de colocar um url, se sim, aparece a mensagem "Faltou colocar um URL. Caso precise de ajuda, após sitechecker digite --help.". Caso você tenha colocado, ele vai chamar a função _site_check() - responsável por receber a lista de URLs- e aplicar a função site_is_online. Assim, as conexões com os sites são solicitadas, se der certo, retorna true e se der errado, um erro.

**Observação**</br> Você vai observar que o código aqui exposto e o fornecido no **__main__.py** são um pouco diferentes. No código do arquivo há linhas com #, que são comentários contendo pedaços de códigos para ler urls de um arquivo. 
Ressalta-se, no entanto, que para que esse tipo de análise seja possível, outras alterações devem ser feitas nos códigos. Inclusive, se você retirar os # e tentar ler um arquivo por meio de cat (nome_do_arquivo.extensão), ele consegue ler os URLs, mas quando vai realizar a análise, ele não roda.</br></br>


**6.** O arquivo **__init__.py** é responsável por ativar o projeto como um pacote do Python. Nele, você pode escrever a versão da aplicação.</br></br>

**7.** O **.gitignore** é um arquivo de texto responsável por informar ao Git quais arquivos ou pastas do projeto ele deve ignorar. Você pode pegar um arquivo de **.gitignore** na internet. No projeto atual, o principal arquivo que deve estar no **.gitignore** é o do venv.


```
# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
```
</br>


**MEXENDO NA APLICAÇÃO**


Para verificar se o seu projeto está funcionando, você deve abrir um terminal e inserir:

```
python -m sitechecker -(AQUI VOCÊ COLOCA UM DOS ARGUMENTOS QUE VOCÊ CONFIGUROU)
```


Ex.:</br>
```
python -m sitechecker -h
```

Ele retorna:</br>

```
usage: sitechecker [-h] [-u URLs [URLs ...]]

Teste a disponibilidade de uma URL.

optional arguments:
  -h, --help            show this help message and exit
  -u URLs [URLs ...], --urls URLs [URLs ...]
                        Insira um ou mais URLs.
```


Caso você queira ver a conectividade de um site, você deve digitar:

```
python -m sitechecker -u (AQUI VOCÊ DIGITA O URL)
```

Ex.:</br> 
```
python -m sitechecker -u www.uol.com.br
```

Ele retorna:</br> 
```
O status da "www.uol.com.br" é: "Online!" 👍
```

Caso queira colocar mais de um URL, basta adicionar os demais após o primeiro, sempre deixando um espaço entre eles.

Ex.:</br>
```
python -m sitechecker -u www.uol.com.br www.recordnews.com.br
```

Ele retorna: 
```
O status da "www.uol.com.br" é: "Online!" 👍
O status da "www.recordnews.com.br" é: "Online!" 👍
```
