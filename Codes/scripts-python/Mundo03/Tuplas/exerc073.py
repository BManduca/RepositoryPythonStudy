"""
    CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS
    DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM
    DA COLOCAÇÃO. DEPOIS, MOSTRE:
        A) APENAS OS CINCO PRIMEIROS COLOCADOS
        B) OS ÚLTIMOS 4 COLOCADOS DA TABELA
        C) OS TIMES EM ORDEM ALFABÉTICA
        D) EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DO GRÊMIO?
"""

print('\n')
print('='*60)
print('{:=^60}'.format(' EXERCÍCIO 73 '))
print('='*60)
print('\n')

print('='*60)
print('{:=^60}'.format('  TABELA DO BRASILEIRÃO '))
print('='*60)
print('\n')

brasileirao = ('Botafogo','Flamengo','Palmeiras','Grêmio',
               'Fluminense','Bragantino','Athletico-PR','São  Paulo',
               'Cuiába','Cruzeiro','Fortaleza','Internacional',
               'Atlético-MG','Corinthians','Santos','Goiás',
               'Bahia','Coritiba','América-MG','Vasco da Gama')

print('{:=^110}'.format(' RELAÇÃO BRASILEIRÃO '))
print(f'\n A) OS PRIMEIROS CINCO COLOCADOS DO BRASILEIRÃO: {brasileirao[:5]}')
print(f' B) OS ÚLTIMOS QUATRO COLOCADOS DO BRASILEIRÃO: {brasileirao[-4:]}')
print(f' C) BRASILEIRÃO EM ORDEM ALFABÉTICA: {sorted(brasileirao)}')
print(f' D) O GRÊMIO ESTÁ NA {brasileirao.index("Grêmio")+1}ª POSIÇÃO\n')
print('='*110)