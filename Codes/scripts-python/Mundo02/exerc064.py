"""
    CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA
    SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO
    DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA
    ENTRE ELES(DESCONSIDERANDO O FLAG)
"""

print('\n')
print('-'*85)
print('\n------------------------ EXERCÍCIO 64 - SOMATÓRIO COM FLAG ------------------------\n')
print('-'*85)
print('\n')

print('~'*45)

somatorio = cont = n = 0

n = int(input('Insira um número [999 para encerrar]: '))

while n != 999:
    somatorio += n
    cont += 1
    n = int(input('Insira um número [999 para encerrar]: '))
print('~'*45)
print('\nVocê digitou {} números e a soma entre eles foi {}'.format(cont, somatorio))
