"""
    Faça um algoritmo que leia o salário de um funcionário e mostre
    seu novo salário, com 15% de aumento.
"""

print('===== EXERCÍCIO 13 ======\n')
salario = float(input('Qual o salário do funcionário? R$ '))

salarioFinal = salario + (salario * 15/100)

print('\nUm funcionário que ganhava R${:.2f}, com 15% de aumento, passa a ganhar R${:.2f}'.format(salario, salarioFinal))