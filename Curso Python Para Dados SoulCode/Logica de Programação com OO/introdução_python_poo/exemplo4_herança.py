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


class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostra_info_veiculo(self):
        imprimirLinha(1)
        imprimirMensagem(f'Tipo: {self.tipo}', 2)
        imprimirMensagem(f'Chassi: {self.chassi}', 2)
        imprimirMensagem(f'Marca: {self.marca}', 2)
        imprimirMensagem(f'Modelo: {self.modelo}', 2)
        imprimirMensagem(f'Ano: {self.ano}', 2)
        imprimirLinha(1)


class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        # utilizando uma super classe | constructor
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindrada = cilindrada

    def mostra_info_motocicleta(self):
        imprimirLinha(1)
        imprimirMensagem(f'Tipo: {self.tipo}', 2)
        imprimirMensagem(f'Chassi: {self.chassi}', 2)
        imprimirMensagem(f'Marca: {self.marca}', 2)
        imprimirMensagem(f'Modelo: {self.modelo}', 2)
        imprimirMensagem(f'Ano: {self.ano}', 2)
        imprimirMensagem(f'Cilindrada: {self.cilindrada}', 2)
        imprimirLinha(1)


veiculo1 = Veiculo('Carro', '456AS4DAS64F1AS3DF16ASD4', 'Ferrari', 'Spider', 2017)
veiculo1.mostra_info_veiculo()
print()
motocicleta1 = Motocicleta('Esportiva', 'FASDF4AS68D4C6AS4F6AS', 'Ducati', 'XDiavels', 2021, 1262)
motocicleta1.mostra_info_motocicleta()
