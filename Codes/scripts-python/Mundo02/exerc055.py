"""
FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FINAL, MOSTRE QUAL FOI O MAIOR 
E O MENOR PESO LIDOS.
"""

print('\n')
print('-'*83)
print('\n------------- PROGRAMA PARA VERIFICAR MAIOR E MENOR PESO DE UMA LISTA -------------\n')
print('-'*83)
print('\n')

maiorPeso = 0
menorPeso = 0

for iPessoa in range(1,6):
    peso = float(input('PESO DA {}º PESSOA: '.format(iPessoa)))

    if iPessoa == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

print('\n')
print('-'*50)
print('\nMaior peso: {} Kg'.format(maiorPeso))
print('\nMenor peso: {} Kg\n'.format(menorPeso))
print('-'*50)