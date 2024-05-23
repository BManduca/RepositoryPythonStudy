import math


def mostraLinha():
    print('-='*15)


def mostraLinha2():
    print('-'*30)


def imprimirLista(lista):
    mostraLinha()
    print(f'| {"POS":<10}{"VALOR":>16} |')
    print('|----------------------------|')
    for pos, lista in enumerate(lista):
        print(f'| {pos + 1:<10}{lista:>16.2f} |')
    mostraLinha()


def raiz(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] = math.sqrt(lista[pos])
        pos += 1


def dobraValor(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


def contador(*num):
    for valor in num:
        # print(f'{valor:^14}')
        print(f' {valor} ', end='')
    print(' => FIM ')

#
# print()
# mostraLinha()
# print('{:^40}'.format('LISTAGEM 1: '))
# mostraLinha()
# contador(1, 2, 8, 9, 0)
# mostraLinha()
# print('\n\n')
# mostraLinha()
# print('{:^40}'.format('LISTAGEM 2: '))
# mostraLinha()
# contador(0, 4, 4, 0, 6, 10, 8, 11)
# mostraLinha()


valores = [11, 2, 0, 8, 9, 24]
mostraLinha2()
print('{:^30}'.format(' CALCULANDO DOBRO '))
mostraLinha2()
print()
dobraValor(valores)
imprimirLista(valores)
print('\n\n')
mostraLinha2()
print('{:^30}'.format(' CALCULANDO RAIZ QUADRADA '))
mostraLinha2()
print()
raiz(valores)
imprimirLista(valores)
print()

