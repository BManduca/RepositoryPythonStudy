"""
  Faça um programa que leia uma frase pelo teclado e mostre:
    - quantas vezes aparece a letra 'a'
    - Em que posição ela aparece pela primeira vez
    - Em que posição ela aparece pela última vez
"""
print('\n===== EXERCÍCIO 26 ======\n')

print('{}-=-'.format('\033[1;34m') * 9)
print('   VERIFICADOR DE FRASES')
print('-=-' * 9)

print('\n')

frase = str(input('Insira uma frase: ')).upper().strip()
# frase.count('o', 0, 13)

print('\n')
print('-'*100)
print('\n')
print('A letra A aparece {} vezes na frase'.format(frase.upper().count('A', 0)))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'. format(frase.rfind('A')+1))
print('\n')
print('-'*100)