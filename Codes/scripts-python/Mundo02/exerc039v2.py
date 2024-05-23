"""
faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo de alistamento

    => seu programa também deve mostrar o tempo que falta ou que
    passou do prazo.

"""

from os import system
from datetime import date
import time

print('\n')
print('-'*60)
print('\nPROGRAMA PARA VERIFICAR O ALISTAMENTO MILITAR!\n')
print('-'*60)
print('\n')

print('\nGostaria de iniciar o processo de verificação?\n')
print('-'*17)
print('| S - Para sim |\n| N - Para não |')
print('-'*17)


question = str(input('Resposta: '))
print('\n')

while question != 'N':

    print('-'*80)
    name = str(input('Insira o seu nome: '))
    anoAtual = date.today().year
    anoNasc = int(input('\nInsira o ano que você nasceu: '))
    idade = anoAtual - anoNasc

    if idade > 18:
        tempoAlistamento = idade - 18
        anoAlistamento = anoAtual - tempoAlistamento
        print('\nVocê {}, no ano de {}, já deveria ter se alistado!\n\nSeu alistamento foi em {}.'.format(name, anoAtual, anoAlistamento))
    elif idade < 18:
        tempoAlistamento = 18 - idade
        anoAlistamento = anoAtual + tempoAlistamento
        print('\nVocê {}, no ano de {} ainda não pode se alistar!\n\nSeu alistamento será em {}!'.format(name, anoAtual, anoAlistamento))
    else:
        print('\nParabéns {}!\nEste ano você pode buscar o alistamento!'.format(name))
    print('-'*80)

    print('\n\nGostaria de iniciar um novo processo de verificação?\n')
    print('-'*17)
    print('| S - Para sim |\n| N - Para não |')
    print('-'*17)
    question = str(input('Resposta: '))
    system("clear")


print('\nObrigado por utilizar meu software!\n')

print('A tela será limpa em 5 segundos!')
time.sleep(5)

system("clear")
