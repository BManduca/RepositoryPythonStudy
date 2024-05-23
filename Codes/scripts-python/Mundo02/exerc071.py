"""
    CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO.
    NO ÍNICIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO 
    (NÚMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA
    VALOR SERÃO ENTREGUES.

    OBS.: CONSIDERE QUE O CAIXA POSSUA CÉDULAS DE R$50, R$20, R$10 E R$1. 
"""

print('\n')
print('-'*58)
print('\n---------------------- EXERCÍCIO 71 ----------------------\n')
print('-'*58)
print('\n')

print('='*25)
print('{:^26}'.format(' BANCO MANDUCA '))
print('='*25)
print('\n')

print('='*60)
print(' NOTAS DISPONÍVEIS PARA SAQUE: [200, 100, 50, 20, 10, 5, 2]')
print('='*60)

print('\n')

print('='*40)
valSaque = int(input('QUAL SERIA O VALOR DO SAQUE? R$ '))
valueTotal = valSaque
highValueBanknote = 200
totalBanknote = 0

while True:
    if valueTotal >= highValueBanknote:
        valueTotal -= highValueBanknote
        totalBanknote += 1
    else:
        if totalBanknote > 0:
            print(f'TOTAL DE {totalBanknote} CÉDULA(S) DE R$ {highValueBanknote}')
        if highValueBanknote == 200:
            highValueBanknote = 100
        if highValueBanknote == 100:
            highValueBanknote = 50
        if highValueBanknote == 50:
            highValueBanknote = 20
        elif highValueBanknote == 20:
            highValueBanknote = 10
        elif highValueBanknote == 10:
            highValueBanknote = 5
        elif highValueBanknote == 5:
            highValueBanknote = 2
        totalBanknote = 0
        if valueTotal == 0:
            break


print('='*40)

print('\nVOLTE SEMPRE AO BANCO MANDUCA!\nTENHA UM ÓTIMO DIA!')


