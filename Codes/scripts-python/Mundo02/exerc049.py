"""
    Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""

print('===== EXERCÍCIO 49 ======\n')

numTabuada = int(input('Digite um número para ver a sua tabuada: '))
print('\n')
print('-' * 15)
for i in range(1,11):
    print('\n{} x {:2} = {}'.format(numTabuada, i, (numTabuada * i)))
print('')    
print('-' * 15)
print('\n')
