'''
teste = []

teste.append('Brunno')
teste.append(31)

galera = []

galera.append(teste[:])

teste[0] = 'Gustavo'
teste[1] = 28

galera.append(teste[:])

print(galera)


galera = [['Brunno', 31], ['Gustavo', 33], ['Ângela', 13], ['Carla', 25]]

for p in galera:
    print(f'Nome: {p[0]} -> idade: {p[1]}')

'''


from os import system
import time

galera = []

dados = []

totMaior = totMenor = 0

for c in range(0, 3):
    dados.append(str(input('NOME: ')))
    dados.append(int(input('IDADE: ')))
    galera.append(dados[:])
    dados.clear()
    print()
    time.sleep(1)

print('-=-'*20)
for p in galera:
    if p[1] >= 18:
        print(f' => {p[0].upper()} É MAIOR DE IDADE!')
        totMaior += 1
    else:
        print(f' => {p[0].upper()} É MENOR DE IDADE')
        totMenor += 1
print('-=-'*20)
print()
print(f'TEMOS {totMaior} MAIOR(ES) E {totMenor} MENOR(ES) DE IDADE!')

