"""
  Faça um programa que leia o nome completo de uma pessoa, mostrando
  em seguida o primeiro e o último nome separadamente
  Ex.: Ana Maria de Souza
  primeiro: Ana
  último: Souza
"""
print('\n===== EXERCÍCIO 27 ======\n')

print('{}-=-'.format('\033[1;34m') * 9)
print('   VERIFICADOR DE PRIMEIRO E ÚLTIMO NOME')
print('-=-' * 9)

print('\n')

nomeComp = str(input('Digite seu nome completo: ')).strip()
nomeDivido = nomeComp.split()

print('\n')
print('-'*100)
print('Muito prazer em te conhecer {}!'.format(nomeComp))
print('Seu primeiro nome é: {}'.format(nomeDivido[0]))
print('Seu ultimo nome é: {}'.format(nomeDivido[len(nomeDivido)-1]))
print('-'*100)