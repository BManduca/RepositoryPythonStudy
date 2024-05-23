"""
    DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS
    EM UM TUPLA. NO FINAL MOSTRE:

    A) QUANTAS VEZES APARECEU O VALOR 9.
    B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3.
    C) QUAIS FORAM OS NÚMEROS PARES.
"""

print('\n')
print('='*60)
print('{:=^60}'.format(' EXERCÍCIO 75 '))
print('='*60)
print('\n')

print('='*70)
print('{:^70}'.format(' ADICIONAR VALORES PELO TECLADO EM UM TUPLA '))
print('\n')
print('{:<70}'.format(' ANALISAR VALORES, CONFORME ABAIXO: '))
print('{:<70}'.format(' A) QUANTAS VEZES APARECEU O VALOR 9. '))
print('{:<70}'.format(' B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3. '))
print('{:<70}'.format(' C) QUAIS FORAM OS NÚMEROS PARES. '))
print('='*70)
print('\n')

keyboardValues = (int(input('INSIRA O 1º VALOR: ')), 
                  int(input('INSIRA O 2º VALOR: ')), 
                  int(input('INSIRA O 3º VALOR: ')),
                  int(input('INSIRA O 4º VALOR: ')))
print('\n')

print('='*60)
print(f'A) O VALOR 9 FOI DIGITADO {keyboardValues.count(9)} VEZ(ES)')

if 3 in keyboardValues:
    print(f'B) O PRIMEIRO VALOR 3 FOI DIGITADO NA {keyboardValues.index(3)+1}º POSIÇÃO')
else:
    print('B) O VALOR 3 NÃO FOI ENCONTRADO EM NENHUMA POSIÇÃO!')

print(f'C) NÚMERO(S) PAR(ES) ENCONTRADO(S): ', end='')
for i in keyboardValues:
    if i % 2 == 0:
        print([i], end = ' ')
print(' ')
print('='*60)