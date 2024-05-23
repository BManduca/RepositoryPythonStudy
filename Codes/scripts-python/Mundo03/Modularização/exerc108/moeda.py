def imprimirLinha(mens):
    tam = len(mens) + 4

    print('~ ' * tam)
    print(f'{mens}')
    print('~ ' * tam)


def aumentar(valor=0, percent=0):
    result = valor + (valor * percent) / 100
    return result


def diminuir(valor=0, percent=0):
    result = valor - (valor * percent) / 100
    return result


def dobro(valor=0):
    result = valor * 2
    return result


def metade(valor=0):
    result = valor / 2
    return result


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')
