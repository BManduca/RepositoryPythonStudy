"""
  REFAÇA O DESAFIO 035 DOS TRIÂNGULOS ACRESCENTANDO O RECURSO DE 
  MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:

  - EQUILÁTERO: TODOS OS LADOS SÃO IGUAIS
  - ISÓSCELES: DOIS LADOS SÃO IGUAIS
  - ESCALENO: TODOS OS LADOS SÃO DIFERENTES
"""

from os import system
import time

print('\n')
print('-'*70)
print('\nPROGRAMA PARA VERIFICAR O TIPO DO TRIÂNGULO\n')
print('-'*70)
print('\n')

print('\nGOSTARIA DE INICIAR O SOFTARE DE VERIFICAÇÃO?\n')
print('-'*17)
print('| S - Para sim |\n| N - Para não |')
print('-'*17)

question = str(input('\nResposta: '))
print('\n')

while question != 'N':

    print('-'*80)
    comp1 = float(input('\nInsira o comprimento da primeira reta: '))
    comp2 = float(input('\nInsira o comprimento da segunda reta: '))
    comp3 = float(input('\nInsira o comprimento da terceira reta: '))

    if (comp1 + comp2 > comp3) and (comp1 + comp3 > comp2) and (comp2 + comp3 > comp1):
        print('\nOS COMPRIMENTOS DE RETA {}, {} e {} FORMAM UM TRIÂNGULO '.format(comp1, comp2, comp3), end='')
        if comp1 == comp2 == comp3:
            print('EQUILÁTERO!\n')
        elif comp1 != comp2 != comp3 != comp1:
            print('ESCALENO!\n')
        else:
            print('ISÓSCELES!\n')
    else:
        print('\nOS COMPRIMENTOS DE RETA {}, {} e {} NÃO FORMAM UM TRIÂNGULO!\n'.format(comp1, comp2, comp3))
    print('-'*80)


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