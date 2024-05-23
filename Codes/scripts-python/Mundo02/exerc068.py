"""
    FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O SEU COMPUTADOR. O JOGO SERÁ 
    INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE 
    ELE CONQUISTOU NO FINAL DO JOGO
"""

from random import randint
from os import system
import time


print('\n')
print('-'*109)
print('\n------------------------------------------------ EXERCÍCIO 68 -----------------------------------------------\n')
print('----------- JOGO PAR OU ÍMPAR CONTRA O COMPUTADOR, COM ESQUEMA DE PARADA QUANDO O JOGADOR PERDER ------------\n')
print('-'*109)
print('\n')

numComputer = numPlayer = qtdPalpites = 0

while True:

    print('OLÁ, EU SOU O SEU COMPUTADOR!\nVAMOS JOGAR PAR OU ÍMPAR?\n\nEU JÁ FIZ MINHA ESCOLHA...AGORA SUA VEZ...\n\nNO 3 REVELAMOS NOSSAS ESCOLHAS...OK?\n\n')

    numComputer = randint(0,10)
    numPlayer = int(input('Vamos lá jogador, insira um valor: '))
    result = numComputer + numPlayer
    option = ' '

    while option not in 'PI':
        option = str(input('PAR OU ÍMPAR? [P - PAR/I - ÍMPAR]: ')).strip().upper()[0]

    print('\n')
    print('| 1 |')
    time.sleep(1)
    print('| 2 |')
    time.sleep(1)
    print('| 3 |')
    time.sleep(1)


    print('\nE AS ESCOLHAS FORAM: \n')

    print('~'*44)
    print(f'COMPUTADOR => {numComputer} VS. JOGADOR => {numPlayer}')
    print(f'A SOMA DOS DOIS VALORES FOI {result}', end='')
    print(' => DEU PAR' if result % 2 == 0 else ' => DEU ÍMPAR')
    print('~'*44)

    if option == 'P':
        if (result % 2 == 0):
            qtdPalpites += 1
            print('\nO JOGADOR VENCEU!\n')
        else:
            print('\nO JOGADOR PERDEU!\n')
            break
    elif option == 'I':
        if (result % 2 == 1):
            qtdPalpites += 1
            print('\nO JOGADOR VENCEU!\n')
        else:
            print('\nO JOGADOR PERDEU!\n')
            break
    print('VAMOS JOGAR NOVAMENTE...\n')
    time.sleep(8)
    system('clear')

print(f'NÚMERO DE VITÓRIAS CONSECUTIVAS DO JOGADOR => {qtdPalpites}\n')
print('\nFINALIZANDO PROGRAMA...!\nVOLTE SEMPRE!')
time.sleep(3)


