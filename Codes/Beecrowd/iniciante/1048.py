"""

    A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


    Salário	Percentual de Reajuste
    0 - 400.00
    400.01 - 800.00
    800.01 - 1200.00
    1200.01 - 2000.00
    Acima de 2000.00

    15%
    12%
    10%
    7%
    4%

    Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o
    índice reajustado, em percentual.

    Entrada
    A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

    Saída
    Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2
    casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

    Exemplo de Entrada	Exemplo de Saída
    400.00

    Novo salario: 460.00
    Reajuste ganho: 60.00
    Em percentual: 15 %

    800.01

    Novo salario: 880.01
    Reajuste ganho: 80.00
    Em percentual: 10 %

    2000.00

    Novo salario: 2140.00
    Reajuste ganho: 140.00
    Em percentual: 7 %


"""

salarioFunc = float(input())
reajuste = 0.0
percentual = 0.0

if salarioFunc > 2000:
    reajuste = (salarioFunc * 0.04) + salarioFunc
    percentual = 4
    print('Novo salario: %.2f' % reajuste)
    print('Reajuste ganho: %.2f' % (reajuste - salarioFunc))
    print('Em percentual: ' + str(percentual) + ' %')
elif 1200.01 <= salarioFunc <= 2000:
    reajuste = (salarioFunc * 0.07) + salarioFunc
    percentual = 7
    print('Novo salario: %.2f' % reajuste)
    print('Reajuste ganho: %.2f' % (reajuste - salarioFunc))
    print('Em percentual: ' + str(percentual) + ' %')
elif 800.01 <= salarioFunc <= 1200:
    reajuste = (salarioFunc * 0.10) + salarioFunc
    percentual = 10
    print('Novo salario: %.2f' % reajuste)
    print('Reajuste ganho: %.2f' % (reajuste - salarioFunc))
    print('Em percentual: ' + str(percentual) + ' %')
elif 400.01 <= salarioFunc <= 800:
    reajuste = (salarioFunc * 0.12) + salarioFunc
    percentual = 12
    print('Novo salario: %.2f' % reajuste)
    print('Reajuste ganho: %.2f' % (reajuste - salarioFunc))
    print('Em percentual: ' + str(percentual) + ' %')
elif 0 <= salarioFunc <= 400:
    reajuste = (salarioFunc*0.15) + salarioFunc
    percentual = 15
    print('Novo salario: %.2f' % reajuste)
    print('Reajuste ganho: %.2f' % (reajuste - salarioFunc))
    print('Em percentual: ' + str(percentual) + ' %')

