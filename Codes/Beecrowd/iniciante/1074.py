"""

beecrowd | 1074
Par ou Ímpar
Timelimit: 1

Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida.
Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN),
ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0),
embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa
deverá imprimir apenas NULL.

Entrada
A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos
de teste. Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

Saída
Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as
letras deverão ser maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.


4
-5
0
3
-4


"""

N = int(input())

for i in range(N):
    aux = int(input())
    if aux < 0:
        if aux % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
    elif aux > 0:
        if aux % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    elif aux == 0:
        print('NULL')



