"""
    FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA 
    VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO. O PROGRAMA SERÁ INTERROMPIDO
    QUANDO O NÚMERO SOLICITADOR FOR NEGATIVO.
"""

print('\n')
print('-'*110)
print('\n------------------------------------------------ EXERCÍCIO 67 ------------------------------------------------\n')
print('--------- MOSTRAR A TABUADA DE CADA VALOR INSERIDO PELO USUÁRIO, COM ESQUEMA DE PARADA USANDO BREAK ----------\n')
print('-'*110)
print('\n')


from os import system
import time

nTabuada = 0


while True:
    nTabuada = int(input('Insira um valor para ver a sua tabuada[Valor negativo para encerrar]: '))

    if nTabuada >= 0:
        print('\n')
        print('~' * 15)
        print(f'\nTABUADA DO {nTabuada}\n')
        for i in range(1,11):
            print(f'{nTabuada} x {i} = {nTabuada*i}')
    else:
        print('\nENCERRANDO O PROGRAMA...\n')
        time.sleep(2)
        break
    print(' ')
    print('~' * 15)
    print('\n')
    time.sleep(5)
    system('clear')
