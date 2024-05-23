"""

beecrowd | 1072
Intervalo 2
Timelimit: 1

Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X
que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e
quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que
indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).


Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos
valores estão fora (out) do intervalo.

"""

N = int(input())

# contador que estao dentro do intervalo
inn = 0
# contador que estao fora do intervalo
out = 0

for i in range(N):

    X = int(input())

    if 10 <= X <= 20:
        inn += 1
    else:
        out += 1

print('%i in' % inn)
print('%i out' % out)

