"""
  ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO
  DE UM FUNCIONÁRIO E CALCULE O VALOR DO 
  SEU AUMENTO

  -> PARA SALÁRIOS SUPERIORES A R$1.250,00, 
  CALCULE UM AUMENTO DE 10%

  -> PARA OS INFERIORES OU IGUAIS, 
  O AUMENTO É DE 15%
"""

print('\n===== EXERCÍCIO 34 ======\n')

print('{}-=-'.format('\033[0;33m') * 22)
print('\n   PROGRAMA PARA CALCULAR O AUMENTO SALARIAL!\n')
print('-=-' * 22)

print('\n')

nome = str(input('{}Insira o nome do funcionário: '.format('\033[0;37m')))
salario = float(input('\nInsira o salário do funcionário: '))

aumentoMaior1250 = salario * 0.10

aumentoMenor1250 = salario * 0.15

if salario > 1250:
    print('\n{}O aumento salarial de {} será de R${:.2f}, totalizando o novo salário em R${:.2f}\n'.format('\033[0;32m', nome, aumentoMaior1250, salario + aumentoMaior1250))
else:
    print('\n{}O aumento salarial de {} será de R${:.2f}, totalizando o novo salário em R${:.2f}\n'. format('\033[0;32m', nome, aumentoMenor1250, salario + aumentoMenor1250))