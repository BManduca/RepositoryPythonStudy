"""
beecrowd | 1065
Pares entre Cinco Números
Timelimit: 1

Faça um programa que leia 5 valores inteiros.
Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.


Exemplo de entrada:

7
-5
6
-4
12
"""

cont = 0

for x in range(5):
    numInt = int(input())
    if numInt % 2 == 0:
        cont += 1

print('%i valores pares' % cont)
