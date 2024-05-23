"""
DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:
    - A MÉDIA DE IDADE DO GRUPO
    - QUAL É NOME DO HOMEM MAIS VELHO
    - QUANTAS MULHERES TEM MENOS DE 20 ANOS
"""

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeHomemMaisVelho = ''
totalMulherMenos20 = 0

print('-'*40)
print('\n------------- PROGRAMA 056 -------------\n')
print('-'*40)


for p in range(1, 5):
    print('\n')
    print('------- {}º PESSOA ------- \n'.format(p), end='')

    nome = str(input('Nome: ')).strip()

    idade = int(input('Idade: '))

    sexo = str(input('Sexo [M/F]: ')).strip()

    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulherMenos20 += 1

    somaIdade += idade

mediaIdade = somaIdade/4

print('\n')
print('-'*83)
print('\nA Média de idade do grupo é de {} anos\n'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}\n'.format(maiorIdadeHomem, nomeHomemMaisVelho))
print('Ao todo tem {} mulher(es) com menos de 20 anos\n'. format(totalMulherMenos20))
print('-'*83)
