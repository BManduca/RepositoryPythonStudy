colors = (
    '\033[0m', # 0 - SEM COR
    '\033[0;31m', # 1 - VERMELHO
    '\033[0;32m', # 2 - VERDE
    '\033[0;33m', # 3 - AMARELO
    '\033[0;34m', # 4 - AZUL
    '\033[0;35m', # 5 - ROXO
    '\033[0;36m', # 6 - BRANCO
)

def imprimirMensagem(msg, cor=0):
    print(colors[cor], end='')
    print(f'{msg:^60}')
    print(colors[0], end='')

def imprimirLinha(cor=0):
    print(colors[cor], end='')
    print('-=-'*20)
    print(colors[0], end='')


def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING ='mongodb+srv://manduca:xmd8Xvu1XCcoIz6Q@mydatabase.8vdqilo.mongodb.net/'

    client = MongoClient(CONNECTION_STRING)

    imprimirLinha(2)
    imprimirMensagem('CONECTADO COM SUCESSO!', 2)
    imprimirLinha(2)

    return client['mandDatabase']


dbname = get_database()
collection_newspapppers = dbname['jornais']

# dictionary

item_newspapper1 = {
    "_id": "np001",
    "nome_jornal": "Página 3",
    "fundador": "Waldemar Cezar Neto",
    "data_criacao": "26 de julho de 1991",
    "cidade": "Balneário Camboriú"
}

item_newspapper2 = {
    "_id": "np002",
    "nome_jornal": "Diário Catarinense",
    "fundador": "Maurício Sirotsky Sobrinho",
    "data_criacao": "26 de julho de 1991",
    "cidade": "Balneário Camboriú"
}

item_newspapper3 = {
    "nome_jornal": "Diarinho",
    "fundador": "Dalmo Vieira",
    "data_criacao": "12 de janeiro de 1979",
    "cidade": "Itajaí e Balneário Camboriú"
}

item_newspapper4 = {
    "_id": "np004",
    "nome_jornal": "A Tribuna",
    "fundador": "Saimon Novack",
    "data_criacao": "5 de novembro de 2005",
    "cidade": "Criciúma"
}

collection_newspapppers.insert_many([
    item_newspapper1,
    item_newspapper2,
    item_newspapper3,
    item_newspapper4
])

imprimirLinha(2)
imprimirMensagem('DADOS INSERIDOS COM SUCESSO!', 2)
imprimirLinha(2)