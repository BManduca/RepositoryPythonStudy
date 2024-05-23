"""
  FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR
  E QUAL É O MENOR.
"""

print('\n===== EXERCÍCIO 33 ======\n')

print('{}-=-'.format('\033[0;33m') * 22)
print('\n   PROGRAMA PARA VERIFICAR QUAL NÚMERO É MAIOR E QUAL É MENOR!\n')
print('-=-' * 22)

print('\n')

numb1 = int(input('{}Insira o primeiro valor: '.format('\033[0;31m')))
numb2 = int(input('{}Insira o segundo valor: '.format('\033[0;30m')))
numb3 = int(input('{}Insira o terceiro valor: '.format('\033[0;36m')))

menor = numb1
maior = numb1

# definindo o menor valor dentre os 3 digitados
if menor > numb2:
    menor = numb2

if menor > numb3:
    menor = numb3

# definindo o maior valor dentre os 3 digitados
if maior < numb2:
    maior = numb2

if maior < numb3:
    maior = numb3

print('\n{}O menor valor é {}\n'.format('\033[0;32m', menor))
print('{}O maior valor é {}\n'.format('\033[0;31m', maior))