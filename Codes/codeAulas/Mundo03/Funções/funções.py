import time
from os import system


def mostraLinha():
    print('-' * 30)


def mensagem(textMsg1, textMsg2, textMsg3):
    print()
    print('-=' * 16)
    print('|{:^30}|'.format(textMsg1))
    print('-=' * 16)
    print()
    time.sleep(1)
    print('-=' * 16)
    print('|{:^30}|'.format(textMsg2))
    print('-=' * 16)
    print()
    time.sleep(1)
    print('-=' * 16)
    print('|{:^30}|'.format(textMsg3))
    print('-=' * 16)
    print()
    time.sleep(1)


mensagem1 = str(input('INSIRA A FRASE 1: ')).upper()
time.sleep(1)
mensagem2 = str(input('INSIRA A FRASE 2: ')).upper()
time.sleep(1)
mensagem3 = str(input('INSIRA A FRASE 3: ')).upper()
time.sleep(1)

mensagem(mensagem1, mensagem2, mensagem3)


# mensagem(str(input('INSIRA A MENSAGEM: ')))
# time.sleep(1)
# mensagem(str(input('INSIRA A MENSAGEM: ')))
# time.sleep(1)
# mensagem(str(input('INSIRA A MENSAGEM: ')))

# programa principal
# print()
# mostraLinha()
# print('{:^30}'.format('AULA FUNÇÕES'))
# mostraLinha()
# print()
# mostraLinha()
# print('{:^30}'.format('BRUNNO MANDUCA'))
# mostraLinha()
# print()
# mostraLinha()
# print('{:^30}'.format('MUNDO 03'))
# mostraLinha()
# print()
