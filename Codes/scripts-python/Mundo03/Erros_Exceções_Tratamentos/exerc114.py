"""
    CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE PUDIM ESTÁ ACESSÍVEL PELO COMPUTADOR
    USADO.
"""
import urllib
from urllib import request, error
from time import sleep

colors = ('\033[0m',  # 0 - SEM CORES
          '\003[0;31m',  # 1 - VERMELHO
          '\033[0;32m',  # 2 - VERDE
          '\033[0;33m',  # 3 - AMARELO
          '\033[0;34m',  # 4 - AZUL
          '\033[0;35m',  # 5 - ROXO
          '\033[0;30m'  # 6 - BRANCO
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


def testSite(urlSite):
    try:
        site = urllib.request.urlopen(f'http://{urlSite}')
    except urllib.error.URLError:
        imprimirMensagem(f'  >>    O SITE {urlSite} NÃO ESTÁ ACESSÍVEL NO MOMENTO!    <<  ', 1)
        sleep(1.5)
    else:
        imprimirMensagem(f'  >>    CONSEGUI ACESSAR O SITE {urlSite} COM SUCESSO!    <<  ', 2)
        sleep(1)
        imprimirMensagem('  >>    FINALIZANDO SOFTWARE! VOLTE SEMPRE!    <<  ', 4)
        sleep(1.5)


    # try:
    #     urlReq = requests.get(urlSite, timeout=3)
    #     urlReq.raise_for_status()
    # except requests.exceptions.HTTPError as errHttp:
    #     imprimirMensagem(f'  >>    HTTP ERROR ==> {errHttp}    <<  ', 1)
    # except requests.exceptions.ConnectionError as errCon:
    #     imprimirMensagem(f'  >>    CONNECTION ERROR ==> {errCon}    <<  ', 1)
    # except requests.exceptions.Timeout as errTime:
    #     imprimirMensagem(f'  >>    TIMEOUT ERROR ==> {errTime}    <<  ', 1)
    # except requests.exceptions.RequestException as err:
    #     imprimirMensagem(f'  >>    {err}    <<  ', 1)
    # else:
    #     imprimirMensagem(f'  >>    O LINK {urlSite} ESTÁ ONLINE, PODE ACESSAR!    <<  ', 2)


# PROGRAMA PRINCIPAL
testSite('www.ahgora.com')
