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


class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        self.__enderecos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def inserir_endereco(self, cidade):
        self.__enderecos.append(Endereco(cidade))

    def lista_enderecos(self):
        for endereco in self.__enderecos:
            imprimirMensagem('Cidade: ' + endereco.cidade, 4)


class Endereco:
    def __init__(self, cidade):
        self.__cidade = cidade

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade


imprimirLinha(1)
cliente1 = Cliente('Brunno')
cliente1.inserir_endereco('Florianópolis')
imprimirMensagem('Nome: ' + cliente1.nome, 2)
cliente1.lista_enderecos()
imprimirLinha(1)
del cliente1
