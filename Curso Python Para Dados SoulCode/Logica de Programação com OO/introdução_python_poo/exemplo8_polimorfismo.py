from abc import ABC, abstractmethod

colors = ('\033[0m',  # 0 - SEM CORES
          '\033[0;31m',  # 1 - VERMELHO
          '\033[0;32m',  # 2 - VERDE
          '\033[0;33m',  # 3 - AMARELO
          '\033[0;34m',  # 4 - AZUL
          '\033[0;35m',  # 5 - ROXO
          '\033[0;30m'  # 6 - BRANCO
          )


def imprimirMensagem(msg, cor=0):
    print(colors[cor], end='')
    print(f'{msg:^60}')
    print(colors[0], end='')


def imprimirLinha(cor=0):
    print(colors[cor], end='')
    print('-=-' * 20)
    print(colors[0], end='')


class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):
        imprimirMensagem(f'B está falando {msg}', 2)


class C(A):
    def fala(self, msg):
        imprimirMensagem(f'C está falando {msg}', 4)


# o objeto 'a' não pode ser criado, pois é uma classe abstrata e está não pode ser instanciada
b = B()
c = C()


"""
    as classes b e c, utilizam o método fala, porém, se comportam de maneira diferente, 
    acaba sobrepondo o que é realizado na classe pai, agindo diferente nas classes filhas.
    
"""
imprimirLinha(1)
b.fala('de Basquete')
c.fala('de Futebol')
imprimirLinha(1)
