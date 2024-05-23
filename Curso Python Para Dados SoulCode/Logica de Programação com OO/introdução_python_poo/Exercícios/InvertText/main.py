from invertText import *

inputDados = str(input('INSIRA UM TEXTO: ')).upper()

result = invertText(inputDados)

print()
imprimirLinha(1)
imprimirMensagem(f'TEXTO ORIGINAL: {inputDados}', 2)
imprimirLinha(1)
imprimirMensagem(f'TEXTO INVERTIDO: {result}', 2)
imprimirLinha(1)
