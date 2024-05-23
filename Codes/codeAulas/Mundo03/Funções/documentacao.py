from time import sleep


def mostraLinha():
    print('-='*25)
    print()


def contador(ini, fim, passo):
    """
    => FAZ UMA CONTAGEM E MOSTRA O RESULTADO EM TELA!!

    :param ini: parâmetro para ínicio da contagem
    :param fim: parâmetro para o fim da contagem
    :param passo: a quantidade que vai 'pular' de um valor para outro
    :return: sem retorno
    """

    cont = ini
    while cont <= fim:
        print(f'{cont} ', end='', flush=True)
        sleep(0.4)
        cont += passo
    print(' FIM!! ')


def somar(a=0, b=0, c=0):
    """

    REALIZA A SOMA ENTRE 3 VALORES PARASSADOS COMO PARÂMETROS

    :param a: PRIMEIRO VALOR DA SOMA
    :param b: SEGUNDO VALOR DA SOMA
    :param c: TERCEIRO VALOR DA SOMA
    :return: SEM RETORNO
    """
    soma = a + b + c
    return soma
    # mostraLinha()
    # if c != 0:
    #     print(f'      A SOMA FINAL DE {a} + {b} + {c} ==> {soma}')
    # elif b != 0:
    #     print(f'      A SOMA FINAL DE {a} + {b} ==> {soma}')
    # elif a != 0:
    #     print(f'      A SOMA FINAL DE {a} ==> {soma}')
    # else:
    #     print('      NÃO EXISTE VALORES PARA REALIZAR A SOMA! ')
    # print()
    # mostraLinha()


r1 = somar(2, 3, 5)
r2 = somar(5, 9)
r3 = somar(9)
r4 = somar()
# help(somar)
# help(contador)

mostraLinha()
print(f'    OS RESULTADOS DAS SOMAS SÃO {r1}, {r2}, {r3} E {r4}')
print()
mostraLinha()



"""
    analisando escopo de varíavel
    
    def teste(b):
    
        global a -> desta forma utilizamos a varíavel a global, em vez de criar uma localmente => palavra 
        reservada 'global'
        
        a = 8 -> se fizer assim, sem chamar uma varíavel global, como foi feito acima, 
        estaremos criando uma varíavel 'a' localmente, diferente da existente no escopo global
        
        b+=4
        c=2
        print(f'A DENTRO VALE ==> {a}')
        print(f'B DENTRO VALE ==> {b}')
        print(f'C DENTRO VALE ==> {c}')
        
    a = 5
    teste(a)
    print(f'A FORA VALE ==> {a}')
    print(f'B FORA VALE ==> {b}') -> daria erro
    print(f'C FORA VALE ==> {c}') -> daria erro
    
    as duas linhas dariam erro pois c e b são varíaveis locais e não globais que nem o a


"""