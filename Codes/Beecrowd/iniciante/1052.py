"""

beecrowd | 1052
Mês
Timelimit: 1

Leia um valor inteiro entre 1 e 12, inclusive.
Correspondente a este valor, deve ser apresentado como resposta o
mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada

A entrada contém um único valor inteiro.

Saída

Imprima por extenso o nome do mês correspondente ao
número existente na entrada, com a primeira letra em maiúscula.

"""

mes = int(input())

if mes == 1:
    print('January')
elif mes == 2:
    print('February')
elif mes == 3:
    print('March')
elif mes == 4:
    print('April')
elif mes == 5:
    print('May')
elif mes == 6:
    print('June')
elif mes == 7:
    print('July')
elif mes == 8:
    print('August')
elif mes == 9:
    print('September')
elif mes == 10:
    print('October')
elif mes == 11:
    print('November')
elif mes == 12:
    print('December')
