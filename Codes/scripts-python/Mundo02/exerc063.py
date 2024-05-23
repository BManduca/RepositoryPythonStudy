"""
    ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE NA TELA 
    OS N PRIMEIROS ELEMENTOS DE UM SEQUENCIA DE FIBONACCI
"""

print('\n')
print('-'*72)
print('\n------------------------ SEQUÊNCIA DE FIBONACCI ------------------------\n')
print('-'*72)
print('\n')

print('~'*40)

n = int(input('QUANTOS TERMOS VOCÊ QUER MOSTRAR? '))

termo1 = 0
termo2 = 1

print('~'*40)
print(' ')
print('{} ➙ {} '.format(termo1, termo2), end='➙ ')
contador = 3

while contador <= n:
    termo3 = termo1 + termo2
    print('{} '.format(termo3), end='➙ ')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print('FIM DA SEQUÊNCIA!\n')
