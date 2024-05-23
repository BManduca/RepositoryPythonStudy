from pymongo import collection
import time
from os import system

colors = (
    '\033[0m', # 0 - SEM COR
    '\033[0;31m', # 1 - VERMELHO
    '\033[0;32m', # 2 - VERDE
    '\033[0;33m', # 3 - AMARELO
    '\033[0;34m', # 4 - AZUL
    '\033[0;35m', # 5 - ROXO
    '\033[0;36m', # 6 - BRANCO
)


"""
    - Crie um script contendo cinco funções:
        - Criar itens, onde o usuário pode selecionar a quantidade de campos => OK
        - Mostrar todos os documentos => OK
        - Deletar documentos pelo ID => 
        - Deletar toda a coleção do banco de dados => 
        - Atualizar documentos por ID ou por campos => 
"""
    
def messageCentralized(msg, wid):
    tam = len(msg)
    space = (wid - tam) // 2
    text = ' ' * space + msg + ' ' * space
    # Se o texto não puder ser centralizado perfeitamente, ajuste uma posição para a direita
    if len(text) < wid:
        text += ' '
        
    return text

def printTextCentralized(msg, wid, cor=0):
    message = messageCentralized(msg, wid)
    print(colors[cor], end='')
    print(message)
    print(colors[0], end='')

def imprimirLinha20(cor=0):
    print(colors[cor], end='')
    print('-=-'*20)
    print(colors[0], end='')

def imprimirLinha28(cor=0):
    print(colors[cor], end='')
    print('-=-'*28)
    print(colors[0], end='')

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://manduca:xmd8Xvu1XCcoIz6Q@mydatabase.8vdqilo.mongodb.net/"

    client = MongoClient(CONNECTION_STRING)

    print(' ')
    imprimirLinha28(2)
    printTextCentralized('EFETUANDO CONEXÃO COM O BANCO...', 84, 2)
    time.sleep(2)
    printTextCentralized('>>>>>', 84, 2)
    time.sleep(2)
    printTextCentralized('>>>', 84, 2)
    time.sleep(2)
    printTextCentralized('>', 84, 2)
    time.sleep(2)
    printTextCentralized('CONECTADO AO BANCO COM SUCESSO!', 84, 2)
    imprimirLinha28(2)
    print(' ')
    time.sleep(2)
    system('clear')

    return client['exerciseDatabase']

def showMenu():
    imprimirLinha28(3)
    printTextCentralized('BEM-VINDO AO PROGRAMA DE MANIPULAÇÃO DE DADOS!', 80, 3)
    printTextCentralized('SELECIONE UMA OPÇÃO: ', 80, 3)
    print(' ')
    printTextCentralized('1 => CADASTRO DE DOCUMENTO', 80, 3)
    printTextCentralized('2 => MOSTRAR TODOS OS DOCUMENTOS', 80, 3)
    printTextCentralized('3 => DELETAR UM DOCUMENTO ATRAVÉS DO ID', 80, 3)
    printTextCentralized('4 => DELETAR TODA A COLEÇÃO DO BANCO DE DADOS', 80, 3)
    printTextCentralized('5 => ATUALIZAR CAMPOS DO(S) DOCUMENTO(S) DO BANCO DE DADOS', 80, 3)
    printTextCentralized('0 => FINALIZAR PROGRAMA', 80, 3)
    imprimirLinha28(3)


"""
This Python function allows the user to input a specified number of key-value pairs to create a
document and store it in a MongoDB collection.
"""
def registerDocument():
    dbname = get_database()
    collection_name = dbname['exerciseListDatabase']
    qtd = int(input('ENTRE COM A QUANTIDADE DE CAMPOS QUE O DOCUMENTO TERÁ: '))
    dct = dict(input('DIGITE A CHAVE E O VALOR SEPARADO POR ESPAÇOS: ').split() for _ in range(qtd))

    print(' ')
    imprimirLinha28(2)
    printTextCentralized(f'{dct}', 84,2)
    imprimirLinha28(2)
    collection_name.insert_one(dct)
    
    time.sleep(2)

    print(' ')
    imprimirLinha28(2)
    printTextCentralized('DADOS CADASTRADOS COM SUCESSO!', 84, 2)
    imprimirLinha28(2)
    print(' ')
    time.sleep(5)
    system('clear')


"""
This Python function retrieves and displays documents from a MongoDB collection with a styled
message for each item, and then clears the screen after a delay.
"""
def showDocuments():
    dbname = get_database()
    collection_name = dbname['exerciseListDatabase']
    detalhes_items = collection_name.find()
    print(' ')

    imprimirLinha28()
    for item in detalhes_items:
        printTextCentralized(f'{item}', 84)
    imprimirLinha28()
    print(' ')

    time.sleep(8)
    system('clear')


