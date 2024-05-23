"""
    CRIE UM PROGRAMA QUE TENHA UM TUPLA TOTALMENTE PREENCHIDA
    COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE

    SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20)
    E MOSTRÁ-LO POR EXTENSO.
"""

print('\n')
print('='*60)
print('{:=^60}'.format(' EXERCÍCIO 72 '))
print('='*60)
print('\n')

print('='*60)
print('{:=^60}'.format(' MOSTRAR O NÚMERO ESCOLHIDO POR EXTENSO '))
print('='*60)
print('\n\n')

import time
from os import system

valores = ('zero', 'um', 'dois', 'três', 
           'quatro', 'cinco', 'seis', 'sete', 
           'oito', 'nove', 'dez', 'onze', 'doze', 
           'treze', 'quatorze', 'quinze', 'dezesseis', 
           'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    resposta = ' '
    print('='*60)
    val = int(input(' INSIRA UM VALOR(ENTRE 0 E 20): '))

    if 0 <= val <= 20 or resposta == 'N':
        break

    # else:
    print(' O VALOR INSERIDO NÃO CORRESPONDE AO INTERVALO SOLICITADO..!\n')
    while resposta not in 'SN':
        time.sleep(1)
        resposta = str(input('\n VOCÊ GOSTARIA DE INSERIR NOVAMENTE? [S/N]: ')).upper()
        print('='*60)
        time.sleep(2)
        system('clear')

    # if resposta == 'N':
    #     break
time.sleep(1)
print(f'\n ===> VOCÊ DIGITOU O NÚMERO {valores[val].upper()} <===')
print('='*60)
print('\n')