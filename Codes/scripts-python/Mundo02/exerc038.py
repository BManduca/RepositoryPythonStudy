"""
Escreva um programa que leia dos números
inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

from os import system
import time

print('\n')
print('-'*60)
print('\nPROGRAMA PARA LEITURA E COMPARAÇÃO DE NÚMEROS INTEIROS\n')
print('-'*60)
print('\n')

question = str(input('\nGostaria de iniciar o processo de comparação?\n'))
print('\n')

while question != 'Nao':

    print('-'*50)
    numb1 = int(input('\nInsira o primeiro valor: '))
    print('\n')
    numb2 = int(input('Insira o segundo valor: '))
    print('\n')

    if numb1 > numb2:
        print('O primeiro valor é maior!\n')
    elif numb2 > numb1:
        print('O segundo valor é maior!\n')
    else:
        print('Não existe valor maior, os dois são iguais!\n')
    print('-'*50)
    
    question = str(input('\nGostaria de realizar uma nova comparação?\n'))
    system("clear")

print('\nObrigado por utilizar meu software!\n')

print('A tela será limpa em 5 segundos!')
time.sleep(5)

system("clear")

