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
collection_books = dbname['livros']

# dictionary

item_book1 = {
    "_id": "bk001",
    "nome_livro": "Harry Potter e a Pedra Filosofal",
    "editora": "Rocco",
    "autor(a)": "J.K. Rowling",
    "preco": 42,
    "desconto": "10%"
}

item_book2 = {
    "_id": "bk002",
    "nome_livro": "O Programador Pragmático",
    "editora": "Bookman",
    "autor(a)": "Andrew Hunt e David Thomas",
    "preco": 157.50,
    "desconto": "15%"
}

item_book3 = {
    "nome_livro": "Seja foda",
    "editora": "Buzz",
    "autor(a)": "Caio Carneiro",
    "preco": 37.47,
    "desconto": "10%"
}

item_book4 = {
    "_id": "bk004",
    "nome_livro": "Cinquenta tons de cinza",
    "editora": "Intríseca",
    "autor(a)": "E.L. James",
    "preco": 28.90
}

item_book5 = {
    "_id": "bk005",
    "nome_livro": "Eu sou o número 4",
    "editora": "Intríseca",
    "autor(a)": "Pittacus Lore",
    "preco": 12.90
}

item_book6 = {
    "nome_livro": "Querido John",
    "autor(a)": "Nicholas Sparks",
    "preco": 24.89,
    "desconto": "8%"
}

collection_books.insert_many([
    item_book1,
    item_book2,
    item_book3,
    item_book4,
    item_book5,
    item_book6
])

imprimirLinha(2)
imprimirMensagem('DADOS INSERIDOS COM SUCESSO!', 2)
imprimirLinha(2)