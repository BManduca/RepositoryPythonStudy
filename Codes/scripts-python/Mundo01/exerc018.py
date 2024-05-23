"""
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
    desse ângulo.
"""

from math import sin, cos, tan, radians

print('\n===== EXERCÍCIO 18 ======\n')

print('-'*100)

ang = float(input('Insira o valor do ângulo que você deseja: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('\nPara o ângulo de {}, o valor do SENO será de {:.2f}'.format(ang, seno))
print('Para o ângulo de {}, o valor do COSSENO será de {:.2f}'.format(ang, cosseno))
print('Para o ângulo de {}, o valor da TANGENTE será de {:.2f}\n'.format(ang, tangente))

print('-'*100)