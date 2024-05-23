"""
    CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ 
    VAI PARAR QUANDO O USUÁRIO DIGITAR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL, 
    MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA TOTAL ENTRE ELES(DESCONSIDERANDO
    A FLAG)
"""

print('\n')
print('-'*94)
print('\n---------------------------------------- EXERCÍCIO 66 ----------------------------------------\n')
print('---------- LEITURA DE VALORES DO TECLADO, COM ESQUEMA DE PARADA USANDO FLAG E BREAK ----------\n')
print('-'*94)
print('\n')


soma = contador = n = 0

while True:
    n = int(input('Insira um valor [999 para encerrar]: '))

    if n == 999:
        break

    contador += 1
    soma += n

print(f'\nA soma dos {contador} valores, resultou em: {soma}\n')
print('~'*45)