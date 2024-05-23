"""

beecrowd | 1047
Tempo de Jogo com Minutos

Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo.
A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .


"""

hourStart, minuteStart, hourEnd, minuteEnd = list(map(int, input().split()))


# transformando tudo em minutos
minuteStart += hourStart*60
minuteEnd += hourEnd*60

# calculando o tempo total
hourTotal = minuteEnd - minuteStart

# calculando todo o processo com base em minutos

if hourTotal <= 0:
    hourTotal += 24*60

hourGame = hourTotal // 60
minuteGame = hourTotal % 60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hourGame, minuteGame))


