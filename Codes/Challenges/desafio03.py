"""
    Crie um script Python que leia dois números e tente mostrar a soma dos dois

    Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também 
    sua ordem de precedência dentro de expressões matemáticas. 
    Veja como funcionam os operadores de adição, subtração, multiplicação, 
    divisão, exponenciação e quociente na linguagem Python.

    adição -> +
    subtração -> -
    Multiplicação -> *
    divisão inteira //
    Potência -> **
    Resto da divisão -> /


"""

print('===== DESAFIO 03 ======\n')
valor1 = int(input('Insira o primeiro valor: '))
valor2 = int(input('Insira o segundo valor: '))

soma = valor1 + valor2
sub = valor1 - valor2
mult = valor1 * valor2
div = valor1 / valor2
poten = valor1 ** valor2

print('\nResultado:\n')
print('\nSoma:',soma,'\nSub:',sub ,'\nMult: ',mult,'\nDiv:',div,'\nPoten:',poten)