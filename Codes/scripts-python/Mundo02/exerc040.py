"""
Crie um programa que leia duas notas de um aluno e calcule 
sua média, mostrando uma mensagem no final de acordo com
a média atingida:

- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
"""

from os import system
import time

print('\n')
print('-'*60)
print('\nPROGRAMA PARA CÁLCULO DE MÉDIA DE UM ALUNO!\n')
print('-'*60)
print('\n')

print('\nGostaria de iniciar o software para cálculo de média?\n')
print('-'*17)
print('| S - Para sim |\n| N - Para não |')
print('-'*17)

question = str(input('Resposta: '))
print('\n')

while question != 'N':

    print('-'*70)
    name = str(input('\nInsira o nome do(a) aluno(a): '))
    nota1 = float(input('\nInsira a nota 1 do(a) aluno(a) {}: '.format(name)))
    nota2 = float(input('\nInsira a nota 2 do(a) aluno(a) {}: '.format(name)))

    media = (nota1 + nota2)/2


    if media < 5.0:
        print('\nO(A) aluno(a) {} está reprovado! Sua média é {:.2f}\n'.format(name, media))
    elif 7 > media >= 5.0:
        print('\nO(A) aluno(a) {} se encontra em recuperação! Sua média é {:.2f}\n'.format(name, media))
    else:
        print('\nParabéns {}!\nVocê está aprovado(a)!\nSua média é {:.2f}\n'.format(name, media))
    print('-'*70)

    print('\n\nGostaria de realizar um novo cálculo de média?\n')
    print('-'*17)
    print('| S - Para sim |\n| N - Para não |')
    print('-'*17)
    question = str(input('Resposta: '))
    system("clear")


print('\nObrigado por utilizar meu software!\n')

print('A tela será limpa em 5 segundos!')
time.sleep(5)

system("clear")