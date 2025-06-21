import os
import pandas as pd
import time

def register_product():
    os.system('clear')
    nome_produto = input('\nInforme nome do produto: ')
    cor_produto = input('Informe a cor do produto: ')
    qtde_produto = input('Informe a quantidade do produto: ')
    valor_entrada_produto = float(input('Informe o valor de entrada do produto: '))
    valor_venda_produto = float(input('Informe o valor de venda do produto: '))

    # armazenando os dados em um dicionário
    product_data = {
        'Nome produto': [nome_produto],
        'Cor produto': [cor_produto],
        'Quantidade': [qtde_produto],
        'Valor entrada': [valor_entrada_produto],
        'Valor venda': [valor_venda_produto]
    }

    # convertendo o dicionario para um DataFrame
    dataframe = pd.DataFrame(product_data)

    # arquivo excel
    file_excel = 'lista_produtos_hsimports.xlsx'

    if os.path.exists(file_excel):
        # se o arquivo ja existir, será anexado os dados ao final da lista
        # sem sobreescrever o que ja existe
        dataframe_existente = pd.read_excel(file_excel)
        new_dataframe_combined = pd.concat([dataframe_existente, dataframe], ignore_index=True)
        new_dataframe_combined.to_excel(file_excel, index=False)
    else:
        # se caso o arquivo não existir, será criado um novo arquivo para fazer o registro
        dataframe.to_excel(file_excel, index=False)

    print('\nRegistro feito com sucesso!')
    time.sleep(3)
    os.system('clear')

def main():

    while True:
        register_product()
        new_register = input('\nGostaria de cadastrar outro produto? (s/n): ').strip().lower()

        if new_register != 's':
            print('\nCadastro finalizado com sucesso.')
            break

if __name__ == '__main__':
    main()
