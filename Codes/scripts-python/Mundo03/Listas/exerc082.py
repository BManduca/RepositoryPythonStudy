"""
    CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR
    EM UMA LISTA.

    DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÀO CONTER
    APENAS VALORES PARES E OS VALORES ÍMPARES DIGITADOS,
    RESPECTIVAMENTE.

    NO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS
"""

print('\n')
print('-=-'*20)
print('{:*^60}'.format(' EXERCÍCIO 82 '))
print('-=-'*20)

valores = []
listPar = []
listImpar = []

while True:
    print()
    # val = int(input('INSIRA UM VALOR: '))

    valores.append(int(input('INSIRA UM VALOR: ')))

    ans = str(input('VOCÊ GOSTARIA DE INSERIR OUTRO VALOR? [S/N]: '))

    while ans not in 'SsNn':
        print('\nRESPOSTA INCORRETA!\n')
        ans = str(input('VOCÊ GOSTARIA DE INSERIR OUTRO VALOR? [S/N]: '))

    if ans in 'Nn':
        break

for num in valores:
    if num % 2 == 0:
        listPar.append(num)
    else:
        listImpar.append(num)


print()
print('='*70)
print(f' LISTA COMPLETA(EM ORDEM): {sorted(valores)}')
print(f' LISTA DE VALORES PARES(EM ORDEM): {sorted(listPar)}')
print(f' LISTA DE VALORES ÍMPARES(EM ORDEM): {sorted(listImpar)}')
print('='*70)
