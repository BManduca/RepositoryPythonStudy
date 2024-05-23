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

def imprimir_linha(cor=0):
    print(colors[cor], end='')
    print('-=-'*25)
    print(colors[0], end='')

df = pd.DataFrame({
    'Aluno': ["José", "Carlos", "Ana", "Júlia", "Débora"],
    'Faltas': [3, 4, 2, 4, 3],
    'Prova': [2, 7, 8, 5.5, 9.2],
    'Seminário': [8.5, 5, 8.2, 6, 9.5]
})


imprimir_linha(3)
print_text_centralized('Visualizando dados especifícos', 72, 3)
imprimir_linha(3)
print(df.loc[3])
imprimir_linha(3)
