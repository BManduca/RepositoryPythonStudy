"""

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.

CODIGO      ESPECIFICAÇÃO         PREÇO
1           Cachorro Quente       R$ 4.00
2           X-Salada              R$ 4.50
3           X-Bacon               R$ 5.00
4           Torrada Simples       R$ 2.00
5           Refrigerante          R$ 1.50


Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e ]
à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago,
com 2 casas após o ponto decimal.



Exemplo de Entrada	    Exemplo de Saída
3 2                     Total: R$ 10.00
4 3                     Total: R$ 6.00
2 3                     Total: R$ 13.50


=> ao pegarmos o id e a quantidade, através de um input de uma linha so e ao dividir
aplicando o split, estaremos dividindo por espaços os elementos
e quando aplicamos um input, teremos uma lista e quando aplicar o split, teremos uma lista de strings

=> para pessesguirmos precisamos pegar essa lista de string e converter para o tipo que precisamos,
que neste caso são inteiros. Para isso, utilizaremos a função map(), passando o tipo que precisamos
e uma lista

"""

total = 0
idPedido, quantid = list(map(int, input().split()))

if idPedido == 1:
    total = quantid * 4.00
    print('Total: R$ %.2f' % total)
elif idPedido == 2:
    total = quantid * 4.50
    print('Total: R$ %.2f' % total)
elif idPedido == 3:
    total = quantid * 5.00
    print('Total: R$ %.2f' % total)
elif idPedido == 4:
    total = quantid * 2.00
    print('Total: R$ %.2f' % total)
elif idPedido == 5:
    total = quantid * 1.50
    print('Total: R$ %.2f' % total)
