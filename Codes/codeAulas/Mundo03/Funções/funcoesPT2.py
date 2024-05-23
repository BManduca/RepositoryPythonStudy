from time import sleep
from os import system


def mostraLinha():
    print('-='*40)


def mostraLinha2():
    print('~'*80)


def fatorial(valor=1):
    nFat = 1

    # forma 1
    # contr = 2
    #
    # while contr <= valor:
    #     nFat *= contr
    #     contr += 1

    # forma 2 -> range(valor inicial, ate onde vai e o passo)
    for contr in range(valor, 0, -1):
        nFat *= contr

    return nFat


resp = 'S'
while resp != 'N':
    mostraLinha2()
    print()
    print('{:^80}'.format(' << APLICAÇÃO PARA CÁLCULO DE FATORIAL! >> \n'))
    mostraLinha2()
    print()
    mostraLinha()
    valFatorial = int(input('\n   INSIRA UM VALOR INTEIRO: '))

    ans = fatorial(valFatorial)

    print(f'   O FATORIAL DE {valFatorial} => {ans}\n')
    sleep(0.5)

    resp = str(input('   GOSTARIA DE CALCULAR OUTRO FATORIAL? [S - SIM/N - NÃO] -> ')).upper()
    print()
    mostraLinha()
    sleep(1.5)
    system('clear')

mostraLinha()
print()
print('{:^80}'.format(' << OBRIGADO POR UTILIZAR NOSSA APLICAÇÃO >> '))
print()
print('{:^80}'.format(' << VOLTE SEMPRE! >> '))
print()
sleep(1)
print('{:^80}'.format(' [3] '))
print()
sleep(1)
print('{:^80}'.format(' [2] '))
print()
sleep(1)
print('{:^80}'.format(' [1] '))
print()
sleep(1)
print()
print('{:^80}'.format(' << APLICAÇÃO FINALIZADA! >> \n'))
mostraLinha()

