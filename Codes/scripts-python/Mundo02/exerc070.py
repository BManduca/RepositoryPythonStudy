"""
    CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS.
    O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO FINAL,
    MOSTRE:
        - QUAL É O TOTAL GASTO NA COMPRA
        - QUANTOS PRODUTOS CUSTAM MAIS DE R$ 1000
        - QUAL É O NOME DO PRODUTO MAIS BARATO
"""

print('\n')
print('-'*58)
print('\n---------------------- EXERCÍCIO 70 ----------------------\n')
print('-'*58)
print('\n')

print('\n')
print('-=-'*21)
print('------------- SOFTWARE PARA CADASTRO DE PRODUTOS --------------')
print('-=-'*21)
print('\n')

nomeLoja = ' CONVENIÊNCIA DO MANDUCA '

totalCompra = qtdValueProdBigger1T = prodValueCheaper = contador = 0
prodCheaper = ''

print('-'*40)
print(f'{nomeLoja:-^40}')
print('-'*40)

while True:
    print('\n')
    print('='*40)
    nameProduct = str(input('INSIRA O NOME DO PRODUTO: '))
    valueProduct = float(input('INSIRA O VALOR DO PRODUTO(R$): '))
    print('='*40)

    contador += 1

    resposta = ' '

    totalCompra += valueProduct

    while resposta not in 'SN':
        resposta = str(input('\nGOSTARIA DE ADICIONAR MAIS UM PRODUTO? [S/N]: ')).strip().upper()[0]

    if valueProduct > 1000:
        qtdValueProdBigger1T += 1

    if contador == 1 or valueProduct < prodValueCheaper:
        prodValueCheaper = valueProduct
        prodCheaper = nameProduct

    if resposta == 'N':
        break
print('\n\n{:=^60}'.format(' FIM DO PROGRAMA '))
print(f'\nO TOTAL DA COMPRA FOI DE R$ {totalCompra:.2f}')
print(f'\nTEMOS {qtdValueProdBigger1T} PRODUTO(S) QUE CUSTA(M) MAIS QUE R$ 1000')
print(f'\nO PRODUTO MAIS BARATO FOI {prodCheaper} QUE CUSTA R$ {prodValueCheaper:.2f}')