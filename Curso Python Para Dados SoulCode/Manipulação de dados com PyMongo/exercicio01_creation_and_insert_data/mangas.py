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
collection_manga = dbname['mangas']

item_manga1 = {
  "_id": "mng001",
  "titulo": "A Noite da Princesa Uriko",
  "editora": "Conrad",
  "volumes": "1"
}

item_manga2 = {
  "_id": "mng002",
  "titulo": "Alive",
  "editora": "Panini"
}

item_manga3 = {
  "titulo": "Battle Angel Alita",
  "editora": "JBC",
  "volumes": "9"
}

item_manga4 = {
  "_id": "mng004",
  "titulo": "Edens Zero",
  "editora": "JBC",
  "volumes": "13 de 28+"
}

item_manga5 = {
  "_id": "mng005",
  "titulo": "One Piece",
  "editora": "Panini",
  "volumes": "16 de 106+"
}


collection_manga.insert_many([
  item_manga1,
  item_manga2,
  item_manga3,
  item_manga4,
  item_manga5
])

imprimirLinha(2)
imprimirMensagem('DADOS INSERIDOS COM SUCESSO!', 2)
imprimirLinha(2)
