"""
    FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA escreva(),
    QUE RECEBA UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE UMA MENSAGEM COM
    TAMANHO ADAPTÁVEL
"""


def mostraLinha(tamanho):
    print('~' * tamanho)


def escreva(mensagem):
    tam = len(mensagem) + 4
    mostraLinha(tam)
    print(f'  {mensagem}')
    mostraLinha(tam)


msg1 = str(input(' INSIRA A PRIMEIRA MENSAGEM: '))
msg2 = str(input(' INSIRA A SEGUNDA MENSAGEM: '))
msg3 = str(input(' INSIRA A TERCEIRA MENSAGEM: '))


escreva(msg1)
escreva(msg2)
escreva(msg3)


