import random as rd

colors = ('\033[0m',  # 0 - SEM CORES
          '\033[0;31m',  # 1 - VERMELHO
          '\033[0;32m',  # 2 - VERDE
          '\033[0;33m',  # 3 - AMARELO
          '\033[0;34m',  # 4 - AZUL
          '\033[0;35m',  # 5 - ROXO
          '\033[0;30m'  # 6 - BRANCO
)


def imprimirMensagem(msg, cor=0):
    print(colors[cor], end='')
    print(f'{msg:^60}')
    print(colors[0], end='')

def mensagem(msg, cor=0):
    print(colors[cor], end='')
    print(f'{msg}')
    print(colors[0], end='')


def imprimirLinha(cor=0):
    print(colors[cor], end='')
    print('-=-'*20)
    print(colors[0], end='')

def pularLinha():
    print()


def jogo_da_forca():
    imprimirLinha(3)
    imprimirMensagem('JOGO DA FORCA', 3)
    imprimirMensagem('SEJA BEM VINDO!')
    imprimirLinha(3)


    
    listaJogo = [
        'AMARELO',
        'SMARTPHONE',
        'BASQUETE',
        'CHAMPAGNE',
        'CAMPEONATO',
        'CATAPORA',
        'PAÇOCA',
        'PEDREIRO',
        'TRILOGIA',
        'MAE',
        'MOEDA',
        'CASA',
        'GATO', 
        'AMIGO',
        'CHUVA',
        'NUVEM',
        'ACENDER',
        'COELHO',
        'CHUVEIRO'
    ]


    #Função para escolher uma palavra da lista aleatoriamente
    def escolhendoPalavra(listaJogo):    
        tamanhoLista = len(listaJogo)
        sorteandoPalavra = rd.randint(0,tamanhoLista-1)    
        escolhendoPalavra = listaJogo[sorteandoPalavra] 
        return escolhendoPalavra
    
    #função para localizar as posições de uma letra em uma palavra
    def localizar(texto,palavra):
        posicoes = []
        for i in range(0,len(texto)):
            if texto[i] == palavra:
                posicoes.append(i)
        return posicoes


    palavra_escolhida = escolhendoPalavra(listaJogo)
    pularLinha()
    print(f'DICA: A palavra tem {len(palavra_escolhida)} letras')


    oportunidades = 0
    pal_mascarada = list('_' * len(palavra_escolhida))
    while oportunidades <= 10:
        pularLinha()
        mensagem('Digite somente uma letra: ', 2)
        letra_escolhida = input('').upper()    
        if letra_escolhida in palavra_escolhida:
                imprimirMensagem(f'A letra {letra_escolhida} está contida na frase', 3)
                posicao = localizar(palavra_escolhida,letra_escolhida)
                for i in posicao:    
                    pal_mascarada[i] = letra_escolhida            
                imprimirMensagem(f'{pal_mascarada}')
                pularLinha()
                pularLinha()
                mensagem('Você já sabe qual é a palavra? (S ou N): ', 4)
                opcao = input('')        
                if opcao.upper() == 'S':
                    resposta = input('Digite o nome da palavra: ')
                    if resposta.upper() == palavra_escolhida:
                        imprimirLinha(3)
                        imprimirMensagem(f'Parabéns!!', 2)
                        imprimirMensagem(f'A Palavra correta é {palavra_escolhida}!', 2)
                        imprimirLinha(3)
                        pularLinha()
                        break
                    else:
                        imprimirMensagem('Você errou!', 1)
                        print(f'A Palavra correta é {palavra_escolhida}!', 1)
                        imprimirMensagem('GAME OVER', 1)
                        pularLinha()
                        break
                else:
                    pularLinha()
                    imprimirLinha(4)
                    imprimirMensagem(f'Você ainda tem {9-int(oportunidades)} oportunidades', 4)
                    imprimirLinha(4)
        else:
            pularLinha()
            imprimirMensagem(f'A letra {letra_escolhida} NÃO está contida na frase', 3)
            pularLinha()
            imprimirMensagem(f'{pal_mascarada}')
            pularLinha()
            pularLinha()
            mensagem('Você já sabe qual é a palavra? (S ou N): ', 4)
            opcao = input('')
            if opcao.upper() == 'S':
                resposta = input('Digite o nome da palavra: ')
                if resposta.upper() == palavra_escolhida:
                    imprimirLinha(3)
                    imprimirMensagem(f'Parabéns!!', 2)
                    imprimirMensagem(f'A Palavra correta é {palavra_escolhida}!', 2)
                    imprimirLinha(3)
                    pularLinha()
                    break
                else:
                    imprimirMensagem('Você errou!', 1)
                    print(f'A Palavra correta é {palavra_escolhida}!', 1)
                    imprimirMensagem('GAME OVER', 1)
                    pularLinha()
                    break 
            else:
                pularLinha()
                imprimirLinha(4)
                imprimirMensagem(f'Você ainda tem {9-int(oportunidades)} oportunidades', 4)
                imprimirLinha(4)
                
        oportunidades +=1
        if oportunidades >= 10:
            imprimirMensagem('GAME OVER', 1)
            imprimirMensagem(f'A Palavra correta é {palavra_escolhida}!', 1)
            pularLinha()
            break


jogo_da_forca()