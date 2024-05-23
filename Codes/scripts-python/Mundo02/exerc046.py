"""
Faça um programa que mostre em tela uma contagem regressiva para o estouro dos fogos de artifício, indo
10 até 0, com uma pauda de 1 segundos, entre elas.
"""

from time import sleep
# import emoji

anoAtual = int(input('Insira o ano atual: '))

print('\n')
print('-'*78)
print('\n-------------------- CONTAGEM REGRESSIVA PARA O ANO NOVO! --------------------\n')
print('-'*78)
print('\n')

for c in range(10,-1, -1):
    print(c)
    sleep(1)

print('BUM BUUUM POOOW!')
print('\nFELIZ {}\n'.format(anoAtual + 1))
print('\nMUITA PAZ\nSAÚDE\nFESTA\nE\nAMOR!')
# print(emoji.emojize("BUM!\nBUM!\nPOOOW!\n:fireworks:", use_aliases=True))