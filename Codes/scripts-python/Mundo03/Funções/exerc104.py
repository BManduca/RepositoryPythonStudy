"""
    CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO LEIAINT(), QUE VAI FUNCIONAR DE FORMA SEMELHANTE
    A FUNÇÃO INPUT() DO PYTHON, SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR NÚMERICO.

    EX.:

    n = leiaInt('DIGITE UM VALOR PARA N: ')
"""


def mostraLinha():
    print('-' * 50)
    print()


def imprimir(text):
    print('{:^50}'.format(text))


def leiaInt(msg):

    """
        ==> IMPRIMIR MENSAGEM APÓS VALIDAR O VALOR INTEIRO INSERIDO PELO USUÁRIO.
        :param msg: A MENSAGEM(NO CASO O VALOR) INSERIDO ATRAVÉS DO TELCADO PELO USUÁRIO.
        :return: MENSAGEM IMPRESSA DIZENDO QUAL O VALOR O USUÁRIO INSERIU ATRAVÉS DO TECLADO.
    """

    ok = False
    valor = 0


    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO!! FAVOR INSERIR UM NÚMERO INTEIRO VÁLIDO! \033[m\n')
        if ok:
            break
    return valor


def mensagem(text):
    return text


# programa principal
mostraLinha()
numb = leiaInt('       ==> INSIRA UM VALOR INTEIRO: ')
msg = mensagem(f'VOCÊ ACABOU DE DIGITAR O NÚMERO {numb} ')
imprimir(msg)
print()
mostraLinha()
