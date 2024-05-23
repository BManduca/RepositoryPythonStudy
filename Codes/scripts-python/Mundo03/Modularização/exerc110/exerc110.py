"""
    ADICIONE AO MÓDULO MOEDA.PY CRIADO NOS DESAFIOS ANTERIORES, UMA
    FUNÇÃO CHAMADA RESUMO(),QUE MOSTRE NA TELA ALGUMAS INFOMAÇÕES GERADAS
    PELAS FUNÇÕES QUE JÁ TEMOS NO MÓDULO CRIADO ATÉ AQUI.
"""

import moeda

moeda.imprimirTitulo("   << MANDUCA'S CALCULADORA >>   ")

price = float(input('\n>>  INSIRA O PREÇO: R$ '))
print()
moeda.resumo(price, 20, 12)
moeda.imprimirTitulo('   ==> AGRADECEMOS A PREFERÊNCIA!   ')
moeda.imprimirTitulo('   ==> VOLTE SEMPRE!   ')
