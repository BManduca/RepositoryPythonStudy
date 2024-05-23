"""
    FAÇA UM PROGRAMA QUE LEIA NOME E PESO
    DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA.
    NO FINAL MOSTRE:

         A) QUANTAS PESSOAS FORAM CADASTRADAS
         B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS.
         C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES.
"""

print('\n')
print('-=-'*20)
print('{:^60}'.format(' EXERCÍCIO 84 '))
print('-=-'*20)

import time

dados = []
pessoas = []

maiorPeso = menorPeso = 0

while True:
    print()
    dados.append(str(input('NOME: ')))
    dados.append(float(input('PESO: ')))

    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    elif dados[1] > maiorPeso:
        maiorPeso = dados[1]
    elif dados[1] < menorPeso:
        menorPeso = dados[1]

    # gerando uma cópia entre as listas através de um fatiamento
    pessoas.append(dados[:])
    dados.clear()
    print()
    time.sleep(1)

    ans = str(input('GOSTARIA DE INSERIR OUTRO CADASTRO? [S/N]: '))
    print()

    while ans not in 'SsNn':
        print('RESPOSTA INCORRETA!')
        ans = str(input('GOSTARIA DE INSERIR OUTRO CADASTRO? [S/N]: '))

    if ans in 'Nn':
        break

print()
print('-=-'*10)
print('{:^30}'.format(' RESPOSTAS '))
print('-=-'*10)
print()
print('='*70)
print(f'A) TOTAL DE PESSOAS CADASTRADAS: {len(pessoas)} pessoa(s)')
print(f'B) O MAIOR PESO FOI DE {maiorPeso} KG ==> LISTAGEM: ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end='')
# for p in pessoas:
#     print(f'NOME ==> {p[0]} | PESO ==> {p[1]}')
print()
print(f'C) O MENOR PESO FOI DE {menorPeso} KG ==> LISTAGEM: ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')
print()
print('='*70)



