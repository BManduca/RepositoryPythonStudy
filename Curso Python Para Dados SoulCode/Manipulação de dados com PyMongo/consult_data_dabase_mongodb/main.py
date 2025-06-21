import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

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
    CONNECTION_STRING = os.getenv('MONGO_URI')

    if not CONNECTION_STRING:
        imprimirMensagem('Erro: MONGO_URI não está definido no .env', 1)
        exit(1)

    # aqui acontece a nossa conexao com o mongodb
    client = MongoClient(CONNECTION_STRING)

    imprimirLinha(2)
    imprimirMensagem('Conectado com sucesso!', 2)
    imprimirLinha(2)

    return client['mandDatabase']


dbname = get_database()
collection_name = dbname["itens_mandDatabase"]

#somente aplicando find sem parâmetro algum
# detalhes_items = collection_name.find()

# consulta aplicando parâmetro de filtro para um elemento especifico
# detalhes_items = collection_name.find({
#     "categoria":"Físico"
# })


# fazendo consulta passando parâmetro baseado em um operador lógico or 
# detalhes_items = collection_name.find({
#     "$or" : [
#         {"desconto_maximo":"15%"},
#         {"desconto_maximo":"35%"}
#     ]
# })


# fazendo consulta passando parâmetro baseado em um operador lógico and
# detalhes_items = collection_name.find({
#     "$and" : [
#         {"categoria":"Físico"},
#         {"desconto_maximo":"35%"}
#     ]
# })

# consultas aplicando parâmetro através de Regex
detalhes_items = collection_name.find({
    "nome_item":{"$regex":"^Ca"}
})

for item in detalhes_items:
    print(item)
