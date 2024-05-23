"""
  Escreva um programa que faça o computador "pensar" em um número 
  inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
  qual foi o número escolhido pelo computador.

  O programa deverá escrever na tela se o usuário venceu ou 
  perdeu
"""

from random import randint
from time import sleep

print('\n===== EXERCÍCIO 28 ======\n')

print('{}-=-'.format('\033[1;34m') * 20)
print('   VERIFICADOR DE VALOR GERADO PELO COMPUTADOR')
print('-=-' * 20)

print('\n')

numComputer = randint(0, 5)

numUser = int(input('Qual valor escolhido pelo computador? '))
print('\nPROCESSANDO RESPOSTA...')
sleep(3)

if numUser == numComputer:
    print('\nParabéns jogador! Você acertou e ganhou o jogo!\n')
else:
    print('\nCOMPUTER WINS!\nEu pensei no número {} e não no {}!\nInsira uma ficha e tente novamente!\n'.format(numComputer, numUser))
