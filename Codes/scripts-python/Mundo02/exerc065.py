"""
    CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
    NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES E QUAL
    FOI O MAIOR E MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUÁRIO 
    SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES
"""

print('\n')
print('-'*95)
print('\n------------------------ EXERCÍCIO 65 - LER VALORES E CALCULAR A MÉDIA ------------------------\n')
print('-'*95)
print('\n')

print('~'*45)

continuar = 'S'
somatorio = quantValores = media = maior = menor = 0

while continuar in 'Ss':
    n = int(input('\nINSIRA UM NÚMERO: '))
    somatorio += n
    quantValores += 1

    if quantValores == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('DESEJA CONTINUAR? [S/N]: ')).upper().strip()[0]
print(' ')
media = somatorio / quantValores
print('VOCÊ INSERIU UM TOTAL DE {} ELEMENTO(S)\nA SOMA ENTRE ELES É {}\nA MÉDIA DOS VALORES LIDOS É {:.2f}\nO MAIOR VALOR LIDO = {}\nO MENOR VALOR LIDO = {}'.format(quantValores, somatorio, media, maior, menor))