"""
    FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS
    EM UMA LISTA.

    NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO
    E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.
"""

print('\n')
print('='*60)
print('{:=^60}'.format(' EXERCÍCIO 78 '))
print('='*60)
print('\n')

valores = []
bigger = 0
lower = 0

for v in range(0, 5):
    valores.append(int(input(f'Insira um valor na posição {v}: ')))

    if v == 0:
        bigger = lower = valores[v]
    else:
        if valores[v] > bigger:
            bigger = valores[v]
        if valores[v] < lower:
            lower = valores[v]

print('\n')
print('='*30)
print(f' LISTA: {valores}')
print('='*30)
print('\n')
print('=' * 55)
print(f' MAIOR VALOR DA LISTA: {bigger:-<10}> POSIÇÕES: ', end='')
for i,v in enumerate(valores):
    if v == bigger:
        print(f'[{i}] ', end='')
print()
print(f'\n MENOR VALOR DA LISTA: {lower:-<10}> POSIÇÕES: ', end='')
for i, v in enumerate(valores):
    if v == lower:
        print(f'[{i}] ', end='')
print()
print('=' * 55)
