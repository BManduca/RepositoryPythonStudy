"""
    CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSÃO 3X3
    E PREENCHA COM VALORES LIDOS PELO TECLADO.

    NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMAÇÃO CORRETA.

"""

print('\n')
print('-=-'*20)
print('{:^60}'.format(' EXERCÍCIO 86 '))
print('-=-'*20)

matriz = []

print()
for line in range(1, 4):
    # listagem de linha vazia
    linha = []
    for column in range(1, 4):
        linha.append(int(input(f'INSIRA O VALOR DA POSIÇÃO [{line}][{column}]: ')))
    matriz.append(linha)
print()
print('-='*12)
print()
mLinhas = len(matriz)
mColunas = len(matriz[0])

for line in range(mLinhas):
    for column in range(mColunas):
        if column == mColunas - 1:
            print(f' [ {matriz[line][column]:^4} ] ', end='')
        else:
            print(f' [ {matriz[line][column]:^4} ] ', end='')
    print()
print()
print('-='*12)
