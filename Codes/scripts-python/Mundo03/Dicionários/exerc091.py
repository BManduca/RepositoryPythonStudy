"""
    CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS.
    GUARDE ESSES RESULTADOS EM UM DICIONÁRIO. NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM,
    SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO NO DADO.
"""

from random import randint
from operator import itemgetter
import time

print()
print('-'*40)
print('{:^40}'.format(' JOGO DOS DADOS '))
print('-'*40)
print()
jogoDados = {
    'JOGADOR1': randint(1, 6),
    'JOGADOR2': randint(1, 6),
    'JOGADOR3': randint(1, 6),
    'JOGADOR4': randint(1, 6)
}
ranking = []
print('='*32)
print('{:^32}'.format(' LISTAGEM GERAL '))
print('='*32)
print()
print('-='*16)
for k, v in jogoDados.items():
    print(f'{k} tirou {v} no dado ')
print('-=' * 16)

print('\n')

print('='*32)
print('{:^32}'.format(' RANKING DOS JOGADORES '))
print('='*32)
print()
print('-='*16)
print(f'{"No.":<10}{"NOME":<15}{"JOGO":^12}')
print()

ranking = sorted(jogoDados.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1:<10}{v[0]:<15}{v[1]:^12}')
    time.sleep(1)

"""
    for i in range(1, 5):
        jogoDados['nomeJogador'] = str(input(f'INSIRA O NOME DO JOGADOR {i}: '))
        jogoDados['valorDado'] = randint(1, 6)
        # relatorioJogos.append(jogoDados.copy())
        print()
        
    for k, v in jogoDados.items():
        print(f'{k} tirou {v} no dado ')
            
    for item in relatorioJogos:
        print(f'{item["nomeJogador"]:<15}{item["valorDado"]:^12}')
        time.sleep(1)
"""
print('-='*16)

