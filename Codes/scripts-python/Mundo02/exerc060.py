"""
    FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE
    O SEU FATORIAL

    Ex.:
    5! = 5x4x3x2x1=120
"""

from time import sleep
from math import factorial

print('\n')
print('{}-'.format('\033[1;32m')*48)
print('\n-------------- CALCULANDO FATORIAL --------------\n')
print('-'*48)
print('\n')

# MANEIRA DE RESOLVER USANDO O MÓDULO FACTORIAL
# valFatorial = int(input('INSIRA UM VALOR PARA CALCULAR O FATORIAL: '))
# resultFatorial = factorial(valFatorial)

# MANEIRA TRADICIONAL DE RESOLVER O FATORIAL 
valFatorial = int(input('INSIRA UM VALOR PARA CALCULAR O FATORIAL: '))
resultFatorial = factorial(valFatorial)
#fator nulo de multiplicação
fatorial = 1
cont = valFatorial

print('Calculando o fatorial de {}...\n'.format(valFatorial))
sleep(2)
print('{}! => '.format(valFatorial), end='')
# while cont > 0:
#     print('{}'.format(cont), end='')
#     # print(' x ' if cont > 1 else ' = {}'.format(resultFatorial), end='')
#     print(' x ' if cont > 1 else ' = ', end='')
#     fatorial *= cont
#     cont -= 1
for i in range(1, valFatorial + 1):
    print('{}'.format(i), end='')
    print(' x ' if i < valFatorial else ' = ', end='')
    fatorial *= i
    i += 1
print('{}'.format(fatorial))

