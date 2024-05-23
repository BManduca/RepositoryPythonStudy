"""

beecrowd | 1060
Números Positivos
Timelimit: 1


Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos
(desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada

Seis valores, negativos e/ou positivos.

Saída

Imprima uma mensagem dizendo quantos valores positivos foram lidos.

"""

cont = 0

for x in range(6):
    numPos = float(input())
    if numPos > 0:
        cont += 1

print('%i valores positivos' % cont)

