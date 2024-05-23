"""
A confederação nacional de natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostra a 
sua categoria, de acordo com a sua idade:

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Júnior
- Até 25 anos: Sênior
- Acima de 25 anos: Master
"""

from os import system
from datetime import date
import time

print('\n')
print('-'*60)
print('\nPROGRAMA PARA VERIFICAÇÃO DE CATEGORIAS DE ATLETAS DA NATAÇÃO\n')
print('-'*60)
print('\n')

print('\nGOSTARIA DE INICIAR O SOFTWARE DE VERIFICAÇÃO DE CATEGORIAS?\n')
print('-'*17)
print('| S - Para sim |\n| N - Para não |')
print('-'*17)

question = str(input('Resposta: '))
print('\n')

while question != 'N':
    print('-'*70)
    name = str(input('\nINSIRA O NOME DO(A) ATLETA: ')).upper()
    anoAtual = date.today().year
    bornYear = int(input('\nINSIRA O ANO DE NASCIMENTO DO(A) ATLETA: '))
    ageAthlete = anoAtual - bornYear
    print('\nO ATLETA {} TEM {} ANOS'.format(name, ageAthlete))

    if ageAthlete <= 9:
        print('\nATLETA: {}\nCATEGORIA: MiRIM\n'.format(name))
    elif ageAthlete > 9 and ageAthlete <= 14:
        print('\nATLETA: {}\nCATEGORIA: INFANTIL\n'.format(name))
    elif ageAthlete <= 19:
        print('\nATLETA: {}\nCATEGORIA: JUNIOR\n'.format(name))
    elif ageAthlete <= 25:
        print('\nATLETA: {}\nCATEGORIA: SENIOR\n'.format(name))
    else:
        print('\nATLETA: {}\nCATEGORIA: MASTER\n'.format(name))
    print('-'*70)

    print('\n\nGOSTARIA DE REALIZAR UMA NOVA VERIFICAÇÃO?\n')
    print('-'*17)
    print('| S - Para sim |\n| N - Para não |')
    print('-'*17)
    question = str(input('\nResposta: '))
    system('clear')

print('\nOBRIGADO POR UTILIZAR MEU SOFTWARE!\n')

print('A TELA SERÁ LIMPA EM 5 SEGUNDOS!\n')
time.sleep(5)

system('clear')

