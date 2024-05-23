"""
    Faça um programa que leia a largura e a altura de uma parede em metros, 
    calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada 
    litro de tinta, pinta uma área de 2m²
"""

print('===== EXERCÍCIO 11 ======\n')
largParede = float(input('Largura da parede: '))
altParede = float(input('Altura da parede: '))

areaTotal = largParede * altParede

qtdTinta = areaTotal / 2

print('\nSua parede tem a seguinte dimensão: {} x {}\nA área da parede é de {:.2f}m².\n\nPara pintar essa parede, será utilizado {:.2f}l de tinta.'.format(largParede, altParede, areaTotal, qtdTinta))