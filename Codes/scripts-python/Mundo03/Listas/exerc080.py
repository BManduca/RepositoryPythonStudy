"""
    CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS
    E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O
    SORT()).

    NO FINAL, MOSTRE A LISTA ORDENADA NA TELA
"""

from os import system
import time

print('\n')
print('='*60)
print('{:=^60}'.format(' EXERCÍCIO 80 '))
print('='*60)
print('\n')

valores = []

for v in range(0, 5):
    aux = int(input('INSIRA UM VALOR: '))

    if v == 0 or aux > valores[len(valores)-1]:
        valores.append(aux)
        print(f'Adicionado o valor {aux} no final da lista\n')
    else:
        p = 0
        while p < len(valores):
            if aux <= valores[p]:
                valores.insert(p, aux)
                print(f'Adicionado o valor {aux} na posição {p}\n')
                break
            p += 1

print()
print('='*60)
print(f' LISTAGEM DOS VALORES DIGITADOS: {valores}')
print('='*60)
print()
print('='*60)
print('{:=^60}'.format(' OBRIGADO POR UTILIZAR NOSSO SOFTWARE! '))
print('='*60)

print('\nREINICIANDO SISTEMA EM...')
print()
time.sleep(1)
print('|3|')
time.sleep(1)
print('|2|')
time.sleep(1)
print('|1|')
time.sleep(1)
system('clear')
