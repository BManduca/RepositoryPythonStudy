"""
    FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES 'M' OU 
    'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO MOVAMENTE ATÉ TER UM VALOR CORRETO.
"""


# pegando o sexo do usuario e retirando os espaços antes e depois da palavra, colocando a mesma em maíuscula, fatiando e pegando somente a primeira letra
sexo = str(input('INFORME O SEU SEXO [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('\nDados inválidos!\nPor favor, informe o sexo novamente: ')).strip().upper()[0]
print('O SEXO {} FOI REGISTRADO COM SUCESSO!'.format(sexo))