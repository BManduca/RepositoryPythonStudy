"""
DESENVOLVA UMA LÓGICA QUE LEIA O PESO E 
A AULTURA DE UMA PESSOA, CALCULE SEU IMC E 
MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:

- ABAIXO DE 18.5: ABAIXO DO PESO
- ENTRE 18.5 E 25: PESO IDEAL
- 25 ATÉ 30: SOBREPESO
- 30 ATÉ 40: OBESIDADE
- ACIMA DE 40: OBESIDADE MÓRBIDA
"""

from os import system
import time

print('\n')
print('-'*70)
print('\nPROGRAMA PARA CÁLCULO E VERIFICAÇÃO DO IMC\n')
print('-'*70)
print('\n')

print('-'*40)
print('QUANDRO PARA VERIFICAÇÃO IMC: ')
print(' ==> ABAIXO DE 18.5: ABAIXO DO PESO')
print(' ==> ENTRE 18.5 E 25: PESO IDEAL')
print(' ==> ACIMA DE 25 ATÉ 30: SOBREPESO')
print(' ==> ACIMA DE 30 ATÉ 40: OBESIDADE')
print(' ==> ACIMA DE 40: OBESIDADE MÓRBIDA')
print('-'*40)



print('\nGOSTARIA DE INICIAR O SOFTWARE DE CÁLCULO DO IMC?\n')
print('-'*17)
print('| S - Para sim |\n| N - Para não |')
print('-'*17)

question = str(input('\nResposta: '))
print('\n')

while question != 'N':

    print('-'*70)
    name = str(input('\nINSIRA O NOME DO PACIENTE: ')).upper()
    peso = float(input('\nINSIRA O PESO DO PACIENTE: '))
    altura = float(input('\nINSIRA A ALTURA DO PACIENTE: '))
    imc = peso / (altura ** 2)

    print('\nO IMC do {} é {:.1f}\n'.format(name, imc))

    if imc < 18.5:
        print('\n ==> ABAIXO DO PESO\n')
    elif 18.5 <= imc < 25:
        print('\n ==> PESO IDEAL\n')
    elif 25 <= imc < 30:
        print('\n ==> SOBREPESO\n')
    elif 30 <= imc < 40:
        print('\n ==> OBESIDADE\n')
    else:
        print('\n ==> OBESIDADE MÓRBIDA\n')
    print('-'*70)


    print('\n\nGOSTARIA DE REALIZAR UM NOVO CÁLCULO?\n')
    print('-'*17)
    print('| S - Para sim |\n| N - Para não |')
    print('-'*17)
    question = str(input('\nResposta: '))
    system('clear')

print('\nOBRIGADO POR UTILIZAR MEU SOFTWARE!\n')

print('A TELA SERÁ LIMPA EM 5 SEGUNDOS!\n')
time.sleep(5)

system('clear')