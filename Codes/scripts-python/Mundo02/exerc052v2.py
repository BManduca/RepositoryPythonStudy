"""
Faça um programa que leia um número inteiro e diga se ele é um número primo ou não
"""

print('\n')
print('-'*99)
print('\n------------------------ PROGRAMA PARA VERIFICAR SE UM NÚMERO PRIMO OU NÃO ------------------------\n')
print('-'*99)
print('\n')

valorInicial = int(input('Insira um valor inteiro: '))

cont = 0
vetDiv = []

print('')
print('{}Representação: '.format('\033[31m'), end='')
for i in range(1, valorInicial + 1):
    if valorInicial % i == 0:
        cont += 1
        vetDiv.append(i)
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    # print('Números divisiveis por {}: '.format(valorInicial), end='')
    print('{} '.format(i), end='')
print('\n')

if cont == 2:
    print('\nO número {} é primo, pois foi divisível {} vezes, pelos seguintes valores: {}\n'.format(valorInicial, cont, vetDiv))
else:
    print('\nO número {} não é primo, pois foi divisível {} vezes, pelos seguintes valores: {}\n'.format(valorInicial, cont, vetDiv))