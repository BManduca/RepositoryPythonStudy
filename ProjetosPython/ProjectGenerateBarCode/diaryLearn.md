## Diário de aprendizado

- ### Neste espaço será armazenado todas as explicações, termos e novidades expostas dentro do projeto.

___________________________________________________________________________________________________ 

<br />
<br />

## Instalação de aplicações/ferramentas dentro do projeto
- ### virtualenv
    - Uma ferramenta para criar ambientes python virtuais isolados
    - instalação: pip3 install virtualenv
    - guia do usuário: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
        - **Create and Use Virtual Environments**
            - python3 -m venv .venv

        - **Activate a virtual environment**
            - source .venv/bin/activate
            - caso aconteça erro na instalação, comentando de não ter pacotes instalados ou pacotes que estejam 'quebrados', utilizar o seguinte comando(obs.: copiar tudo e jogar no terminal):
                - sudo rm /var/lib/apt/lists/* ; sudo rm /var/lib/apt/lists/partial/* ; sudo apt-get -f install ; sudo apt-get clean ; sudo apt-get update
                - após executar deletar a pasta venv e em seguida executar os comandos de criação e ativação novamente.

            - To confirm the virtual environment is activated, check the location of your Python interpreter:
                - which python

            - While the virtual environment is active, the above command will output a filepath that includes the .venv directory, by ending with the following:
                - .venv/bin/python

- # Pylint
    - Pylint é um analisador de código estático para python 2 ou 3.
    - instalação: pip3 install pylint

- # Criando um arquivo geral de configuração Pylint
    - pylint --generate-rcfile > .pylintrc

- # Pre-commit
    - Um framework para gerenciar e manter pre-commits multilíngues
    - instalação: pip3 install pre-commit -> pre-commit install

- # Flask
    - Framework de aplicação Web, que foi projetado com intuito de escalar aplicações web complexas, de uma maneira inicial rápida e fácil.
    - instalação: pip3 install -U Flask

- # Python BarCode
    - Maneira simples de criar código de barras em python
    - instalação: pip3 install python-barcode

- # Pillow
    - Biblioteca requisitada para geração de imagens.
    - instalação: pip3 install pillow

- # Code128
    - instalação: pip3 install code128
    - É uma simples biblioteca para criar código de barras no padrão Code-128

- # Requirements
    - Arquivo para registrar as dependências e quais são suas versões
    - .venv/bin/pip3 freeze > requirements.txt    

## Sintaxes e usabilidade
- ## snake_case
    - é o formato padrão utilizado no python, aonde as palavras são separadas por _
    - Esse padrão pode ser atribuído a Funções, Variáveis e Métodos.

- ## PascalCase
    - é o formato utilizado, aonde as palavras tem as suas iniciais em maiúsculo.
    - Esse padrão é utilizado em Classes.


## Validação de dados e tratativa
- ## Biblioteca Cerberus
    - Busca facilitar na questão de tratar dados e fazer uma validação de entrada
    - Documentação: https://docs.python-cerberus.org/
    - instalação via pip install: pip3 install Cerberus

<br />
<br />
<br />

# Unitary Tests
- pytest -> https://docs.pytest.org/en/8.0.x/getting-started.html
- install: pip3 install -U pytest

- Geralmente arquivos de teste unitário tem a palavra reservada test no final do nome do arquivo.
- executando teste:
    - pytest
        - já vai identificar o(s) arquivo(s) de teste presente no repositório
    - pytest -s -v 
        - executa os teste criados e mostra o retorno se passou ou não.
