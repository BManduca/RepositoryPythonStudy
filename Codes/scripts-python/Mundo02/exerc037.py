"""
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual a base de conversão:
1 - para binário
2 - para octal
3 - para hexadecimal
"""

from os import system
import time

print('-'*50)
print('\nPROGRAMA PARA CONVERSÃO DE BASE NÚMERICA\n')
print('-'*50)

question = str(input('\nGostaria de iniciar o processo de conversão númerica?\n'))
print('\n')

while question != 'Nao':
    
    print('-'*50)
    print('\nBASES PARA CONVERSÃO:\n')
    print('[1] - Converter para Binário\n')
    print('[2] - Converter para Octal\n')
    print('[3] - Converter para Hexadecimal\n')
    print('-'*50)

    number = int(input('\nInsira um valor inteiro: '))
    valConver = int(input('\nInsira a base de conversão escolhida: '))
    
    if valConver == 1:
        print('\n{} convertido para BINÁRIO é igual a {}\n'.format(number, bin(number)[2:]))
        print('-'*50)
    elif valConver == 2:
        print('\n{} convertido para OCTAL é igual a {}\n'.format(number, oct(number)[2:]))
        print('-'*50)
    elif valConver == 3:
        print('\n{} convertido para HEXADECIMAL é igual a {}\n'.format(number, hex(number)[2:]))
        print('-'*50)
    else:
        print('\nOpção inválida!! Tente novamente!')

    question = str(input('\n\nGostaria de iniciar um novo processo de conversão?\n'))
    system("clear")

print('\nObrigado por usar meu software!')

print("\nLimparei a tela em 5 segundos!")
time.sleep(5)

system("clear")
