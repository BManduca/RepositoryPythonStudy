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

for i in range(valorInicial):
    if valorInicial%(i+1) == 0:
        cont += 1
        vetDiv.append(i+1)
    else:
        cont

if cont == 2:
    print('\nO número {} é primo, pois é divisível por {}!'.format(valorInicial, vetDiv))
else:
    print('\nO número {} não é primo!, pois é divisível por {}'.format(valorInicial, vetDiv))