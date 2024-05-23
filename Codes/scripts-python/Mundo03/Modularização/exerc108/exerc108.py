"""
    ADAPTE O CÓDIGO DO DESAFIO 107,CRIANDO UMA FUNÇÃO ADICIONAL CHAMADA MOEDA() QUE
    CONSIGA MOSTRAR OS VALORES COMO UM VALOR MONETÁRIO FORMATADO.
"""

import moeda

moeda.imprimirLinha("   << MANDUCA'S CALCULADORA >>   ")

price = float(input('\n    INSIRA O PREÇO: R$ '))
print()
moeda.imprimirLinha(f' A) ==> A METADE DE {moeda.moeda(price)} É {moeda.moeda(moeda.metade(price))}  ')
moeda.imprimirLinha(f' B) ==> O DOBRO DE {moeda.moeda(price)} É {moeda.moeda(moeda.dobro(price))}   ')
moeda.imprimirLinha(f' C) ==> AUMENTANDO 10%, TEMOS {moeda.moeda(moeda.aumentar(price, 10))}   ')
moeda.imprimirLinha(f' D) ==> DIMINUINDO 13%, TEMOS {moeda.moeda(moeda.diminuir(price, 13))}   ')
print()
moeda.imprimirLinha('   ==> AGRADECEMOS A PREFERÊNCIA!   ')
moeda.imprimirLinha('   ==> VOLTE SEMPRE!  ')
