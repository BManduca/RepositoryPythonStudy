

def imprimirTitulo(mens):
    tam = len(mens)

    print('\033[0;36m~\033[m'*tam)
    print(f'\033[0;36m{mens.center(tam)}\033[m')
    print('\033[0;36m~\033[m'*tam)


def imprimiLinha():
    print()
    print('\033[0;32m~\033[m'*55)
    print()


def imprimirRelacao(mens):
    tam = len(mens)
    print(f'\033[0;32m{mens:^{tam}}\033[m')


def aumentar(valor, percent, formato=False):
    result = valor + (valor * percent) / 100

    return result if formato is False else typeMoeda(result)


def diminuir(valor, percent, formato=False):
    result = valor - (valor * percent) / 100

    return result if formato is False else typeMoeda(result)


def dobro(valor, formato=False):
    result = valor * 2

    return result if formato is False else typeMoeda(result)


def metade(valor, formato=False):
    result = valor / 2

    return result if formato is False else typeMoeda(result)


def typeMoeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def resumo(valor, percentAum=10, percentDim=5):
    imprimirTitulo("   << RESUMO DAS OPERAÇÕES >>   ")
    imprimiLinha()
    imprimirRelacao(f'   PREÇO ANALISADO ==> \t{typeMoeda(valor):>25}')
    imprimirRelacao(f'   DOBRO DO PREÇO  ==> \t{dobro(valor, True):>25}')
    imprimirRelacao(f'   METADE DO PREÇO ==> \t{metade(valor, True):>25}')
    imprimirRelacao(f'   {percentAum}% DE AUMENTO  ==> \t{aumentar(valor, percentAum, True):>25}')
    imprimirRelacao(f'   {percentDim}% DE REDUÇÃO  ==> \t{diminuir(valor, percentDim, True):>25}')
    imprimiLinha()

