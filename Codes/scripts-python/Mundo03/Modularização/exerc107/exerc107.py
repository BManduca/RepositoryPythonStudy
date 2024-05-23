"""
    CRIE UM MÓDULO CHAMADO MOEDA.PY QUE TENHAAS FUNÇÕES INCORPORADAS
    AUMENTAR(),  DIMINUIR(), DOBRAR() E METADE()

    FAÇA TAMBÉM UM PROGRAMA QUE IMPORTE ESSE MÓDULO E USE ALGUMAS DESSAS FUNÇÕES
"""

import moeda

moeda.imprimirLinha("    << MANDUCA'S CALCULADORA >>   ")

price = float(input('\n   INSIRA O PREÇO: R$ '))
print()
moeda.imprimirLinha(f' A)  ==> A METADE DE {price} É {moeda.metade(price)}  ')
moeda.imprimirLinha(f' B)  ==> O DOBRO DE {price} É {moeda.dobro(price)}  ')
moeda.imprimirLinha(f' C)  ==> AUMENTANDO 10%, TEMOS {moeda.aumentar(price, 10)}  ')
moeda.imprimirLinha(f' D)  ==> DIMINUINDO 13%, TEMOS {moeda.diminuir(price, 13)}  ')
print()
moeda.imprimirLinha('   ==> AGRADEMOS A PREFERÊNCIA!   ')
moeda.imprimirLinha('   ==> VOLTE SEMPRE!  ')

