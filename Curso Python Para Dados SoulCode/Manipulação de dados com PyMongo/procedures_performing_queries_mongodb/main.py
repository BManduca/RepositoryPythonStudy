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


    CONNECTION_STRING = "mongodb+srv://manduca:xmd8Xvu1XCcoIz6Q@mydatabase.8vdqilo.mongodb.net/"

    client = MongoClient(CONNECTION_STRING)

    imprimirLinha(2)
    imprimirMensagem('CONECTADO COM SUCESSO!', 2)
    imprimirLinha(2)

    return client['mandDatabase']

dbname = get_database()
collection_name = dbname["itens_mandDatabase"]

# detalhes_itens = collection_name.find()


"""
em outras palavras, seria detalhes_itens, me forneça 
apenas os dados em que a categoria seja igual a Físico.

detalhes_itens = collection_name.find({
    "categoria":"Físico"
})
"""


"""
utilizando valores lógicos para realizar a consulta

detalhes_itens = collection_name.find({
    "$or": [{"desconto_maximo":"22%"},{"desconto_maximo":"35%"}]
})
"""


"""
consultas através de regex, neste caso buscamos através de fragmentos de texto.
"""

detalhes_itens = collection_name.find({
    "nome_item": {"$regex":"^Ca"}
})



for item in detalhes_itens:
    imprimirMensagem(f'{item}', 4)

