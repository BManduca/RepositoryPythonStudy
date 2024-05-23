"""
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
    de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

from math import sqrt

print('\n===== EXERCÍCIO 17 ======\n')

def calcHypotenuse(catOposto, catAdjacente):
    hipotenusa = sqrt(catOposto ** 2 + catAdjacente ** 2)
    return hipotenusa

print('-'*100)
catOposto = float(input('\nInsira o comprimento do cateto oposto: '))
catAdjacente = float(input('Insira o comprimeiro do cateto adjacente: '))

'''
    outra forma de resolver a questão atual, é importando o modulo hypot:
    from math import hypot
    hipotenusa = hypot(catetoB, catetoC)
'''

print('\nA hipotenusa vai medir {:.2f}\n'.format(calcHypotenuse(catOposto,catAdjacente)))
print('-'*100)