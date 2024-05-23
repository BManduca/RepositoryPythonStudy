def mostraLinha():
    print('-' * 30)


def somaValores(val1, val2):
    soma = val1 + val2
    print()
    print('-=' * 15)
    print(f'{val1:^7} + {val2:^7} => {soma:^7}')
    print('-=' * 15)
    print()


print()
mostraLinha()
a = int(input('INSIRA O VALOR DE A: '))
b = int(input('INSIRA O VALOR DE B: '))
mostraLinha()
print()
mostraLinha()
c = int(input('INSIRA O VALOR DE C: '))
d = int(input('INSIRA O VALOR DE D: '))
mostraLinha()
print()
mostraLinha()
e = int(input('INSIRA O VALOR DE E: '))
f = int(input('INSIRA O VALOR DE F: '))
mostraLinha()
print()

somaValores(a, b)
somaValores(c, d)
somaValores(e, f)
