"""
    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

print('===== EXERCÍCIO 08 ======\n')

vMetros = float(input('Insira uma distância em metros: '))
vKm = vMetros / 1000
vHm = vMetros / 100
vDam = vMetros / 10
vDm = vMetros * 10
vCent = vMetros * 100
vMilim = vMetros * 1000

print('\nO valor inserido em metros é {} e corresponde a: '.format(vMetros))
print('\nKM = {}km\nHM = {}hm\nDAM = {}dam\nDM = {}dm\nCM = {}cm\nMM = {}mm'.format(vKm, vHm, vDam, vDm, vCent, vMilim))
