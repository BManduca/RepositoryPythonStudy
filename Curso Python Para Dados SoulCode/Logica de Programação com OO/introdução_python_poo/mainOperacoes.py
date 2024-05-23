import operacoes as op

soma = op.somar(2, 4)
subtracao = op.subtrair(4, 2)
divisao = op.dividir(8, 4)
multiplicacao = op.multiplicar(4, 2)

op.imprimirLinha(1)
op.imprimirMensagem(f'Soma: {soma}', 2)
op.imprimirMensagem(f'Subtração: {subtracao}', 2)
op.imprimirMensagem(f'Divisão: {divisao:.2f}', 2)
op.imprimirMensagem(f'Multiplicação: {multiplicacao}', 2)
op.imprimirLinha(1)

op.imprimirLinha(4)
op.imprimirMensagem('Final do programa', 4)
op.imprimirLinha(4)
