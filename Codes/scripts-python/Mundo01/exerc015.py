"""
    Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
    e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
    R$60 por dia e R$0,15 por km rodado.
"""

print('===== EXERCÍCIO 15 ======\n')

totalDiasAlugados = int(input('Por quantos dias o carro foi alugado? '))
totalkmRodados = float(input('Quantos KM foram rodados com o carro? '))

print('\nO total a pagar pela locação do veículo é de R${:.2f}'.format(totalDiasAlugados * 60 + totalkmRodados * 0.15))