"""
    FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA área(), QUE
    RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR( LARGURA E COMPRIMENTO )
    E MOSTRE A ÁREA DO TERRENO
"""


def mostraLinha():
    print()
    print('-='*25)
    print()


def areaTerreno():
    mostraLinha()
    print('{:^50}'.format(' CALCULANDO A ÁREA DE UM TERRENO '))
    mostraLinha()
    larg = float(input('    INSIRA A LARGURA DO TERRENO (m): '))
    compr = float(input('    INSIRA O COMPRIMENTO DO TERRENO (m): '))
    area = larg * compr
    mostraLinha()
    print(f'    A ÁREA DO TERRENO {larg} X {compr} ===> {area:.2f} m²')
    mostraLinha()


areaTerreno()
