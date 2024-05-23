"""
    APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:

    A) A SOMA DE TODOS OS VALORES PARES DIGITADOS
    B) A SOMA DOS VALORES DA TERCEIRA COLUNA
    C) O MAIOR VALOR DA MINHA SEGUNDA LINHA
"""

print()
print('-=-'*20)
print('{:^60}'.format(' EXERCÍCIO 87 '))
print('-=-'*20)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maior = somaCol = 0

print()

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'INSIRA O VALOR DA POSIÇÃO [{l+1}][{c+1}]: '))
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]

print()
print('-='*15)
print('{:^30}'.format(' MATRIZ 3X3 '))
print('-='*15)
print()
print('-='*15)
print()
for line in range(0, 3):
    for column in range(0, 3):
        print(f' [ {matriz[line][column]:^4} ] ', end='')
    print()
print()
print('-='*15)

print()
print('*'*30)
print('{:^30}'.format(' => RESPOSTAS <= '))
print('*'*30)
print()
print(f'A) SOMA DE TODOS OS VALORES PARES DIGITADOS: {somaPar}')
for l in range(0, 3):
    somaCol += matriz[l][2]
print(f'B) SOMA DE TODOS OS VALORES DA TERCEIRA COLUNA: {somaCol}')
for l in range(0, 3):
    if column == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'C) O MAIOR VALOR DA SEGUNDA LINHA: {maior}')




