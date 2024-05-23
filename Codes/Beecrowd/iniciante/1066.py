"""

Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares,
quantos valores digitados foram ímpares, quantos valores digitados foram positivos
e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha,
não esquecendo o final de linha após cada uma.

Exemplo de entrada

-5
0
-3
-4
12

"""

contPar = 0
contImpar = 0
contPos = 0
contNeg = 0

for x in range(5):
    numInt = int(input())

    if numInt % 2 == 0:
        contPar += 1
    else:
        contImpar += 1

    if numInt > 0:
        contPos += 1
    elif numInt < 0:
        contNeg += 1

print('%i valor(es) par(es)' % contPar)
print('%i valor(es) impar(es)' % contImpar)
print('%i valor(es) positivo(s)' % contPos)
print('%i valor(es) negativo(s)' % contNeg)
