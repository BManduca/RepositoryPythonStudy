"""
    CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA 
    PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER CONTINUAR.
    NO FINAL, MOSTRE:
        - QUANTAS PESSOAS TEM MAIS DE 18 ANOS
        - QUANTOS HOMENS FORAM CADASTRADOS
        - QUANTAS MULHERES TEM MENOS DE 20 ANOS
"""

print('\n')
print('-'*58)
print('\n---------------------- EXERCÍCIO 69 ----------------------\n')
print('-'*58)
print('\n')

from os import system
import time

qtdCadastros = contMaior18 = contHomem = contMulherMenor20 = 0

print('\n')
print('-=-'*20)
print('----------- SOFTWARE PARA CADASTRO DE PESSOAS ------------')
print('-=-'*20)
print('\n')

while True:
    print('\n')
    print('='*35)
    idade = int(input('INSIRA A IDADE DA PESSOA: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('INSIRA O SEXO DA PESSOA [M/F]: ')).strip().upper()[0]

    print('='*35)
    print('\n')

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('GOSTARIA DE CONTINUAR CADASTRANDO? [S/N]: ')).strip().upper()[0]

    if sexo == 'M':
        contHomem += 1

    if sexo == 'F' and idade < 20:
            contMulherMenor20 += 1
    
    if idade > 18:
        contMaior18 += 1

    qtdCadastros += 1

    if resposta == 'N':
        break
    # time.sleep(2)
    # system('clear')
print('\n========== FIM DO PROGRAMA ==========')
print(f'\nTOTAL DE CADASTROS REALIZADOS: {qtdCadastros}\n')
print('-=-'*30)
print(f'\nTOTAL DE PESSOAS CADASTRADAS COM MAIS DE 18 ANOS: {contMaior18}\n')
print(f'TOTAL DE HOMENS CADASTRADOS: {contHomem}\n')
print(f'TOTAL DE MULHERES CADASTRADAS QUE TEM IDADE INFERIOR A 20 ANOS: {contMulherMenor20}\n')
print('-=-'*30)