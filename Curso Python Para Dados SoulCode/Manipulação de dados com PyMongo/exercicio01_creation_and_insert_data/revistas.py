from pymongo import collection

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


    CONNECTION_STRING = 'mongodb+srv://manduca:xmd8Xvu1XCcoIz6Q@mydatabase.8vdqilo.mongodb.net/'

    client = MongoClient(CONNECTION_STRING)

    imprimirLinha(2)
    imprimirMensagem('CONECTADO COM SUCESSO!', 2)
    imprimirLinha(2)

    return client['mandDatabase']

dbname = get_database()
collection_magazines = dbname['revistas']

# dictionary


item_magazine1 = {
    "_id": "mg001",
    "nome_revista": "Quatro rodas",
    "editora": "Editora Abril",
    "data_criacao": "agosto de 1960",
    "preço": 96
}

item_magazine2 = {
    "nome_revista": "Veja",
    "editora": "Editora Abril",
    "data_criacao": "11 de setembro de 1968",
    "preço": 358.80
}

item_magazine3 = {
    "_id": "mg003",
    "nome_revista": "Exame",
    "editora": "Editora e Comercio Valongo",
    "data_criacao": "julho de 1967",
    "preço": 129.90
}

item_magazine4 = {
    "_id": "mg004",
    "nome_revista": "Superinteressante",
    "editora": "Editora Abril",
    "data_criacao": "setembro de 1987",
    "preço": 96
}

collection_magazines.insert_many([
    item_magazine1,
    item_magazine2,
    item_magazine3,
    item_magazine4
])

imprimirLinha(2)
imprimirMensagem('DADOS INSERIDOS COM SUCESSO!', 2)
imprimirLinha(2)