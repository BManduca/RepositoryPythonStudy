"""
  FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE 
  SE ELE É BISSEXTO.
"""

print('\n===== EXERCÍCIO 32 ======\n')

print('{}-=-'.format('\033[1;34m') * 20)
print('\n   PROGRAMA PARA VERIFICAR SE UM ANO É BISSEXTO!\n')
print('-=-' * 20)

print('\n')

from datetime import date
ano = int(input('Que ano você gostaria de analisar?\nInsira 0 caso queira verificar o ano atual: '))

if ano == 0:
    ano = date.today().year

if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
    print('\nO ano {} é bissexto!\n'.format(ano))
else:
    print('\nO ano {} não é bissexto!\n'.format(ano))