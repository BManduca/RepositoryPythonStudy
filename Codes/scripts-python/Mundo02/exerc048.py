"""
FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO
DE 1 ATÉ 500
"""

print('\n')
print('-'*123)
print('\n-------------------- PROGRAMA PARA CALCULAR A SOMA DE TODOS OS ÍMPARES E MÚLTIPLOS DE 3 ENTRE 1 E 500  --------------------\n')
print('-'*123)
print('\n')


soma = 0
contador = 0

print('Os números ',end="")
for c in range(1, 501, 2):
    # trazendo os números ímpares pulando de 2 em 2
    # calcula quais os números ímpares são multiplos de 3 usando o resto da divisão
    if c % 3 == 0:
        soma += c
        #somar quantos números foram somados ao total
        contador += 1
        print(' {} '.format(c),end="")
print(' são todos ímpares!\n')

print('\nA soma de todos os {} valores é {}'. format(contador, soma))