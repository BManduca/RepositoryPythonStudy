"""

beecrowd | 1059
Números Pares
Timelimit: 1


Faça um programa que mostre os números pares entre 1 e 100, inclusive.

Entrada

Neste problema extremamente simples de repetição não há entrada.

Saída

Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

"""

start = 1
end = 100

for x in range(start, end+1):
    if x % 2 == 0:
        print(x)
