"""

beecrowd | 1070
Seis Números Ímpares
Timelimit: 1

Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares
consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

"""

numInt = int(input())

i = 0

while i < 6:
    if numInt % 2 == 1:
        print(numInt)
        i += 1
    numInt += 1

