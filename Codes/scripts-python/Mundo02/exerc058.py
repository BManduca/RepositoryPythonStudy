"""
    Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10.
    Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
    foram necessários para vencer.
"""

from random import randint

print('\n')
print('{}-'.format('\033[1;34m')*85)
print('\n-------------- PROGRAMA PARA ADIVINHAR VALOR "PENSADO" PELO COMPUTADOR --------------\n')
print('-'*85)
print('\n')

numComputer = randint(0, 10)

print('OLÁ, EU SOU O COMPUTADOR... ACABEI DE PENSAR EM UM NÚMERO ENTRE 0 E 10...')
print('SERÁ QUE VOCÊ CONSEGUE ADIVINHAR O NÚMERO QUE EU PENSEI? \n')

acertou = False

qtdPalpites = 0

while not acertou:
    numUser = int(input('QUAL O SEU PALPITE? '))
    qtdPalpites += 1
    if numUser == numComputer:
        acertou = True
    else:
        if numUser < numComputer:
            print('MAIS.... TENTE MAIS UMA VEZ..\n')
        elif numUser > numComputer:
            print('MENOS... TENTE MAIS UMA VEZ..\n')
print('PARABÉNS, VOCÊ ACERTOU E VENCEU O JOGO COM {} TENTATIVAS!!\n'.format(qtdPalpites))


