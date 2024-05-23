# for i in range(1,10):
#     print(i)
# print('FIM')

# i = 1

# while i < 10:
#     print(i)
#     i += 1
# print('FIM')

par = 0
impar = 0
vetPar = []
vetImpar = []

val = int(input('Insira o valor inicial: '))

while val != 0:
    val = int(input('Insira o proxímo valor: '))

    if val != 0:
        if val % 2 == 0:
            par += 1
            vetPar.append(val)
        else:
            impar += 1
            vetImpar.append(val)

print('\nVALORES:\n\nPares: {}\nÍmpares: {}\n\nTotalizando {} pares e {} ímpares'.format(vetPar, vetImpar, par, impar))