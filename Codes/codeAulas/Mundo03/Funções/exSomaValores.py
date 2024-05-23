def mostraLinha():
    print('-=' * 25)


# def somaValores(val1, val2):
#     soma = val1 + val2
#     print()
#     print(f' A = {val1} | B = {val2}')
#     print()
#     print('-=' * 15)
#     print('     A SOMA DE A + B = ', end='')
#     print(f'{soma:^2}')
#     print('-=' * 15)
#     print()


# situação de desempacotamento
def somaValores(*valores):
    mostraLinha()
    soma = 0
    for num in valores:
        soma += num
    print(f'  SOMANDO OS VALORES {valores} TEMOS ==> {soma}  ')
    mostraLinha()


# print()
# mostraLinha()
# a = int(input('INSIRA O VALOR DE A: '))
# b = int(input('INSIRA O VALOR DE B: '))
# mostraLinha()
#
somaValores(2, 5, 4, 8)
print()
somaValores(2, 5)
