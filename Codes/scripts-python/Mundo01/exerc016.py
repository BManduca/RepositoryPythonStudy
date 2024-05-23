"""
    Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

    Ex.: 
        Digite um número: 6.124
        A parte inteira do número 6.124 é 6.
"""
from math import trunc

print('===== EXERCÍCIO 16 ======\n')
print('-'*100)
valInicial = float(input('\nDigite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}\n'.format(valInicial, trunc(valInicial)))
'''
    para não precisar importar módulos, podemos ver resolver o exerc acima da seguinte forma:
    print('O valor digitado foi {} e a sua porção inteira é {}\n'.format(valInicial, int(valInicial)))
'''
print('-'*100)