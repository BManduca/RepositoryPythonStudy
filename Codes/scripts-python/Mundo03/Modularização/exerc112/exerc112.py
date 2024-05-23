"""
    DENTRO DO PACOTE UTILIDADESBM QUE CRIAMOS NO DESAFIO 111,
    TEMOS UM MÓDULO CHAMADO DADOS. CRIE UMA FUNÇÃO CHAMADA LEIADINHEIRO()
    QUE SEJA CAPAZ DE FUNCIONAR COMO A FUNÇÃO INPUT(), MAS COM UMA VALIDAÇÃO
    DE DADOS PARA ACEITAR APENAS VALORES QUE SEJAM MONETÁRIOS.
"""


from utilidadesBM import moeda
from utilidadesBM import dados

moeda.imprimirTitulo("   << MANDUCA'S CALCULADORA >>   ")
price = dados.leiaDinheiro('\n\033[0;31m    INSIRA O PREÇO: R$ \033[m')
print()
moeda.resumo(price, 55, 25)
moeda.imprimirTitulo('   ==> AGRADECEMOS A PREFERÊNCIA!   ')
moeda.imprimirTitulo('   ==> VOLTE SEMPRE!   ')

