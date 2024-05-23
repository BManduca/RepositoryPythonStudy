"""
    FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA maior(), QUE RECEBA VÁRIOS
    PARÂMETROS COM VALORES INTEIROS.

    SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR.
"""
import time
from time import sleep
from os import system


def mostraLinha():
    print()
    print('-=' * 30)


def maior(*valInt):
    mostraLinha()
    cont = maior = 0
    print(' => ANALISANDO OS VALORES PASSADOS COMO PARÂMETRO...')
    for v in valInt:
        print(f'  {v} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = v
        elif v > maior:
            maior = v
        cont += 1
    print(' =>  FIM!!')

    print(f'\n   FORAM INFORMADOS {cont} VALORES AO TODO!!')
    print(f'\n   ==> O MAIOR VALOR INFORMADO FOI {maior}!!')
    mostraLinha()


# programa principal
maior(7, 2, 5, 6, 15, 25, 0)
maior(5, 2, 9, 0, 13)
maior(1, 5, 9)
maior(0)
maior()
