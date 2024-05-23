"""
DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA 
APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O
"""

print('\n')
print('-'*123)
print('\n-------------------------- PROGRAMA PARA LEVAR EM CONSIDERAÇÃO SOMENTE NÚMEROS PARES E SOMÁ-LOS  --------------------------\n')
print('-'*123)
print('\n')


soma = 0
contador = 0
lista = []

for c in range(1,7):
    number = int(input('Insira o {}º valor: '.format(c)))
    print('')
    #calcula os números PARES usando o resto da divisão
    if number % 2 == 0:
        soma += number
        #somar quantos números foram somados ao total
        contador += 1
        lista.append(number)

if contador == 1:
    print('\nO único valor par é: {}\n'.format(lista))
    print('\nA soma do único valor par é {}\n'. format(soma))
else:
    print('\nOs valores pares são: {}\n'.format(lista))
    print('\nA soma dos {} valores é {}\n'. format(contador, soma))