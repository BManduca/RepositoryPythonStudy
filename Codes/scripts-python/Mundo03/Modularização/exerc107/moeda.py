

def imprimirLinha(mens):
    tam = len(mens) + 4

    print('~'*tam)
    print(f'{mens}')
    print('~'*tam)


def aumentar(valor, percent):
    result = valor + (valor * percent) / 100
    return result


def diminuir(valor, percent):
    result = valor - (valor*percent)/100
    return result


def dobro(valor):
    result = valor * 2
    return result


def metade(valor):
    result = valor/2
    return result
