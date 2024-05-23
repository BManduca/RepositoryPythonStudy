"""
    CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE
    TUDO EM UMA LISTA COMPOSTA. NO FINAL, MOSTRE UM BOLETIM CONTENDO
    A MÉDIA DE CADA UM E PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS
    DE CADA ALUNO INDIVIDUALMENTE.
"""
import os
import time
from os import system

print()
print('-'*60)
print('{:^60}'.format(' EXERCÍCIO 89 '))
print('-'*60)

listaAlunos = []

while True:
    print('-=' * 30)
    print('{:^60}'.format(' CADASTRO ALUNO E NOTAS '))
    print('-=' * 30)
    resposta = ' '
    print()
    print('-='*28)
    nome = str(input('NOME DO ALUNO(A): '))
    print()
    n1 = float(input(f'PRIMEIRA NOTA DO ALUNO(A) {nome.upper()}: '))
    time.sleep(1)
    n2 = float(input(f'SEGUNDA NOTA DO ALUNO(A) {nome.upper()}: '))
    media = (n1 + n2) / 2
    listaAlunos.append([nome, [n1, n2], media])
    print('-=' * 28)

    print()
    resposta = str(input('GOSTARIA DE INSERIR O REGISTRO DE OUTRO ALUNO(A)? [S/N]: ')).upper()
    time.sleep(1)

    while resposta not in 'SN':
        resposta = str(input('A RESPOSTA ESTÁ INCORRETA! GOSTARIA DE TENTAR NOVAMENTE? [S/N]: ')).upper()
        time.sleep(1)
    print()
    system('clear')

    if resposta == 'N':
        break

print()
# print(listaAlunos)
print('-'*60)
print('{:^60}'.format(' BOLETIM FINAL '))
print('-'*60)
print()
print('-='*20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*20)
for i, p in enumerate(listaAlunos):
    print(f'{i+1:<4}{p[0]:<10}{p[2]:>8.1f}')

while True:
    print()
    print('-'*60)
    print()
    opt = int(input('VERIFICAR NOTAS INDIVIDUAIS DE QUAL ALUNO? [999 -> ENCERRAR]: '))

    if opt == 999:
        print('ENCERRANDO...')
        time.sleep(1)
        break

    if opt <= len(listaAlunos)-1:
        print(f'ALUNO(A) ===> {listaAlunos[opt][0]} | NOTAS ===> {listaAlunos[opt][1]}')

print('{:^60}'.format(' <<< ATÉ ANO QUE VEM >>> '))
