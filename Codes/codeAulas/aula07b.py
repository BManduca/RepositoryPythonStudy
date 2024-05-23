print('===== EXERCÍCIO AULA 07b ======\n')

valor1 = int(input('Insira o primeiro valor: '))
valor2 = int(input('Insira o segundo valor: '))

soma = valor1 + valor2
sub = valor1 - valor2
mult = valor1 * valor2
div = valor1 / valor2
divInt = valor1 // valor2
exp = valor1 ** valor2

print('\nA soma é {}\nA subtração é {}\nA multiplicação é {}'.format(soma, sub, mult))
print('\nA divisão é {:.3f}\nA divisão inteira é {}\nA exponenciação é {}'.format(div, divInt, exp))

