"""
    FAÇA UM PROGRAMA QUE LEIA O NOME E MÉDIA
    DE UM ALUNO, GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO.
    NO FINAL MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA
"""

print()
print('-'*60)
print('{:^60}'.format(' RELATÓRIO MÉDIA DE ALUNO '))
print('-'*60)

relatorio = {}
print()
relatorio['nome'] = str(input('NOME DO ALUNO: '))
relatorio['media'] = float(input(f'INSIRA A MÉDIA DO ALUNO {relatorio["nome"].upper()}: '))

if relatorio['media'] >= 7:
    relatorio['situacao'] = 'APROVADO'
elif relatorio['media'] >= 5 and relatorio['media'] <= 6.9:
    relatorio['situacao'] = 'RECUPERAÇÃO'
else:
    relatorio['situacao'] = 'REPROVADO'

# print(relatorio)

print()
print('-='*15)
print(f'NOME ==> {relatorio["nome"]}\nMÉDIA ==> {relatorio["media"]}\nSITUAÇÃO ==> {relatorio["situacao"]}')
print('-='*15)
