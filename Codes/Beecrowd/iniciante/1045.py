"""

beecrowd | 1045
Tipos de Triângulos

Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior
dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos,
sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO

se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES


Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.

"""

a = b = c = 0

N1, N2, N3 = list(map(float, input().split()))

if N1 >= N2 and N1 >= N3:
    a = N1
    b = N2
    c = N3

if N2 >= N1 and N2 >= N3:
    a = N2
    b = N1
    c = N3

if N3 >= N1 and N3 >= N2:
    a = N3
    b = N1
    c = N2

if a < b + c:
    # relacionado ao ângulo do triangulo
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    elif a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    # relacionado aos lados do triangulo
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
