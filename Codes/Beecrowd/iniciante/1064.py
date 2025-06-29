"""
beecrowd | 1064
Positivos e Média
Timelimit: 1
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se
mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada

A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será
positivo.

Saída

O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores
positivos digitados.
"""

cont = 0
totalPos = 0

for x in range(6):
    numPos = float(input())
    if numPos > 0:
        totalPos += numPos
        cont += 1

media = totalPos / cont

print('%i valores positivos' % cont)
print('%.1f' % media)

"""
teste

7
-5
6
-3.4
4.6
12

"""
