"""
    CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:

    [1] SOMAR
    [2] DIMINUIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR
    [6] NOVOS NÚMEROS
    [7] SAIR DO PROGRAMA
"""

from time import sleep

print('\n')
print('{}-'.format('\033[1;32m')*48)
print('\n-------------- CALCULADORA PYTHON --------------\n')
print('-'*48)
print('\n')

valor1 = int(input('INSIRA O PRIMEIRO VALOR: '))
valor2 = int(input('INSIRA O SEGUNDO VALOR: '))

optionMenu = 0
soma = 0
subtr = 0
multi = 0
divid = 0
maior = 0
      
while optionMenu != 7:
    print('''
    --------- MENU ---------
    | [1] SOMAR            |
    | [2] DIMINUIR         |
    | [3] MULTIPLICAR      |
    | [4] DIVIDIR          |
    | [5] MAIOR            |
    | [6] NOVOS NÚMEROS    |
    | [7] SAIR DO PROGRAMA |
    ------------------------
    ''')
    
    optionMenu = int(input('\n>>>>>> Qual a opção escolhida? '))

    if optionMenu == 1:
        soma = valor1 + valor2
        print('\nA SOMA ENTRE {} E {} É {}'.format(valor1, valor2, soma))
    elif optionMenu == 2:
        # subtr = valor1 - valor2
        if valor2 > valor1:
            subtr = valor2 - valor1
            print('\nA SUBTRAÇÃO ENTRE {} E {} É {}'.format(valor2, valor1, subtr))
        else:
            subtr = valor1 - valor2
            print('\nA SUBTRAÇÃO ENTRE {} E {} É {}'.format(valor1, valor2, subtr))
    elif optionMenu == 3:
        multi = valor1 * valor2
        print('\nA MULTIPLICAÇÃO ENTRE {} E {} É {}'.format(valor1, valor2, multi))
    elif optionMenu == 4:
        divid = valor1 / valor2
        print('\nA DIVISÃO ENTRE {} E {} É {:.2f}'.format(valor1, valor2, divid))
    elif optionMenu == 5:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('ENTRE {} E {} O MAIOR VALOR É {}'.format(valor1, valor2, maior))
    elif optionMenu == 6:
        print('\nINFORME OS NÚMEROS NOVAMENTE..')
        valor1 = int(input('INSIRA O PRIMEIRO VALOR: '))
        valor2 = int(input('INSIRA O SEGUNDO VALOR: '))
    elif optionMenu == 7:
        print('FINALIZANDO...')
        sleep(2)
    else:
        print('\nOPÇÃO INSERIDA ESTÁ INCORRETA!\nTENTE NOVAMENTE!')
    print('=-=' * 10)
    sleep(2)
    

print('\nPROGRAMA FINALIZADO COM SUCESSO...!\nVOLTE SEMPRE!\n')
