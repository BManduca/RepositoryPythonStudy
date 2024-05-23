"""
CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS PARES QUE ESTÃO NO INTERVALO
ENTRE 1 E 50
"""

print('\n')
print('-'*105)
print('\n-------------------- PROGRAMA PARA MOSTRAR NÚMEROS PARES EM UM DETERMINADO INTERVALO --------------------\n')
print('-'*105)
print('\n')

print('Os números [ ',end="")
for c in range(2, 51, 2):
    print(' {} '.format(c),end="")

print(' ] são todos pares!\n')