"""
    Crie um programa que leia dois números e mostre a soma entre eles.
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
print('Está capitalizado?', textInput)
