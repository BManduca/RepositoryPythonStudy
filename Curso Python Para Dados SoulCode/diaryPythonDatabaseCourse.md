## Manipulação de dados com PyMongo

- Install your driver
    - python -m pip install "pymongo[srv]"
<br><br>
- Iniciando:
    - Inicialmente criar uma conta no MondoDB
    - criar uma database
    - Criar um user -> Database Access
    - Para fazer a conexão, é necessário 'pegar' uma connection string e adicionar dentro da aplicação => essa connection string é possível pegar dentro do mongo, na área de connect da sua database.
        - database -> Connect
    - Sempre validar se o IP esta pegando corretamente
        - é possível verificar dentro da pagina do mongodb atlas em: Security -> Network Access


- ## Inserindo coleções nas databases
    - 'dentro' de uma database podemos criar um document e inserir ele via mongodb, através de uma estrutura JSON e logo em seguida inserir os dados 


- ## Acessando Banco de Dados MongoDB com Python
    - ### Estrutura do Mongodb - Aula 24
        - O Mongodb é construído por uma base de dados
        - Essa base de dados vai ter coleções
            - São unidades básicas de dados. 
            - Formatados como Binary JSON
            - esses documentos podem armazenar vários tipos de dados e ser distribuídos para diversos sistemas.
        - As coleções vão ter documentos
        - Os documentos são inseridos por nós usuários.


- ## Exercício de Treino
  - criar uma base de dados MongoDB contendo as seguintes coleções: 
    - Livros (20 documentos)
    - Revistas (15 documentos)
    - Jornais (15 documentos)
    - Mangás (10 documentos)

  - Obs.: 
    - todos os documentos devem ter pelo menos 4 campos
    - alguns documentos devem ter mais ou menos campos que os demais
    - deverá haver _id do tipo Object e declarado pelo usuário
    - devem haver campos dos tipos: Int, Double, String e ObjectId

- ## Lista de dados - Parte 1
    - Funções MongoDB
        - Procedimento para realizar consultas dentro do MongoDB: find()
        - Para realizar uma pesquisa é so usar o find seguido de um parâmentro, como por exemplo: 
            - detalhes_itens = collection_name.find({"categoria":"Físico"})
        - Pesquisas podem ser realizadas usando de maneira tradicional, com valores lógicos e também com base em Regex.
            - Exemplos:
                - collection_name.find({"categoria":"Físico"}) -> maneira tradicional
                - collection_name.find({"$or": [{"desconto_maximo":"22%"},{"desconto_maximo":"35%"}]}) -> operadores lógicos
                - collection_name.find({"nome_item": {"$regex":"^Ca"}}) -> uso do Regex

- ## Listagem de dados - pt. 1 (4:18)
  - find() -> responsável por exibir dados no MongoDB
    - podemos também filtrar usando o find e passando um parâmetro específico, para reduzir mais o retorno da busca.
      > 
        find("categoria":"Online")
  - distinct() -> exibe os dados sem repetição
  - limit() -> limita a quantidade de dados a serem mostrados
  - skip() -> 'pular'a quantidade de itens definido pelo usuario e mostrar somente os itens resultantes dessa ação em tela

- ## Atualização de Dados
    - Para atualizar utilizamos a palavra reservada set, que faz o update das informações
    - No exemplo abaixo, estaremos atualizando vários registros, através do update_many()
        >
            collection_name.update_many(
                {"desconto_maximo":"50%"},
                {"$set":{"desconto_maximo":"55%"}}
            )

    - Para atualizar um registro somente, aplicamos o update_one()
        - Logo abaixo conseguimos verificar através de um regex, aonde vai ser buscado em qualquer parte do texto,
        a palavra Drone e caso seja encontrado, o desconto_maximo vai para 100%, mas somente de um item, por causa do update_one()
        > 
            collection_name.update_one(
                {"nome_item":{"$regex":"Drone"}}, {"$set":{"desconto_maximo":"100%"}}
            )

- ## Exclusão de Dados
    - Podemos realizar a exclusão de dados da seguinte forma:
        - para um único elemento:
            >
                collection_name.delete_one({"_id": "SC001"})

                detalhes_itens = collection_name.find()
                for item in detalhes_itens:
                    print(item)

    - Para esvaziar totalmente a coleção, podemos utilizar o Drop:
        >
            collection_name.drop()