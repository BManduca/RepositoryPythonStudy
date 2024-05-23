
"""

    readlines() => pega as linhas do arquivo e joga dentro de uma lista
    read() => le o arquivo inteiro e a ideia é extrair as informações e
    jogar em algum variável ou dispô-las na tela

"""


from lib.interface import *

colors = ('\033[0m',  # 0 - SEM CORES
          '\033[0;31m',  # 1 - VERMELHO
          '\033[0;32m',  # 2 - VERDE
          '\033[0;33m',  # 3 - AMARELO
          '\033[0;34m',  # 4 - AZUL
          '\033[0;35m',  # 5 - ROXO
          '\033[0;30m'  # 6 - BRANCO
          )


def imprimirMensagem(msg, cor=0):
    print()
    print(colors[cor], end='')
    print('~' * 60)
    print(f'{msg:^60}')
    print('~' * 60)
    print(colors[0], end='')
    print()


def archiveExist(archiveName):
    try:
        """ r => leitura(read) && t => texto(text) | abrir arquivo em modo texto """
        archive = open(archiveName, 'rt')
        archive.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createArchive(archiveName):
    try:
        """
            w -> escrita(write)
            t -> texto(text)
            + -> verificação de existência do arquivo, caso não exista, será criado.
        """
        archive = open(archiveName, 'wt+')
        archive.close()
    except:
        msgErro = 'HOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO!'
        imprimirMensagem(f'{msgErro}', 1)
    else:
        msg = f'ARQUIVO {archiveName.upper()} CRIADO COM SUCESSO!'
        imprimirMensagem(msg, 2)


def readArchive(archiveName):

    try:
        archive = open(archiveName, 'rt')
    except:
        msgErro = 'HOUVE UM ERRO AO LER O ARQUIVO!'
        imprimirMensagem(msgErro, 1)
    else:
        msgRegister = 'PESSOAS CADASTRADAS'
        imprimirMensagem(msgRegister, 4)
        for linha in archive:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>20} anos')
        print(archive.read())
    finally:
        archive.close()


def registerCollaborator(archiveName, nomeColab='desconhecido', idadeColab=0):
    try:
        archive = open(archiveName, 'at')
    except:
        imprimirMensagem('HOUVE UM ERRO NA ABERTURA DO ARQUIVO!', 1)
    else:
        try:
            archive.write(f'{nomeColab};{idadeColab}\n')
        except:
            imprimirMensagem('HOUVE UM ERRO NA HORA DE ESCREVER O REGISTRO!', 2)
        else:
            msgNewRegister = f'NOVO REGISTRO DE {nomeColab.upper()} ADICIONADO COM SUCESSO!'
            # print(f'\n{msgNewRegister:^60}\n')
            imprimirMensagem(msgNewRegister, 2)
            archive.close()


