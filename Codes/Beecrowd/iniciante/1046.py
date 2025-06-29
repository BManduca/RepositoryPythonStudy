"""

beecrowd | 1046
Tempo de Jogo

Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo,
sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração
mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de
início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.

"""


N1, N2 = list(map(int, input().split()))

if N1 < N2:
    horaJogo = N2 - N1
else:
    horaJogo = (N2 + 24) - N1
print(f'O JOGO DUROU %d HORA(S)' % horaJogo)
