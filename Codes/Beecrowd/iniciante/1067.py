"""

beecrowd | 1067
Números Ímpares
Timelimit: 1

Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares
de 1 até X, um valor por linha, inclusive o X, se for o caso.

Entrada
O arquivo de entrada contém 1 valor inteiro qualquer.

Saída
Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

"""

numInt = int(input())

for numInt in range(1, numInt+1):
    if numInt % 2 == 1:
        print(numInt)


