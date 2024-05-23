"""
    filme = {
        'Titulo': 'Star Wars',
        'Ano': 1977,
        'Diretor': 'George Lucas'
    }

    for k, v in filme.items():
        print(f'{k} ==> {v}')

    -----------------------------------------------------------------------------------------

    ações:

        print(pessoas.keys())
        print(pessoas.values())
        print(pessoas.items())

        #alterando nome
        pessoas['nome'] = 'Gustavo'

        #adicionando uma propriedade
        pessoas['peso'] = 79.4


    pessoas = {
        'nome': 'Brunno',
        'idade': 31,
        'sexo': 'M'
    }

    pessoas['peso'] = 79.4

    for k, v in pessoas.items():
        print(f'{k} = {v}')

    print()
    print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

    -----------------------------------------------------------------------------------------

    brasil = []

    estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
    estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

    brasil.append(estado1)
    brasil.append(estado2)

    print(brasil)

    -----------------------------------------------------------------------------------------
"""

import time

estado = {}
brasil = []

for i in range(0, 3):
    estado['uf'] = str(input('UNIDADE FEDERATRIVA: '))
    estado['sigla'] = str(input('SIGLA DO ESTADO: '))
    brasil.append(estado.copy())
    time.sleep(1)
    print()

print()
print('='*30)
print('{:^30}'.format(' RELAÇÃO: '))
print('='*30)
print()
print('-='*15)
print(f'{"UF":<16}{"SIGLA":^10}')
print('-'*30)
for e in brasil:
    print(f'{e["uf"]:<16}{e["sigla"]:^10}')
    """
        for k, v in e.items():
            # print(f'| {k} ==> {v} ', end=' ')
        print()
        # print('|')
        # print(f'{e["uf"]} ==> {e["sigla"]}')
    """
print('-=' * 15)

