"""
Coordenadas de um Ponto

Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano.
A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos
ou na origem (x = y = 0).

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.

"""

X, Y = list(map(float, input().split()))

if X == 0 and Y == 0:
    print('Origem')
elif X == 0:
    print('Eixo Y')
elif Y == 0:
    print('Eixo X')
elif X > 0 and Y > 0:
    print('Q1')
elif X < 0 < Y:
    print('Q2')
elif X < 0 and Y < 0:
    print('Q3')
elif X > 0 > Y:
    print('Q4')
