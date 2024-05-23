"""
  CRIE UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE
  NA TELA SE ELE É PAR OU ÍMPAR.
"""

print('\n===== EXERCÍCIO 30 ======\n')

print('{}-=-'.format('\033[1;34m') * 20)
print('   PROGRAMA PARA VERIFICAR SE UM VALOR É PAR OU ÍMPAR!')
print('-=-' * 20)

print('\n')

valor = int(input('\nInsira um número qualquer: '))

if (valor % 2 == 0):
    print('\nO VALOR INSERIDO É PAR!\n')
else:
    print('\nO VALOR INSERIDO É ÍMPAR!\n')