"""
    CRIE UM  PACOTE CHAMADO UTILIDADESBM QUE TENHA DOIS MÓDULOS
    INTERNOS CHAMADOS MOEDA E DADO.

    TRANSFIRA  TODAS AS FUNÇÕES UTILIZADAS NOS DESAFIOS 107, 108, 109 E 110,
    PARA O PRIMEIRO PACOTE E MANTENHA TUDO FUNCIONANDO.
"""

from utilidadesBM import moeda

moeda.imprimirTitulo("   << MANDUCA'S CALCULADORA >>   ")
price = float(input('\n    INSIRA O PREÇO: R$ '))
print()
moeda.resumo(price, 80, 35)
moeda.imprimirTitulo('   ==> AGRADECEMOS A PREFERÊNCIA!   ')
moeda.imprimirTitulo('   ==> VOLTE SEMPRE!   ')

