"""
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o 
valor da casa, o salário do comprador e em quantos 
anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será 
negado.
"""

from os import system
import time

print('-'*50)

print('\n===== EXERCÍCIO 036 ======\n')

print('-'*50)

print('\nPROGRAMA PARA APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO\n')

questionEmprest = str(input('Bom Dia!\nGostaria de iniciar um empréstimo conosco?\n'))

while questionEmprest != 'Nao' and questionEmprest != 'N' and questionEmprest != 'n':

  print('\nFavor inserir seu nome para iniciarmos o processo de empréstimo: ')

  nome = str(input())

  print('\nInsira agora o valor da casa(em reais): ')
  valCasa = float(input())

  print('\nInsira o seu salário mensal do comprador(em reais): ')
  salario = float(input())

  print('\nInsira em quantos anos pretende pagar o empréstimo: ')
  qtdAnos = int(input())
  qtdMeses = qtdAnos * 12

  prestacao = valCasa / qtdMeses

  print('\nValor da prestacao R$ {:.2f}'.format(prestacao))

  valPrest30pSal = salario * 0.3

  if prestacao <= valPrest30pSal:
      print('Valor de empréstimo liberado com sucesso!\nParabéns pela compra de sua nova casa!\n')
  else:
      print('Valor de empréstimo negado!\n')

  questionEmprest = str(input('Gostaria de iniciar uma nova solicitacao de empréstimo conosco?\n'))

print('\nObrigado pelo contato!')
print("\nLimparei a tela em 5 segundos!")
time.sleep(5)

system("clear")
