"""
  Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas
    - O nome com todas as letras minúsculas
    - Quantas letras ao todo(sem considerar espaços)
    - Quantas letras tem o primeiro nome
"""

print('\n===== EXERCÍCIO 22 ======\n')

nome = str(input('Insira o seu nome completo: ')).strip()
print('\n')


nomeMaiusc = nome.upper()
nomeMinusc = nome.lower()
nomeSemEspaço = nome.replace(' ', '')
qtdLetrasNome = len(nomeSemEspaço)
dividirNome = nome.split()
tamanhoPrimeiroNome = len(dividirNome[0])

'''
  - forma paliativa de resolver a contagem de espaços
  .format(len(nome) - nome.count(' '))

  - forma paliativa para pegar o qtd de letras do primeiro nome
  .format(nome.find(' '))
'''

print('-'*100)
print('\nSeu nome completo em caixa alta: {}'.format(nomeMaiusc))
print('Seu nome completo em caixa baixa: {}'.format(nomeMinusc))
print('Total de letras do seu nome completo: {}'.format(qtdLetrasNome))
print('O seu primeiro nome é {} e ele tem {} letras\n'.format(dividirNome[0], tamanhoPrimeiroNome))
print('-'*100)