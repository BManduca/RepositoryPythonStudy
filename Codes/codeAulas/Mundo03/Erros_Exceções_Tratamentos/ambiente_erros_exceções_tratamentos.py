colors = ('\033[m',      # 0 - sem cores
          '\033[0;31m',  # 1 - vermelho
          '\033[0;32m',  # 2 - verde
          '\033[0;33m',  # 3 - amarelo
          '\033[0;34m',  # 4 - azul
          '\033[0;35m',  # 5 - roxo
          '\033[7;30m'   # 6 - branco
          )


def imprimirMensagem(msg, cor=0):
    tam = len(msg)
    print()
    print(colors[cor], end='')
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    print(colors[0], end='')
    print()


try:
    a = int(input('INSIRA O NUMERADOR: '))
    b = int(input('INSIRA O DENOMINADOR: '))

    res = a / b
# except Exception as erro:
#     imprimirMensagem('    ERRO! O PROBLEMA ENCONTRADO FOI {erro.__class__} =(    ', 1)
except (ValueError, TypeError):
    imprimirMensagem('    TIVEMOS UM PROBLEMA COM OS TIPOS DE DADOS QUE VOCÊ DIGITOU!    ', 1)
except ZeroDivisionError:
    imprimirMensagem('    NÃO É POSSÍVEL DIVIDIR UM NÚMERO POR ZERO!    ', 1)
except KeyboardInterrupt:
    imprimirMensagem('    O USUÁRIO PREFERIU NÃO INFORMAR OS DADOS!    ', 1)
except Exception as erro:
    imprimirMensagem(f'    O ERRO ENCONTRADO FOI {erro.__cause__}    ', 1)
else:
    imprimirMensagem(f'    O resultado da divisão é {res:.2f}    ', 2)
finally:
    imprimirMensagem('    VOLTE SEMPRE! MUITO OBRIGADO!    ', 4)