def imprimirLinha(mens):
    tam = len(mens) + 4

    print('~' * tam)
    print(f'{mens}')
    print('~' * tam)


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
