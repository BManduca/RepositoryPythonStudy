

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
    """
        --> CALCULA O AUMENTO DE UM DETERMINADO PREÇO,
        RETORNANDO O RESULTADO COM OU SEM FORMATAÇÃO.

        :param valor: O VALOR AO QUAL SERÁ APLICADO A OPERAÇÃO DE AUMENTO
        :param percent: VALOR DE PORCENTAGEM QUE SERÁ APLICADO O AUMENTO OU DIMINUIÇÃO
        :param formato: PARÂMETRO PARA SINALIZAR SE A SAÍDA SERÁ FORMATADA OU NÃO
        :return: O VALOR FINAL COM O REAJUSTE APLICADO COM OU SEM A FORMATAÇÃO.
    """

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


def resumo(valor, percentAum=0, percentDim=0):
    imprimirTitulo("   << RESUMO DAS OPERAÇÕES >>   ")
    imprimiLinha()
    imprimirRelacao(f'   PREÇO ANALISADO ==> {typeMoeda(valor):>25}')
    imprimirRelacao(f'   DOBRO DO PREÇO  ==> {dobro(valor, True):>25}')
    imprimirRelacao(f'   METADE DO PREÇO ==> {metade(valor, True):>25}')
    imprimirRelacao(f'   {percentAum}% DE AUMENTO  ==> {aumentar(valor, percentAum, True):>25}')
    imprimirRelacao(f'   {percentDim}% DE REDUÇÃO  ==> {diminuir(valor, percentDim, True):>25}')
    imprimiLinha()

