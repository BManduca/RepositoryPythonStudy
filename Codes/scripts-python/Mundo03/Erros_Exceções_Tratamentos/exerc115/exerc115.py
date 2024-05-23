"""
    CRIE UM PEQUENO SISTEMA MODULARIZADO QUE PERMITE CADASTRAR PESSOAS PELO SEU NOME E IDADE
    EM UM ARQUIVO DE TEXTO SIMPLES.

    O SISTEMA SÓ VAI TER 2 OPÇÕES: CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS.


    OPÇÕES PARA MANIPULAÇÃO DE ARQUIVOS PYTHON

    'r' ==> LEITURA
    'w' ==> ESCRITA. SUBSTITUI O CONTEÚDO DO ARQUIVO EXISTENTE
    'x' ==> ESCRITA. RETORNA ERRO CASO O ARQUIVO JÁ EXISTA
    'a' ==> ESCRITA. INSERE OS NOVOS DADOS NO FINAL DO ARQUIVO
    'b' ==> MONO BINÁRIO
    't' ==> MODO DE TEXTO (PADRÃO)
    '+' ==> ATUALIZAR. TANTO LEITURA QUANTO ESCRITA

"""

from os import system
from time import sleep
from lib.interface import *
from lib.arquivo import *


# PROGRAMA PRINCIPAL
cabecalho('SISTEMA MANDUCA v1.0', 4)

while True:
    resp = menu(['CRIAR ARQUIVO DE DADOS', 'CADASTRAR NOVO COLABORADOR', 'LISTAR COLABORADORES', 'SAIR DO SISTEMA'], 2)
    print()
    sleep(1.5)

    archive = 'colabListManduca.txt'

    if resp == 1:

        if not archiveExist(archive):
            createArchive(archive)
        else:
            msg = f'ARQUIVO {archive.upper()} JÁ FOI CRIADO COM SUCESSO!'
            imprimirMensagem(f'{msg:^60}', 2)

        sleep(4)
        system('clear')
    elif resp == 2:
        imprimirMensagem('NOVO CADASTRO', 4)
        nome = str(input('NOME: '))
        idade = leiaInt('IDADE: ')
        registerCollaborator(archive, nome, idade)
        sleep(3)
        system('clear')
    elif resp == 3:
        # OPÇÃO DE LISTAR O CONTEÚDO DO ARQUIVO
        readArchive(archive)
        sleep(8)
        system('clear')
    elif resp == 4:
        txtExit = 'SAINDO DO SISTEMA.... ATÉ LOGO!'
        cabecalho(f'{txtExit:^60}', 5)
        sleep(1.5)
        break
    else:
        txterror = 'ERRO! INSIRA UMA OPÇÃO VALÍDA!'
        cabecalho(f'{txterror:^60}', 1)
        sleep(2.5)
        system('clear')

