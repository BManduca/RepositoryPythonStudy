colors = (
    '\033[m',  # 0 - sem cores
    '\033[0;30;41m',  # 1 - VERMELHO
    '\033[0;30;42m',  # 2 - VERDE
    '\033[0;30;43m',  # 3 - AMARELO
    '\033[0;30;44m',  # 4 - AZUL
    '\033[0;30;45m',  # 5 - ROXO
    '\033[7;37;40m',  # 6 - BRANCO
)


def imprimiLinha(cor=0):
    print()
    print(colors[cor])
    print('-=' * 30)
    print()
    print(colors[0])


def imprimiLinha2(mens, cor=0):
    tam = len(mens) + 4

    print()
    print(colors[cor])
    print('~' * tam)
    print(f'{mens}')
    print('~' * tam)
    print()
    print(colors[0])