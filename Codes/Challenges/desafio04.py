"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
informações possíveis sobre ela.
"""
print('===== EXERCÍCIO 04 ======\n')

textInput = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(textInput)))
print('Só tem espaços?', textInput.isspace())
print('É um número?', textInput.isnumeric())
print('É alfabético?', textInput.isalpha())
print('É alfanumérico?', textInput.isalnum())
print('Está em maiúsculas?', textInput.isupper())
print('Está em minúsculas?', textInput.islower())
print('Está capitalizado?', textInput.istitle())
