"""
    CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR SETE VALORES
    NÚMERICOS E CADASTRE-OS EM UMA LISTA ÚNICA QUE MANTENHA
    SEPARADOS OS VALORES PARES E ÍMPARES. NO FINAL
    MOSTRE OS VALORES PARES E ÍMPARES EM ORDEM CRESCENTE.
"""

print('\n')
print('-=-'*20)
print('{:^60}'.format(' EXERCÍCIO 85 '))
print('-=-'*20)


import time

dados = [[], []]
valorAux = 0

for item in range(1, 8):
    valorAux = int(input(f'INSIRA O {item}º VALOR: '))

    if valorAux % 2 == 0:
        dados[0].append(valorAux)
    elif valorAux % 2 != 0:
        dados[1].append(valorAux)
    print()
    # time.sleep(1)


time.sleep(1)

print('-='*30)
print('{:^60}'.format(' RESPOSTA '))
print('-='*30)
print()
print('-='*30)
print(f'LISTA VALORES PARES: {sorted(dados[0])}\nLISTA VALORES ÍMPARES: {sorted(dados[1])}')
print('-='*30)

