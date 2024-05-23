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
    import pymongo

    CONNECTION_STRING = "mongodb+srv://manduca:xmd8Xvu1XCcoIz6Q@mydatabase.8vdqilo.mongodb.net/"

    # aqui acontece a nossa conexao com o mongodb
    client = MongoClient(CONNECTION_STRING)

    imprimirLinha(2)
    imprimirMensagem('Conectado com sucesso!', 2)
    imprimirLinha(2)

    return client['mandDatabase']


dbname = get_database()
collection_name = dbname["itens_mandDatabase"]


#DICTIONARY
item_1 = {
    "_id": "SC001",
    "nome_item": "Livro",
    "desconto_maximo": "10%",
    "REF": "RRGSFF001",
    "preco": 340,
    "categoria": "Físico"
}

item_2 = {
    "_id": "SC002",
    "nome_item": "Camêra",
    "desconto_maximo": "15%",
    "REF": "RRGSJ001S4",
    "preco": 540,
    "categoria": "Físico"
}

item_3 = {
    "nome_item": "Drone",
    "desconto_maximo": "28%",
    "REF": "DRFGHE12452S",
    "preco": 990,
    "categoria": "Físico"
}

item_4 = {
    "nome_item": "Geladeira",
    "desconto_maximo": "35%",
    "REF": "GLR4154DSFS",
    "preco": 1850,
    "categoria": "Físico"
}

item_5 = {
    "_id": "SC005",
    "nome_item": "Cama",
    "desconto_maximo": "22%"
}

# collection_name.insert_many([
#     item_1,
#     item_2,
#     item_3
# ])

collection_name.insert_one(item_1)
# collection_name.insert_one(item_5)

imprimirLinha(2)
imprimirMensagem('Dados inseridos com sucesso!', 2)
imprimirLinha(2)