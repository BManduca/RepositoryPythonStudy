"""
  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"
  no nome.
"""
print('\n===== EXERCÍCIO 25 ======\n')

print('{}-=-'.format('\033[1;34m') * 9)
print('   VERIFICADOR DE NOMES COMPLETOS')
print('-=-' * 9)

print('\n')

nomeComp = str(input('Digite o seu nome completo: ')).strip()
print('\n')
print('-'*100)
print('\n')
print('O seu nome tem Silva? {}'.format('SILVA' in nomeComp.upper()))
print('\n')
print('-'*100)