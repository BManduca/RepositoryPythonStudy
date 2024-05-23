"""
    CRIE UM PROGRAMA AONDE O USUÁRIO POSSA DIGITAR
    VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA.
    CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO.
    NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS,
    EM ORDEM CRESCENTE.
"""

print('\n')
print('='*60)
print('{:=^60}'.format(' EXERCÍCIO 79 '))
print('='*60)
print('\n')

valores = []

from os import system
import time

while True:
    v = int(input('Insira um valor: '))

    if v not in valores:
        valores.append(v)
        print('VALOR ADICIONADO A LISTA COM SUCESSO!\n')
    else:
        print('VALOR JÁ EXISTENTE NA LISTA!')

    resp = str((input('Gostaria de continuar? [S/N]: ')))
    while resp not in 'SsNn':
        resp = str((input('\nGostaria de continuar? [S/N]: ')))

    print('\n')
    # system('clear')

    if resp in 'Nn':
        break

print('=' * 45)
print(f' LISTA: {sorted(valores)}')
print('=' * 45)
