"""
  Faça um programa que leia um número de 0 9999 e 
  mostre na tela cada um dos dígitos separados

  Ex.:
  Digite um número: 1458

  Unidade:8
  Dezena:5
  Centena:4
  Milhar:1

"""

print('\n===== EXERCÍCIO 23 ======\n')

print('{}-=-'.format('\033[1;34m') * 9)
print('   ANALIZADOR DE NÚMEROS')
print('-=-' * 9)

print('\n')

valorInit = int(input('Insira o valor inicial(0 a 9999): '))

unid = valorInit // 1 % 10
dez =  valorInit // 10 % 10
cen = valorInit // 100 % 10
mil = valorInit // 1000 % 10

print('\n')
print('-'*100)
print('Analisando o valor inserido: \n')
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unid, dez, cen, mil))
print('-'*100)
print('\n')

'''
  resolvendo com uso de string
  valorInit = int(input('Informe o número: '))
  n = str(valorInit)
  print('Analisando o valor inserido: \n')
  print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n[3], n[2], n[1], n[0]))

  mas para esse caso funcionar, será preciso utilizar laços de repetição
'''