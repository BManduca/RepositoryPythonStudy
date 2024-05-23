import math

num = int(input('Digite um número: '))
expoente = int(input('Insira o valor do expoente: '))

raizQuadrada = math.sqrt(num)
pot = math.pow(num, expoente)

print('\n')
print('-'*100)
print('\nA raiz quadrada de {} é {:.2f}'.format(num, raizQuadrada))
print('\nA raiz quadrada de {} arredondando para cima é {:.2f}'.format(num, math.ceil(raizQuadrada)))
print('\nA raiz quadrada de {} arredondando para baixo é {:.2f}'.format(num, math.floor(raizQuadrada)))
print('\nO número {} elevado a {}º potência é {:.2f}\n'.format(num, expoente, pot))
print('-'*100)
