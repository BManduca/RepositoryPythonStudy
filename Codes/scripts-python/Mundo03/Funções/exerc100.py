"""
    FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES
    CHAMADAS SORTEIA() E SOMAPAR().

    A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCÁ-LOS DENTRO DA LISTA
    E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE OS VALORES PARES SORTEADOS PELA
    FUNÇÃO ANTERIOR.
"""

from random import randint
from time import sleep


def mostraLinha():
    print('-=' * 30)


def mostraLinha2():
    print()
    print('~' * 80)
    print()


def sorteia(lista):
    mostraLinha()
    print()
    print('   SORTEANDO 5 VALORES ==> |  ', end='')
    for aux in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}  ', end='', flush=True)
        sleep(0.5)
    print('|', end='')
    # print(f'   A LISTA SORTEADA ==> {lista}')
    print('\n')
    mostraLinha()
    print()


def somapar(lista):
    soma = 0
    listapar = []

    for v in lista:
        if v % 2 == 0:
            listapar.append(v)
            soma += v
    mostraLinha2()
    print(f' ==> A LISTA DE VALORES PARES: {listapar} \n\n ==> SOMA DOS VALORES PARES => {soma} ')
    mostraLinha2()


numeros = []
sorteia(numeros)
somapar(numeros)
