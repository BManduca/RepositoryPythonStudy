"""
    CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSÃO 3X3
    E PREENCHA COM VALORES LIDOS PELO TECLADO.

    NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMAÇÃO CORRETA.

"""

print('\n')
print('-=-'*20)
print('{:^60}'.format(' EXERCÍCIO 86 '))
print('-=-'*20)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print()

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'INSIRA UM VALOR NA POSIÇÃO [{l+1}][{c+1}]: '))

print()
print('-='*18)
print('{:^36}'.format(' RESPOSTA '))
print('-='*18)
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f' [ {matriz[l][c]:^4} ] ', end='')
    print()
print()
print('-='*18)
