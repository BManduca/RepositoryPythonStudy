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

# distinct -> exibe os dados sem repetição
# detalhes_items = collection_name.distinct("nome_item")

#limit -> limita a quantidade de dados a serem mostrados
# detalhes_items = collection_name.find({'categoria':'Físico'}).limit(2)

#skip -> 'pular'a quantidade de itens definido pelo usuario e mostrar somente os itens resultantes dessa ação em tela
detalhes_items = collection_name.find({}, {"nome_item", "desconto_maximo"}).skip(2)

# detalhes_items = collection_name.find()

print(' ')
# imprimirLinha(3)
for item in detalhes_items:
    # print(f'{item:^16}')
    print(item)
# imprimirLinha(3)
print(' ')