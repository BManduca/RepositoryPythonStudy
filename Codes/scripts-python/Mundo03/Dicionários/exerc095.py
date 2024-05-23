"""
    APRIMORE O DESAFIO 093 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES,
    INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTO
    DE CADA JOGADOR.
"""

import time
from os import system

print()
print('-' * 100)
print('{:^100}'.format(' SOFTWARE PARA GERENCIAR APROVEITAMENTO DE JOGADORES '))
print('-' * 100)
print()

relacaoTime = []

dadosJogador = {}
placarPartidas = []

print()

while True:
    """
        apagando os dados do jogador, antes de ler os dados de um jogador  
    """
    dadosJogador.clear()
    dadosJogador['nome'] = str(input('INSIRA O NOME DO JOGADOR: '))
    print()
    totalPartidas = int(input(f' ==> QUANTAS PARTIDAS {dadosJogador["nome"].upper()} JOGOU? '))
    print()
    placarPartidas.clear()
    for i in range(0, totalPartidas):
        placarPartidas.append(
            int(input(f' ==> QUANTOS GOLS {dadosJogador["nome"].upper()} MARCOU NA {i + 1} PARTIDA? ')))
        # placarPartidas.append(int(input(f'     - QUANTIDADE DE GOLS MARCADOS NA {i+1}° PARTIDA? ')))

    dadosJogador['qtdGols'] = placarPartidas[:]
    dadosJogador['totalGols'] = sum(placarPartidas)

    """
        após ler todas as infos do jogador, vamos jogar dentro da relação de times, fazendo uma cópia 
        dos dados do jogador, que é um dicionário, fazendo um copy, pois não podemos fazer fatiamento 
        dentro de dicionários     
    """
    relacaoTime.append(dadosJogador.copy())

    while True:
        print('\n\n')
        resp = str(input('GOSTARIA DE ADICIONAR OUTRO JOGADOR? [S/N]: ')).upper()[0]

        if resp in 'SN':
            break
        else:
            print('ERRO!\nRESPONSA SOMENTE COM S OU N!')

    time.sleep(1)
    system('clear')

    if resp == 'N':
        break
    # time.sleep(1)
    # system('clear')

print('\n\n')
print('-' * 80)
print('{:^80}'.format(' RELATÓRIO DO GERENCIAMENTO '))
print('-' * 80)
print()
print('-=' * 30)
print('COD ', end='')
for i in dadosJogador.keys():
    print(f'{i.upper():<15}', end='')
print()
print('-=' * 30)
for i, v in enumerate(relacaoTime):
    print(f'{(i + 1):>3}º ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)

while True:
    print('\n\n')
    print('-' * 60)
    print()
    busca = int(input('INSIRA UM JOGADOR PARA SER VERIFICADO\n(999 -> PARA ENCERRAR): '))

    if busca == 999:
        print('\n\n')
        time.sleep(1)
        system('clear')
        print('-' * 60)
        print('{:^40}'.format(' << ENCERRANDO APLICAÇÃO >> '))
        print('{:^40}'.format(' << VOLTE SEMPRE! >> '))
        print('-' * 60)

        break

    if busca >= len(relacaoTime):
        print(f'\nERRO!! NÃO EXISTE JOGADOR COM O CÓDIGO {busca}!')
    else:
        print('\n')
        print(f' -- LEVANTAMENTO DO JOGADOR {relacaoTime[busca]["nome"]}: ')
        for i, g in enumerate(relacaoTime[busca]['qtdGols']):
            print(f'   No jogo {i + 1} fez {g} gol(s)!')
        time.sleep(1)
    print()
    print('-' * 60)
