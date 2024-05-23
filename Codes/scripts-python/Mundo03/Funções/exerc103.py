"""
    FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ficha(), QUE RECEBA DOIS PARÂMETROS
    OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU.

    O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO
    NÃO TENHA SIDO INFORMADO CORRETAMENTE.
"""
import os
from os import system
from time import sleep


def mostraLinha(text):
    print('-' * len(text))
    print()


def mostraLinha2():
    print('~' * 40)


def mostraLinha3():
    print('-=' * 40)
    print()


def imprimirResp(text):
    print('{:^80}'.format(text))


def ficha(jog='<desconhecido>', qtdGols=0):

    """
    :param jog: NOME DO JOGADOR QUE VAI ESTAR PRESENTE NA FICHA
    :param qtdGols: QUANTIDADE DE GOLS QUE O JOGADOR MARCOU NO CAMPEONATO
    :return: SEM RETURN
    """

    msg = f'    O jogador {jog} fez {qtdGols} gol(s) no campeonato!    \n'

    print()
    mostraLinha(msg)
    print('{:^50}'.format(msg))
    mostraLinha(msg)


# programa principal

ans = 'S'

while True:

    mostraLinha2()
    print(' {:^40} '.format('CADASTRO FICHA DE JOGADOR'))
    mostraLinha2()

    nome = str(input('\nINSIRA O NOME DO JOGADOR: '))
    gols = str(input(f'INSIRA A QUANTIDADE DE GOLS MARCADOS PELO JOGADOR {nome.upper()}: '))

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    if nome.strip() == '':
        ficha(qtdGols=gols)
    else:
        ficha(nome, gols)

    while True:
        ans = str(input('\nGOSTARIA DE REALIZAR UM NOVO CADASTRO DE FICHA? [S - SIM / N - NÃO] ==> ')).upper()
        print()
        sleep(0.5)

        if ans in 'SN':
            break
        print('RESPOSTA INCORRETA! FAVOR INSERIR S OU N')

    if ans == 'N':

        break

sleep(1)
system('clear')
mostraLinha3()
imprimirResp(' << OBRIGADO POR UTILIZAR NOSSA APLICAÇÃO >> ')
print()
imprimirResp(' << VOLTE SEMPRE! >> ')
print()
sleep(1)
imprimirResp(' [3] ')
print()
sleep(1)
imprimirResp(' [2] ')
print()
sleep(1)
imprimirResp(' [1] ')
print()
sleep(1)
print()
imprimirResp(' << APLICAÇÃO FINALIZADA! >> \n')
mostraLinha3()
