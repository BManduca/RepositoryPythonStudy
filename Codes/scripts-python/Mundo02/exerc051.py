"""
DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TEMOS 
DESSA PROGRESSÃO
"""

print('\n')
print('-'*90)
print('\n------------------------ PROGRAMA PARA REALIZAR CÁLCULO DE UMA PA ------------------------\n')
print('-'*90)
print('\n')

firstTerm = int(input('INSIRA O PRIMEIRO TERMO DA PA: '))
print('')
razao = int(input('INSIRA A RAZÃO DA PA: '))
print('')

lista = []

decimo = firstTerm + (10-1) * razao

## PA = a1, (a1 + r), (a1 + 2r), (a1 + 3r), (a1 + 4r), (a1 + 5r)....

for i in range(firstTerm, decimo + razao, razao):
    lista.append(i)
    print('{} '.format(i), end='➙ ')
print('ACABOU\n')
# print('\n\n')
# print(lista)
