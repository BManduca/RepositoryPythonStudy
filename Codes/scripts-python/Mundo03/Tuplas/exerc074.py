"""
    CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS 
    E COLOCAR EM UMA TUPLA.
    DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE
    O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA.
"""

print('\n')
print('='*60)
print('{:=^60}'.format(' EXERCÍCIO 74 '))
print('='*60)
print('\n')

print('='*80)
print('{:=^80}'.format(' GERAÇÃO DE NÚMEROS ALEATÓRIOS PARA ADICIONAR EM UMA TUPLA '))
print('='*80)
print('\n')

from random import randint

valoresAletorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('='*42)
print(' OS VALORES SORTEADOS FORAM: ', end='')
for n in valoresAletorios:
    print(f'{n} ', end='')
print(' ')
print('\n')
print(f' => O MAIOR VALOR SORTEADO: {max(valoresAletorios)}')
print(f' => O MENOR VALOR SORTEADO: {min(valoresAletorios)}')
print('='*42)



