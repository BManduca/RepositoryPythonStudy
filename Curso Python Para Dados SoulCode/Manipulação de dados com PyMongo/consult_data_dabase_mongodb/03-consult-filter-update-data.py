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

def imprimirLinha20(cor=0):
    print(colors[cor], end='')
    print('-=-'*20)
    print(colors[0], end='')

def imprimirLinha(cor=0):
    print(colors[cor], end='')
    print('-=-'*5)
    print(colors[0], end='')


def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://manduca:xmd8Xvu1XCcoIz6Q@mydatabase.8vdqilo.mongodb.net/"

    # aqui acontece a nossa conexao com o mongodb
    client = MongoClient(CONNECTION_STRING)

    imprimirLinha20(2)
    imprimirMensagem('Conectado com sucesso!', 2)
    imprimirLinha20(2)

    return client['mandDatabase']


dbname = get_database()
collection_name = dbname["itens_mandDatabase"]


# para atualizar utilizamos a palavra reservada set, que faz o update das informações
# collection_name.update_many(
#     {"desconto_maximo":"50%"},
#     {"$set":{"desconto_maximo":"55%"}}
# )

# na seguinte forma 
collection_name.update_one(
    {"nome_item":{"$regex":"Drone"}}, {"$set":{"desconto_maximo":"100%"}}
)

imprimirLinha20(4)
imprimirMensagem("Dados atualizados com sucesso!", 4)
imprimirLinha20(4)

detalhes_items = collection_name.find()

print()
for item in detalhes_items:
    print(item)