"""
    EXERCÍCIO 101 - CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO()
    QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA, RETORNANDO
    UM VALOR LITERAL INDICANDO SE A PESSOA TEM SEU VOTO NEGADO, OPCIONAL OU
    OBRIGATÓRIO NAS ELEIÇÕES.
"""

from datetime import date


def mostraLinha():
    print()
    print('-='*30)


def voto(inputYear):
    anoAtual = date.today().year

    idade = anoAtual - inputYear

    if idade < 16:
        return f'\n   COM {idade} ANOS: VOTO NEGADO! '
    elif 16 <= idade < 18 or idade > 70:
        return f'\n   COM {idade} ANOS: VOTO OPCIONAL! '
    else:
        return f'\n   COM {idade} ANOS: VOTO OBRIGATÓRIO! '


# programa principal
mostraLinha()
anoNasc = int(input('\n   INSIRA O SEU ANO DE NASCIMENTO: '))
voteANS = voto(anoNasc)
print(voteANS)
mostraLinha()
print()
