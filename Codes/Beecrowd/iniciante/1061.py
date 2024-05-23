"""

beecrowd | 1061
Tempo de um Evento
Timelimit: 1

Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril,
iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar,
uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a
calcular a duração deste evento.

Entrada

Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai
começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss.
Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas,
indicando o término do evento.

Saída

Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

Mês de abril vai de 1 a 30
"""

# execução geral

diaI = int(input().split()[1])
hI, mI, sI = map(int, input().split(":"))
# transformando todos os valores de input para segundos
totalI = sI + (mI * 60) + (hI * 3600) + (diaI * 86400)

diaF = int(input().split()[1])
hF, mF, sF = map(int, input().split(":"))
# transformando todos os valores de input para segundos
totalF = sF + (mF * 60) + (hF * 3600) + (diaF * 86400)

res = totalF - totalI
# calculando os dias
d = res // 86400
# armazenando o resto da divisão
res = res % 86400

# calculando as horas
h = res // 3600
# armazenando o resto da divisão
res = res % 3600

# calculando os minutos
m = res // 60
# armazenando o resto da divisão
res = res % 60

# calculando os segundos
s = res

print('%i dia(s)' % d)
print('%i hora(s)' % h)
print('%i minuto(s)' % m)
print('%i segundo(s)' % s)

"""
teste
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23
"""

# print(f"Dia {diaI}\nhora(s) {hI}\nminuto(s) {mI}\nsegundo(s) {sI}")
# print()
# print(f"Dia {diaF}\nhora(s) {hF}\nminuto(s) {mF}\nsegundo(s) {sF}")
