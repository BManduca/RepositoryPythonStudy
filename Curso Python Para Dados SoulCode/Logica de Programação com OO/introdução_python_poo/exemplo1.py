def imprimirMensagem(msg):
    print(f'{msg:^60}')


def imprimirLinha():
    print('-=-'*20)


class Veiculo:
    # a function logo abaixo é o constructor da nossa classe
    # Atributos e métodos da classe
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrarInfo(self):
        imprimirLinha()
        imprimirMensagem(f'Tipo: {self.tipo}')
        imprimirMensagem(f'Chassi: {self.chassi}')
        imprimirMensagem(f'Marca: {self.marca}')
        imprimirMensagem(f'Modelo: {self.modelo}')
        imprimirMensagem(f'Ano: {self.ano}')
        imprimirLinha()


class Aviao:
    # Atributos e métodos da classe
    def __init__(self, tipo, motor, linha_aerea, modelo, ano):
        self.tipo = tipo
        self.motor = motor
        self.linha_aerea = linha_aerea
        self.modelo = modelo
        self.ano = ano

    def mostraInfo(self):
        imprimirLinha()
        imprimirMensagem(f'Tipo: {self.tipo}')
        imprimirMensagem(f'Motor: {self.motor}')
        imprimirMensagem(f'Linha aerea: {self.linha_aerea}')
        imprimirMensagem(f'Modelo: {self.modelo}')
        imprimirMensagem(f'Ano: {self.ano}')
        imprimirLinha()


# para criar um objeto novo, estaremos instanciando uma classe

carro1 = Veiculo('Coupe', 'A15SDAD4FDAS5DF78ASD45FAS5DF', 'Aston Martin', 'Vantage', '2005')
aviao1 = Aviao('Carga', 'Quadrimotor', 'Manduca Airlines', 'Airbus a380', '2010')
carro1.mostrarInfo()
aviao1.mostraInfo()
