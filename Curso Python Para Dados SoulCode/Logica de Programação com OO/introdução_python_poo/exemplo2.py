def imprimirMensagem(msg):
    print(f'{msg:^60}')


def imprimirLinha():
    print('-=-' * 20)


class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def get_info_func(self):
        imprimirLinha()
        imprimirMensagem(f'Nome: {self.nome}')
        imprimirMensagem(f'CPF: {self.cpf}')
        imprimirMensagem(f'Salario: {self.salario}')
        imprimirLinha()

    def get_bonificacao(self):
        return self.salario * 0.20


func1 = Funcionario('Brunno', '08354047903', 5250)
func1.get_info_func()
bonus = func1.get_bonificacao()
print()
imprimirLinha()
imprimirMensagem(f'A bonificação do funcionário é: {bonus}')
imprimirLinha()
