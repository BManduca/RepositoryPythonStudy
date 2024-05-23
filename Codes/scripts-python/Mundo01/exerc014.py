"""
    Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

print('===== EXERCÍCIO 14 ======\n')

tempCelsius = float(input('Informe a temperatura em ºC: '))

tempFahrenheit = (tempCelsius * 9/5) + 32

print('\nA temperatura de {:.1f}ºC, corresponde a {:.1f}ºF!'.format(tempCelsius, tempFahrenheit))
