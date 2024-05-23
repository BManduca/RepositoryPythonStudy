"""
    FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES.
    O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS E VAI SORTEAR 6 NÚMEROS
    ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA.
"""

print()
print('-'*60)
print('{:^60}'.format(' GERADOR DE JOGOS DA MEGA SENA'))
print('-'*60)

from random import randint
import time

totalJogos= 1
listaAux = []
listaMega = []

quantJogos = int(input('\nINSIRA A QUANTIDADE DE JOGOS QUE SERÁ SORTEADO: '))

while totalJogos <= quantJogos:

    contador = 0

    while True:
        numAleat = randint(1, 60)
        if numAleat not in listaAux:
            listaAux.append(numAleat)
            contador += 1

        if contador >= 6:
            break

    # colocando a lista em ordem
    listaAux.sort()
    # fazendo uma copia de listaAux para a listaMega
    listaMega.append(listaAux[:])
    # 'limpando' o conteúdo da listaAux
    listaAux.clear()
    totalJogos += 1
print()
print('-='*6, f' SORTEANDO {quantJogos} JOGOS ', '-='*6)

for i, l in enumerate(listaMega):
    print(f' JOGO {i+1}: {l}')
    time.sleep(1)
print('-='*7, ' < BOA SORTE! > ', '-='*7)


