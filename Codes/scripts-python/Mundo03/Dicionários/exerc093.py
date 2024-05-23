"""
    CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL.
    O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU.
    DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA.
    NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO
    O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO.
"""

import time

print()
print('-'*100)
print('{:^100}'.format(' SOFTWARE PARA GERENCIAR APROVEITAMENTO DE JOGADORES '))
print('-'*100)
print()

dadosJogador = {}
placarPartidas = []

dadosJogador['nome'] = str(input('INSIRA O NOME DO JOGADOR: '))
totalPartidas = int(input(f'QUANTAS PARTIDAS {dadosJogador["nome"].upper()} JOGOU? '))

print()
if totalPartidas == 0:
    print('\n')
    print('-'*80)
    print('{:^80}'.format(' RELATÓRIO DO GERENCIAMENTO '))
    print('-'*80)
    print()
    print('-='*40)
    print(f'{"NOME JOGADOR":<25}{"QTD PARTIDAS":^20}')
    print('-='*40)
    print()
    print(f'{dadosJogador["nome"]:<25}{totalPartidas:^20}')
    print('-='*40)
else:
    for i in range(0, totalPartidas):
        placarPartidas.append(int(input(f'QUANTOS GOLS {dadosJogador["nome"]} MARCOU NA {i+1} PARTIDA? ')))
        # placarPartidas.append(int(input(f'     - QUANTIDADE DE GOLS MARCADOS NA {i+1}° PARTIDA? ')))

    dadosJogador['qtdGols'] = placarPartidas[:]
    dadosJogador['totalGols'] = sum(placarPartidas)

    print('\n\n')
    print('-'*80)
    print('{:^80}'.format(' RELATÓRIO DO GERENCIAMENTO '))
    print('-'*80)
    print()
    print('-='*32)
    print(f'{"NOME JOGADOR":<25}{"GOLS":^20}{"TOTAL":>15}')
    print()
    print(f'{dadosJogador["nome"]:<25}{dadosJogador["qtdGols"]}{dadosJogador["totalGols"]:>20}')
    print('-='*32)

    # for k, v in dadosJogador.items():
    #     print(f'O CAMPO {k} ===> {v}')

    # print(f'O JOGADOR {dadosJogador["nome"]} JOGOU {len(dadosJogador["qtdGols"])} PARTIDAS. ')

    for i, v in enumerate(dadosJogador['qtdGols']):
        print(f'     => NA PARTIDA {i}° FEZ {v} GOLS.')
    print(f'FOI UM TOTAL DE {dadosJogador["totalPartidas"]} GOLS.')






