"""
  Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com
  o nome "SANTO"
"""
print('\n===== EXERCÍCIO 24 ======\n')

print('{}-=-'.format('\033[1;34m') * 14)
print('   VERIFICADOR DE NOMES DE CIDADES')
print('-=-' * 14)

print('\n')
nomeCidade = str(input('Digite o nome da sua cidade natal: ')).strip()
print('\n')
# nomeDivido = nomeCIDADE.split()

print('-'*100)
print('\n')
print('O nome da cidade inicia com Santo?')
print(nomeCidade[:5].upper() == 'SANTO')
print('\n')
# print(str(nomeDivido[0].find('Santo')))
print('-'*100)