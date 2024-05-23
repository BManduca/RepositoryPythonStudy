"""
    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
"""
import math

print('===== EXERCÍCIO 06 ======\n')

valorEnt = int(input('Digite um número: '))
vDobro = valorEnt * 2
vTriplo = valorEnt * 3
vRaizQuadrada = valorEnt ** (1/2)
#math.pow(valorEnt, 1/2)

print('\nValor inicial inserido: {}\n'.format(valorEnt))
print('O dobro de {} é {}'.format(valorEnt, vDobro))
print('O triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}'.format(valorEnt, vTriplo, valorEnt, vRaizQuadrada))
