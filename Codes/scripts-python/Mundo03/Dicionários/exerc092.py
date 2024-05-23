"""
    CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO
    E CADASTRE-OS(COM IDADE) EM UM DICIONÁRIO CASO O CTPS FOR DIFERENTE DE ZERO,
    O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO.
    CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE
    APOSENTAR.
"""

from datetime import datetime

print()
print('-'*40)
print('{:^40}'.format(' CALCULADORA DE APOSENTADORIA '))
print('-'*40)
print()

dados = {}

dados['nome'] = str(input('INSIRA O NOME: '))
anoNasc = int(input(f'INSIRA O ANO DE NASCIMENTO DE {dados["nome"].upper()}: '))
dados['idade'] = datetime.now().year - anoNasc
dados['CTPS'] = int(input('INSIRA A CARTEIRA DE TRABALHO (0 CASO NÃO TENHA): '))

if dados['CTPS'] != 0:
    dados['anoContratacao'] = int(input(f'INSIRA O ANO DE CONTRATAÇÃO DE {dados["nome"].upper()}: '))
    dados['salario'] = float(input(f'INSIRA O SALÁRIO DE {dados["nome"].upper()}: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['anoContratacao'] + 35) - datetime.now().year)

    print('\n\n')
    print('-' * 130)
    print('{:^130}'.format(' RELATÓRIO FINAL '))
    print('-' * 130)
    print()
    print('-=' * 65)
    print(f'{"NOME":<20}{"IDADE":<15}{"CTPS":<15}{"ANO DE CONTRATAÇÃO":^30}{"SALÁRIO":^20}{"APOSENTADORIA":^20}')
    print('-=' * 65)
    print()
    print(f'{dados["nome"]:<20}{dados["idade"]:<15}{dados["CTPS"]:<15}{dados["anoContratacao"]:^30}{dados["salario"]:^20}{dados["aposentadoria"]:^20}')
    print('-=' * 65)
else:
    print('\n\n')
    print('-'*50)
    print('{:^50}'.format(' RELATÓRIO FINAL '))
    print('-'*50)
    print()
    print('-=' * 25)
    print(f'{"NOME":<20}{"IDADE":^15}{"CTPS":^15}')
    print()
    print(f'{dados["nome"]:<20}{dados["idade"]:^15}{dados["CTPS"]:^15}')
    print('-=' * 25)


"""
    for k, v in dados.items():
    print(f' {k} ===> {v}')
"""
