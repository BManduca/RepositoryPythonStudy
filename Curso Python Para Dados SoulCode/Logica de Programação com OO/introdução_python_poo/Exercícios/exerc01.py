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


class Animal:
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def mostra_info_animal(self):
        imprimirLinha(1)
        imprimirMensagem(f'Nome: {self.nome}', 2)
        imprimirMensagem(f'Cor: {self.cor}', 2)
        imprimirMensagem(f'Idade: {self.idade}', 2)
        imprimirLinha(1)


class Cachorro(Animal):
    def __init__(self, nome, cor, idade, tipo, porte, raça):
        super().__init__(nome, cor, idade)
        self.tipo = tipo
        self.porte = porte
        self.raça = raça

    def mostra_info_cachorro(self):
        imprimirLinha(1)
        imprimirMensagem(f'Nome: {self.nome}', 2)
        imprimirMensagem(f'Cor: {self.cor}', 2)
        imprimirMensagem(f'Idade(meses): {self.idade}', 2)
        imprimirMensagem(f'Tipo: {self.tipo}', 2)
        imprimirMensagem(f'Porte: {self.porte}', 2)
        imprimirMensagem(f'Raça: {self.raça}', 2)
        imprimirLinha(1)


class Gato(Animal):
    def __init__(self, nome, cor, idade, tipo, porte, raça):
        super().__init__(nome, cor, idade)
        self.tipo = tipo
        self.porte = porte
        self.raça = raça

    def mostra_info_gato(self):
        imprimirLinha(1)
        imprimirMensagem(f'Nome: {self.nome}', 2)
        imprimirMensagem(f'Cor: {self.cor}', 2)
        imprimirMensagem(f'Idade(meses): {self.idade}', 2)
        imprimirMensagem(f'Tipo: {self.tipo}', 2)
        imprimirMensagem(f'Porte: {self.porte}', 2)
        imprimirMensagem(f'Raça: {self.raça}', 2)
        imprimirLinha(1)


animal1 = Animal('Kyle', 'Acinzentado', 29)
animal1.mostra_info_animal()
print()
cachorro1 = Cachorro('Kyle', 'Acinzentado', 29, 'Cachorro', 'Médio', 'Pastor alemão')
cachorro1.mostra_info_cachorro()
print()
gato1 = Gato('Agatha', 'Mesclado', '96', 'Gato', 'Médio', 'SRD')
gato1.mostra_info_gato()

