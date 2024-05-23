"""
    CRIE UM PROGRAMA QUE TENHA UM TUPLA ÚNICA COM NOMES 
    DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA.

    NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS
    EM FORMA TABULAR
"""

print('\n')
print('='*72)
print('{:=^72}'.format(' EXERCÍCIO 76 '))
print('='*72)
print('\n')


elementos = ('Chaleira Wood 2,5 Litros', 94,
              'Caixa de Som JBL Boombox 3 Bluetooth 80W', 2699, 
              'Torradeira Elétrica Electrolux Experience Inox', 229.90,
              'Smart TV Samsung 43" UHD 4K Tela sem limites 2023', 2049,
              'Suporte para TV ELG Fixo 32" a 75"', 109.90,
              'Suporte de Mesa Articulado até 32"', 241.90,
              'Mochila Dell', 209.90)

# print(elementos)

print('='*72)
print('{:^72}'.format(' LISTAGEM DE PREÇOS '))
print('='*72)
print('\n')
print('='*72)
for elem in range(0, len(elementos)):
    if elem % 2 == 0:
        print(f'{elementos[elem]:.<62}', end='')
    else:
        print(f'R$ {elementos[elem]:>7.2f}')
print('='*72)