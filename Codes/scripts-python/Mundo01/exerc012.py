"""
    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
    com 5% de desconto.
"""

print('===== EXERCÍCIO 12 ======\n')

precoProduto = float(input('Qual o preço do produto? R$ '))

valorDesc = (precoProduto * 5)/100

valorFinal = precoProduto - valorDesc

print('\nO produto custava {:.2f}, mas na promoção com desconto de 5%, \no valor passa a ser R$ {:.2f}'.format(precoProduto, valorFinal))