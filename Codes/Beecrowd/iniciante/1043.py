"""

beecrowd | 1043
Triângulo

Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

lista = [float(x) for x in input().strip().split(' ')]

função strip remove os espaços em branco no ínicio e no fim de uma string,
retornando uma cópia formatada da string sem os espaços em branco no ínicio e no fim

O método split() retorna uma lista de strings após quebrar a
string dada pelo separador especificado

validando um triângulo:

A < B + C
B < A + C
C < A + B

"""

X, Y, Z = list(map(float, input().split()))

if X < Y + Z and Y < X + Z and Z < X + Y:
    print('Perimetro = %.1f' % (X + Y + Z))
else:
    print('Area = %.1f' % (((X + Y) * Z) / 2))
# for i in range(3):
#     print(lista[i])
