"""
    FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO contador(), QUE RECEBA
    TRÊS PARÂMETROS: início, fim e passo E REALIZE A CONTAGEM

    SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
    A) DE 1 ATÉ 10, DE 1 EM 1
    B) DE 10 ATÉ 0, DE 2 EM 2
    C) UMA CONTAGEM PERSONALIZADA
"""

from time import sleep


def mostraLinha():
    print('~' * 46)
    print()


def mostraLinha2():
    print('-'*45)
    print()


def contador(ini, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'CONTAGEM DE {ini} ATÉ {fim}, COM INTERVALO = {passo}\n')
    sleep(1.5)
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f' {cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print(' FIM!! \n')
    else:
        cont = ini
        while cont >= fim:
            print(f' {cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print(' FIM!! \n')


mostraLinha()
print(' A) ', end='')
contador(1, 10, 1)
mostraLinha()
print(' B) ', end='')
contador(10, 0, 2)
mostraLinha()
mostraLinha2()
print(' AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!')
print()
mostraLinha2()
mostraLinha()
i = int(input('INSIRA O VALOR INICIAL DA CONTAGEM: '))
f = int(input('INSIRA O VALOR FINAL DA CONTAGEM:   '))
p = int(input('INSIRA O INTERVALO DA CONTAGEM:    '))
print()
mostraLinha()
print(' C) ', end='')
contador(i, f, p)
mostraLinha()

