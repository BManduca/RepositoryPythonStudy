# Configurações e instalações gerais

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

- # Requirements
    - Arquivo para registrar as dependências e quais são suas versões
    - .venv/bin/pip3 freeze > requirements.txt
  
## Validação de dados e tratativa
- ## Biblioteca Cerberus
    - Busca facilitar na questão de tratar dados e fazer uma validação de entrada
    - Documentação: https://docs.python-cerberus.org/
    - instalação via pip install: pip3 install Cerberus

## Sintaxes e usabilidade
- ## snake_case
    - é o formato padrão utilizado no python, aonde as palavras são separadas por _
    - Esse padrão pode ser atribuído a Funções, Variáveis e Métodos.

- ## PascalCase
    - é o formato utilizado, aonde as palavras tem as suas iniciais em maiúsculo.
    - Esse padrão é utilizado em Classes.

<br />
<br />
<br />

# Unitary Tests
- pytest -> https://docs.pytest.org/en/8.0.x/getting-started.html
- install: pip3 install -U pytest