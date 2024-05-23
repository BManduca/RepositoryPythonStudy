"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente,
uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

lista => []
tupla => ()
dicionário => {}

"""

N1, N2, N3 = list(map(int, input().split()))
# lista = [int(x) for x in input().strip().split(' ')]

lista = [N1, N2, N3]
listaOrdered = lista[:]
listaOrdered.sort()

for i in range(3):
    print(listaOrdered[i])
print()
for i in range(3):
    print(lista[i])
