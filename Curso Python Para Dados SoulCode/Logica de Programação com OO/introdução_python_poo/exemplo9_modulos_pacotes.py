import math


# import math
# import numpy
print(dir())


def imprimirMensagem(msg):
    print(f'{msg:^30}')


for i in range(10):
    imprimirMensagem(f'Fatorial {i+1}: {math.factorial(i+1):>20}')

