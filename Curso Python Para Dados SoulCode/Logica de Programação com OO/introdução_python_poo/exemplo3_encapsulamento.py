def imprimirMensagem(msg):
    print(f'{msg:^60}')


def imprimirLinha():
    print('-=-' * 20)


i = 0
jobHours = 8


class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        # aqui estamos criando atríbutos do tipo private
        # porém por questões de segurança, esse modo de criar não é suficiente
        # para deixar inacessível o atríbuto ou até mesmo alterar o mesmo
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossível alterar o salário diretamente. Use a função calcula_salario().")

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
        return self.__salario

    def get_info_func(self):
        imprimirLinha()
        imprimirMensagem(f'Funcionário: {self.nome}')
        imprimirMensagem(f'Cargo: {self.cargo}')
        imprimirMensagem(f'Valor da hora trabalhada: {self.valor_hora_trabalhada}')
        imprimirLinha()


funcionario1 = Funcionario('José', 'Professor', 175)
# se caso usassemos funcionario1.salario = 10000, daria um erro, pois tentamos acessar e modificar um atríbuto
# fora da classe
funcionario1.get_info_func()

while i < jobHours:
    funcionario1.registra_hora_trabalhada()
    i += 1

novoSalario = funcionario1.calcula_salario()
print()
imprimirLinha()
imprimirMensagem(f'O salario do {funcionario1.nome} é: {novoSalario}')
imprimirLinha()
