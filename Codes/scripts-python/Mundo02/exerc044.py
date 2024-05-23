"""

Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros

"""

from os import system
import time

print('\n')
print('-'*70)
print('\nPROGRAMA PARA SIMULAR O CÁLCULO DE PRODUTOS SELECIONADOS\n')
print('-'*70)
print('\n')

print('\nGOSTARIA DE INICIAR A SIMULAÇÃO?\n')
print('-'*17)
print('| S - Para sim |\n| N - Para não |')
print('-'*17)

question = str(input('\nResposta: '))
print('\n')

while question != 'N':

    print('-'*70)
    print('\n')
    print('{:=^40}'.format(' LOJAS MANDUCA '))

    nameProduto = str(input('\nInsira o nome do produto: '))
    preço = float(input('\nDigite o valor do produto: R$ '))
    print('''Escolha uma forma de pagamento:
        [ 1 ] à vista dinheiro/cheque
        [ 2 ] à vista no cartão
        [ 3 ] em até 2x no cartão
        [ 4 ] 3x ou mais no cartão
    ''')


    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        valor = preço - (preço * 10 / 100)
        print('\nAo pagar o produto {} à vista no dinheiro/chegue, o valor ficará {:.2f}\n'.format(nameProduto, valor))
    elif opcao == 2:
        valor = preço - (preço * 5 / 100)
        print('\nAo pagar o produto {} à vista no cartão, o valor ficará {:.2f}\n'.format(nameProduto, valor))
    elif opcao == 3:
        valor = preço
        parcela = valor / 2
        print('\nAo pagar o produto {} em até 2x no cartão,\no valor de cada parcela será de R$ {:.2f} sem juros\n\nAo final a compra resultará em um total de R$ {:.2f}\n'.format(nameProduto, parcela, valor))
    elif opcao == 4:
        valor = preço + (preço * 20 / 100)
        totalParcelas = int(input('Quantas parcelas? '))
        parcela = valor / totalParcelas
        print('\nAo pagar o produto {} em {}x no cartão,\no valor de cada parcela será de R$ {:.2f} com juros\n\nAo final a compra resultará em um total de R$ {:.2f}\n'.format(nameProduto, totalParcelas, parcela,valor))
    else:
        total = 0
        print('\n{}OPÇÃO INVÁLIDA DE PAGAMENTO!{}\n'.format('\033[1;31m','\033[0;30m'))
    print('-'*70)

    print('\n\nGOSTARIA DE REALIZAR UM NOVO CÁLCULO DO VALOR DO PRODUTO?\n')
    print('-'*17)
    print('| S - Para sim |\n| N - Para não |')
    print('-'*17)
    question = str(input('\nResposta: '))
    system('clear')

print('\nOBRIGADO POR UTILIZAR MEU SOFTWARE!\n')

print('A TELA SERÁ LIMPA EM 5 SEGUNDOS!\n')
time.sleep(5)

system('clear')