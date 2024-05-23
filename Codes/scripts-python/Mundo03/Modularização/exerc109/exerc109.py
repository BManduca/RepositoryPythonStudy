"""
    MODIFIQUE AS FUNÇÕES QUE FORAM CRIADAS NO DESAFIO 107 PARA QUE ELAS
    ACEITEM UM PARÂMETRO A MAIS, INFORMANDO SE O VALOR RETORNADO POR ELES
    VAI SER OU NÃO FORMATADO PELA FUNÇÃO MOEDA(), DESENVOLVIDA NO DESAFIO 108
"""

import moeda

moeda.imprimirLinha("   << MANDUCA'S CALCULADORA >>   ")

price = float(input('\n    INSIRA O PREÇO: R$ '))
percentAum = int(input('    INSIRA O PERCENTUAL PARA A SOMA: '))
percentDim = int(input('    INSIRA O PERCENTUAL PARA A SUBTRAÇÃO: '))

print()
moeda.imprimirLinha(f' A) ==> A METADE DE {moeda.typeMoeda(price)} É {moeda.metade(price, True)}  ')
moeda.imprimirLinha(f' B) ==> O DOBRO DE {moeda.typeMoeda(price)} É {moeda.dobro(price, True)}   ')
moeda.imprimirLinha(f' C) ==> AUMENTANDO {percentAum}%, TEMOS {moeda.aumentar(price, percentAum, True)}   ')
moeda.imprimirLinha(f' D) ==> DIMINUINDO {percentDim}%, TEMOS {moeda.diminuir(price, percentDim, True)}   ')
print()
moeda.imprimirLinha('   ==> AGRADECEMOS A PREFERÊNCIA!   ')
moeda.imprimirLinha('   ==> VOLTE SEMPRE!  ')
