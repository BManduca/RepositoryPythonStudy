"""
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
    mostre quantos Dólares ela pode comprar

    Considera:
    US$ 1,00 = R$ 3,27
"""

print('===== EXERCÍCIO 10 ======\n')

vCarteira = float(input('Quanto dinheiro você tem na carteira? \nR$ '))
vRealToDolar = vCarteira / 3.27
vRealtoEuro = vCarteira / 5.55

print('\n-> Com R${:.2f}, você pode comprar US${:.2f}'.format(vCarteira, vRealToDolar))
print('\n-> Com R${:.2f}, você pode comprar €{:.2f}'.format(vCarteira, vRealtoEuro))