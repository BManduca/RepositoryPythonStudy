"""

beecrowd | 1071
Soma de Impares Consecutivos I
Timelimit: 1

Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos
números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores
ímpares que estão entre os valores fornecidos na entrada que
deverá caber em um inteiro.

"""

x = int(input())
y = int(input())

soma = 0

start = min(x, y)
end = max(x, y)

for i in range(start+1, end):
    if i % 2 != 0:
        soma += i

print(soma)
