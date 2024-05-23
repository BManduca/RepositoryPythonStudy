"""
    CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA

    DEPOIS DISSO:
        A) QUANTOS NÚMEROS FORAM DIGITADOS?
        B) A LISTA DE VALORES ORDENADOS DE FORMA DECRESCENTE
        C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA
"""

print('\n')
print('-=-'*20)
print('{:*^60}'.format(' EXERCÍCIO 81 '))
print('-=-'*20)
print('\n')

valores = []

while True:
    # val = int(input('INSIRA UM VALOR: '))

    valores.append(int(input('INSIRA UM VALOR: ')))

    # if val not in valores:
    #     valores.append(val)
    # else:
    #     print('O VALOR DIGITADO, JÁ FOI INSERIDO NA LISTA!')

    ans = str(input('GOSTARIA DE INSERIR OUTRO VALOR? [S/N]: '))

    while ans not in 'SsNn':
        ans = str(input('GOSTARIA DE INSERIR OUTRO VALOR? [S/N]: '))
    print()

    if ans in 'Nn':
        break

print('='*80)
print(f'A LISTA DOS VALORES DIGITADOS: {valores}')
print('='*80)
print()
print('='*60)
print('{:=^60}'.format(' RESPOSTAS '))
print('='*60)
print()
print('='*80)
print(f'A) QUANTIDADE DE NÚMEROS DIGITADOS: {len(valores)}')
print(f'B) A LISTA DE VALORES ORDENADA DE FORMA DECRESCENTE: {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'C) O VALOR 5 FAZ PARTE DA LISTA!\nE A PRIMEIRA OCORRÊNCIA ESTÁ NA POSIÇÃO {valores.index(5)+1}')
else:
    print('C) O VALOR 5 NÃO FAZ PARTE DA LISTA!')
print('='*80)
