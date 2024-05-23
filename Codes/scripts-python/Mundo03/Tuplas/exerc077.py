"""
    CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS 
    (NÃO USAR ACENTOS). DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA 
    CADA PALAVRA, QUAIS SÃO SUAS VOGAIS.
"""

print('\n')
print('='*72)
print('{:=^72}'.format(' EXERCÍCIO 77 '))
print('='*72)
print('\n')

words = ('computador', 'bombeiro', 
         'aviao', 'policia', 
         'viagem', 'helicoptero', 
         'painel', 'quadrado', 
         'apartamento', 'bone',
         'aprender', 'programar',
         'python', 'curso',
         'video', 'estudar')

# print(words)

print('='*72)
print('{:=^72}'.format(' LISTAGEM PALAVRAS E SUAS RESPECTIVAS VOGAIS '))
print('='*72)

print('\n')
print('='*72)
for elem in words:
    print(f'\nNa palavra {elem.upper()} temos as vogais: ', end='')
    # print(f'\nPALAVRA: {elem.upper():-<20}>', end='')
    # print(' VOGAIS: ', end='')
    for letter in elem:
        if letter in 'aeiou':
            print(f' {letter.lower()} ', end=' ')
    # print(' |')
print('\n')
print('='*72)
