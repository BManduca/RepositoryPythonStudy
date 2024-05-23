"""
CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE A PALAVRA É PALÍNDROME, DESCONSIDERANDO OS ESPAÇOS!
"""

print('\n')
print('-'*109)
print('\n---------------------- PROGRAMA PARA VERIFICAR SE O TEXTO INSERIDO É PALÍNDROME OU NÃO ----------------------\n')
print('-'*109)
print('\n')


# exemplos:
#  - APÓS A SOPA
#  - A SACADA DA CASA
#  - A TORRE DA DERROTA
#  - O LOBO AMA O BOLO
#  - ANOTARAM A DATA DA MARATONA

# frase = str(input('Insira uma frase: ')).upper().replace(' ', '')

# 'jogando' toda a frase pra maiusculo e eliminando os espaços antes e depois da frase
frase = str(input('Insira uma frase: ')).strip().upper()
print('')
# gerando uma lista da frase 'splitada'
palavras = frase.split()
print('')
# eliminando os espaços presente na frase
tudojunto = ''.join(palavras)

inverso = ''


"""
   - len(tudojunto) - 1 => ir da última letra até a primeira
   - aqui sabemos que a primeira letra é zero, por isso temos
   que usar o -1, pois, é sempre um a menos  
   - e o outro parâmetro -1, pois vai ser feito uma varredura 
   ao contrário 
"""

#gerando o inverso da frase
for letra in range(len(tudojunto) - 1, -1, -1):
    inverso += tudojunto[letra]

print('O inverso de {} é {}'.format(tudojunto, inverso), '\n')

if inverso == tudojunto:
    print('O TEXTO INSERIDO É PALÍNDROME!','\n')
else:
    print('A TEXTO NÃO É PALÍNDROME!','\n')

# utilizando o fatiamento
# if tudojunto == tudojunto[:: - 1]:
#     print('O TEXTO INSERIDO É PALÍNDROME!','\n')
#     # print('O TEXTO INVERTIDO: {}'.format(tudojunto), '\n')
# else:
#     print('A TEXTO NÃO É PALÍNDROME!','\n')

