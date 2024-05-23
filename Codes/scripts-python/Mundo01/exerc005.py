"""
    Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
"""

print('===== EXERCÍCIO 05 ======\n')

valorEnt = input('Insira o valor inicial: ')

if valorEnt == '0':
    print('O número inserido foi < 0 >, desta forma, o seu antecessor é um número negativo')
    valorRes = int(valorEnt) + 1
    print('Sucessor: {}'.format(valorRes))
elif valorEnt > '0':
    valorResSuc = int(valorEnt) + 1
    print('Sucessor: {}'.format(valorResSuc))
    valorResAnt = int(valorEnt) - 1
    print('Antecessor: {}'.format(valorResAnt))