def deleteDocumentForID():
    dbname = get_database()
    collection_name = dbname['exerciseListDatabase']
    deleteID = str(input('ENTRE COM O ID DO DOCUMENTO QUE SERÁ DELETADO: '))
    
    collection_name.delete_one({"_id": deleteID})
    
    time.sleep(2)
    
    print(' ')
    imprimirLinha28(1)
    printTextCentralized(f'DOCUMENTO {deleteID} FOI DELETADO COM SUCESSO!', 80, 1)
    imprimirLinha28(1)
    print(' ')
    time.sleep(5)
    system('clear')


def deleteAllCollectionDB():
    dbname = get_database()
    collection_name = dbname['exerciseListDatabase']
    
    answer = str(input('DESEJA REALMENTE DELETAR TODA A COLEÇÃO DO BANCO DE DADOS? ')).upper()
    time.sleep(2)
    
    while answer not in 'SN':
        answer = str(input('DESEJA REALMENTE DELETAR TODA A COLEÇÃO DO BANCO DE DADOS? ')).upper()
        time.sleep(2)
    print(' ')
    
    if answer == 'N':
        time.sleep(2)
        printTextCentralized('RETORNANDO PARA O MENU PRINCIPAL..', 80, 2)
        print()
        printTextCentralized('3', 80, 2)
        time.sleep(2)
        printTextCentralized('2', 80, 2)
        time.sleep(2)
        printTextCentralized('1', 80, 2)
        time.sleep(2)
        system('clear')        
    else:
        collection_name.drop()
        dbname.drop_collection()
        printTextCentralized('DELETANDO COLEÇÃO...')
        print()
        printTextCentralized('3', 80, 2)
        time.sleep(2)
        printTextCentralized('2', 80, 2)
        time.sleep(2)
        printTextCentralized('1', 80, 2)
        time.sleep(2)
        printTextCentralized('COLEÇÃO DELETADA COM SUCESSO!', 80, 2)


def updateDocuments():
    dbname = get_database()
    collection_name = dbname['exerciseListDatabase']
    
    printTextCentralized('MENU DE ATUALIZAÇÃO\n1 - ATUALIZAR DOCUMENTO POR ID \n2 - ATUALIZAR DOCUMENTO POR CAMPO ', 80, 3)
    print(' ')
    optionUser = str(input('INSIRA A OPÇÃO QUE GOSTARIA DE REALIZAR: '))
    time.sleep(3)
    system('clear')
    
    while optionUser not in '12':
        printTextCentralized('MENU DE ATUALIZAÇÃO\n1 - ATUALIZAR DOCUMENTO POR ID\n2 - ATUALIZAR DOCUMENTO POR CAMPO', 80, 3)
        print(' ')
        optionUser = str(input('INSIRA A OPÇÃO QUE GOSTARIA DE REALIZAR: '))
    print(' ')
    
    if optionUser == '1':
        changeID = str(input('INSIRA O ID DO DOCUMENTO A SER ALTERADO: '))
        print(' ')
        key = str(input('INSIRA O CAMPO A SER ALTERADO: '))
        value = str(input('INSIRA O NOVO VALOR DO CAMPO: '))
        
        collection_name.update_one({"_id":changeID}, {"$set":{key:value}})
        
        print(' ')
        imprimirLinha28(2)
        printTextCentralized('ATUALIZAÇÃO REALIZADA COM SUCESSO!', 80, 2)
        imprimirLinha28(2)
        print(' ')
        time.sleep(3)
        system('clear')
    elif optionUser == '2':
        keySearch = str(input('INSIRA O CAMPO A SER ANALISADO: '))
        valueSearch = str(input('INSIRA O VALOR DO CAMPO A SER ANALISADO: '))
        print('')
        keyChange = str(input('INSIRA O CAMPO A SER ALTERADO:'))
        valueChange = str(input('INSIRA O NOVO VALOR: '))
        
        collection_name.update_many({keySearch:valueSearch}, {"$set":{keyChange, valueChange}})
        

def main():
    while True:
        showMenu()
        print( )
        
        textChoice = 'INSIRA A OPÇÃO DESEJADA: '
        
        theChoice = input(f'{textChoice}')

        if theChoice == '1':
            registerDocument()
        elif theChoice == '2':
            showDocuments()
        elif theChoice == '3':
            deleteDocumentForID()
        elif theChoice == '4':
            deleteAllCollectionDB()
        elif theChoice == '5':
            updateDocuments()
        elif theChoice == '0':
            print('\n')
            imprimirLinha28(1)
            printTextCentralized('FINALIZANDO PROGRAMA!', 84, 1)
            imprimirLinha28(1)
            print('\n')
            break
        else:
            print('\n')
            print('OPÇÃO INVÁLIDA! POR FAVOR,\nINSIRA NOVAMENTE UMA OPÇÃO DO MENU!')
            print('\n')
            time.sleep(5)
            system('clear')


if __name__ == "__main__":
    main()