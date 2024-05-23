import numpy as np
import pandas as pd

colors = (
    '\033[0m', # 0 - SEM COR
    '\033[0;31m', # 1 - VERMELHO
    '\033[0;32m', # 2 - VERDE
    '\033[0;33m', # 3 - AMARELO
    '\033[0;34m', # 4 - AZUL
    '\033[0;35m', # 5 - ROXO
    '\033[0;36m', # 6 - BRANCO
)

def message_centralized(msg, wid):
    tam = len(msg)
    space = (wid - tam) // 2
    text = ' ' * space + msg + ' ' * space
    # Se o texto não puder ser centralizado perfeitamente, ajuste uma posição para a direita
    if len(text) < wid:
        text += ' '
    return text

def print_text_centralized(msg, wid, cor=0):
    message = message_centralized(msg, wid)
    print(colors[cor], end='')
    print(message)
    print(colors[0], end='')

def imprimir_linha_20(cor=0):
    print(colors[cor], end='')
    print('-=-'*20)
    print(colors[0], end='')

notas = pd.Series([10, 5, 7.5, 9, 10])

notas2 = pd.Series([10, 5, 7.5, 9, 10], index=['José', 'Carlos', 'André', 'João', 'Débora'])
# print(notas2)

# método describe exibe informações estatísticas(count, mean, std, min...)
imprimir_linha_20(2)
# print(notas.describe())
print_text_centralized(f'Média: {notas.mean()}', 60, 2)
imprimir_linha_20(2)
print()
imprimir_linha_20(2)
print_text_centralized('IMPRIMINDO O DOBRO DAS NOTAS: ', 60, 2)
imprimir_linha_20(2)
# aqui estará impirmindo toda a cadeia de informações das notas com seus devidos indexes
print(f'{notas**2}')
# para imprimir somente os valores das notas ou os index
# print(f'{notas.values}')
# print(f'{notas.index}')
imprimir_linha_20(2)
print()
imprimir_linha_20(3)
print_text_centralized('ALUNOS VS. NOTAS', 60, 3)
imprimir_linha_20(3)
print(notas2)
imprimir_linha_20(3)
