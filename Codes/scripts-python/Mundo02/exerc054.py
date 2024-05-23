"""
CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL MOSTRE QUANTAS PESSOAS
AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ ATINGIRAM 
"""

print('\n')
print('-'*84)
print('\n------------------------ PROGRAMA PARA VERIFICAR MAIORIDADE ------------------------\n')
print('-'*84)
print('\n')


from datetime import date
vetMaior = []
vetMaiorIdade = []
totMaior = 0
vetMenor = []
vetMenorIdade = []
totMenor = 0

anoAtual = date.today().year

for iPessoa in range(1,8):
    anoNasc = int(input('EM QUE ANO A {}º PESSOA NASCEU? '.format(iPessoa)))

    idade = anoAtual - anoNasc

    if idade >= 18:
        vetMaior.append(anoNasc)
        vetMaiorIdade.append(idade)
        totMaior += 1
    else:
        vetMenor.append(anoNasc)
        vetMenorIdade.append(idade)
        totMenor += 1

print('\n')
print('-'*50)
print('Ao todo tivemos {} pessoas maiores de idade\nQue nasceram nos anos: {}\nCom as seguintes idades: {}'.format(totMaior,vetMaior, vetMaiorIdade))
print('\n\nAo todo tivemos {} pessoas menores de idade \nQue nasceram nos anos: {}\nCom as seguintes idades: {}'.format(totMenor,vetMenor, vetMenorIdade))
print('-'*50)