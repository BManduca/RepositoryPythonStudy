"""
    REESCREVA A FUNÇÃO LEIAINT() QUE FIZEMOS NO DESAFIO 104, INCLUINDO A POSSIBILIDADE DA DIGITAÇÃO
    DE UM NÚMERO DE TIPO INVÁLIDO. APROVEITE E CRIE TAMBÉM UMA FUNÇÃO LEIAFLOAT() COM A MESMA FUNCIONALIDADE.
"""

colors = ('\033[m',  # 0 - sem cores
          '\033[0;31m',  # 1 - vermelho
          '\033[0;32m',  # 2 - verde
          '\033[0;33m',  # 3 - amarelo
          '\033[0;34m',  # 4 - azul
          '\033[0;35m',  # 5 - roxo
          '\033[7;30m'  # 6 - branco
          )


def imprimirMensagem(msg, cor=0):
    tam = len(msg)
    print()
    print(colors[cor], end='')
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)
    print(colors[0], end='')
    print()


def leiaInt(msg):
    """

        ==> IMPRIMIR MENSAGEM APÓS VALIDAR O VALOR INTEIRO INSERIDO PELO USUÁRIO.
        :param msg: A MENSAGEM(NO CASO O VALOR) INSERIDO ATRAVÉS DO TECLADO PELO USUÁRIO.
        :return: MENSAGEM IMPRESSA DIZENDO QUAL O VALOR QUE O USUÁRIO INSERIU ATRAVÉS DO TECLADO.
    """
    while True:
        try:
            valInteiro = int(input(msg))
        except (ValueError, TypeError):
            imprimirMensagem('    ERRO! POR FAVOR, INSIRA UM INTEIRO VÁLIDO!   ', 1)
            # joga para o while novamente
            continue
        except KeyboardInterrupt:
            imprimirMensagem('    ENTRADA DE DADOS INTERROMPIDA PELO USUÁRIO!    ', 1)
            return 0
        else:
            return valInteiro


def leiaFloat(msg):

    """
        ==> IMPRIMIR MENSAGEM APÓS VALIDAR O VALOR FLOAT INSERIDO PELO USUÁRIO.
        :param msg: A MENSAGEM(NO CASO O VALOR) INSERIDO ATRAVÉS DO TECLADO PELO USUÁRIO.
        :return: MENSAGEM IMPRESSA DIZENDO QUAL O VALOR QUE O USUÁRIO INSERIU ATRAVÉS DO TECLADO.
    """

    while True:
        try:
            valFloat = float(input(msg))
        except (ValueError, TypeError):
            imprimirMensagem('    ERRO! POR FAVOR, INSIRA UM FLOAT VÁLIDO!    ', 1)
            continue
        except KeyboardInterrupt:
            imprimirMensagem('    ENTRADA DE DADOS INTERROMPIDA PELO USUÁRIO!    ', 1)
            return 0
        else:
            return valFloat


# programa principal
numInteiro = leiaInt('INSIRA UM VALOR INTEIRO: ')
numFloat = leiaFloat('INSIRA UM VALOR REAL: ')

imprimirMensagem(f'  >>    VALOR INTEIRO DIGITADO ==> {numInteiro} | VALOR REAL DIGITADO ==> {numFloat}    <<  ', 2)
