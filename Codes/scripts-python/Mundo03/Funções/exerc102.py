"""
    CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS:
        - O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR O FATORIAL
        - O SEGUNDO CHAMADO SHOW, QUE SERÁ UM VALOR LÓGICO(OPCIONAL) INDICANDO
        SE SERÁ MOSTRADO OU NÃO NA TELA O PROCESSO DE CALCULO DO FATORIAL.
"""

from time import sleep
from os import system


def mostraLinha():
    print('-=' * 40)


def mostraLinha2():
    print('~' * 80)


def fatorial(valor, show=False):

    """
        ==> CALCULAR O FATORIAL DE UM NÚMERO E VERIFICAR SE O CÁLCULO EM SI SERÁ MOSTRADO OU NÃO
    :param valor: O NÚMERO ESCOLHIDO PARA QUE SEJA CALCULADO O SEU FATORIAL!
    :param show: {OPCIONAL} INFORMAÇÃO A SER RECEBIDA E VERIFICAR SE VAI MOSTRAR OU NÃO O CÁLCULO!
    :return: O VALOR DO FATORIAL DE UM VALOR INSERIDO PELO USUÁRIO!
    """
    nFat = 1
    print('  ==> Fatorial: ', end='')
    for contr in range(valor, 0, -1):
        if show:
            print(contr, end='', flush=True)
            sleep(0.5)
            if contr > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        nFat *= contr
    return nFat


# programa principal

resp = 'S'

while resp != 'N':
    mostraLinha2()
    print()
    print('{:^80}'.format(' << APLICAÇÃO PARA CÁLCULO DE FATORIAL! >> \n'))
    mostraLinha2()
    print()
    mostraLinha()
    valFatorial = int(input('\n  INSIRA UM VALOR INTEIRO: '))
    showCalc = bool(input('\n  PARA VER O CÁLCULO DO FATORIAL, DIGITE True, \n  CASO CONTRÁRIO, APERTE "ENTER": '))
    print()
    ans = fatorial(valFatorial, showCalc)
    print(f'{ans}')
    sleep(0.5)

    resp = str(input('\n\n  GOSTARIA DE REALIZAR OUTRO FATORIAL? [S - sim/N - não] -> ')).upper()

    while resp not in 'SN':
        print('\n << RESPOSTA INCORRETA >> ')
        resp = str(input('\n   GOSTARIA DE REALIZAR OUTRO FATORIAL? [S - sim/N - não] -> ')).upper()

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

# help(fatorial)
