## Diário de aprendizado

- ### Neste espaço será armazenado todas as explicações, termos e novidades expostas dentro do projeto.

- ### Material complementar:
    - https://efficient-sloth-d85.notion.site/Python-17d72ad083874c57b01a4d9d76f92a25
    - **repo rocket**: https://github.com/rocketseat-education/nlw-unite-python/tree/main

___________________________________________________________________________________________________ 

<br />
<br />

## Instalação de aplicações/ferramentas dentro do projeto

### DBeaver
- **instalação**:
    - Adicione o repositório do programa: 
        - echo "deb https://dbeaver.io/debs/dbeaver-ce /" | sudo tee /etc/apt/sources.list.d/dbeaver.list
        - wget -O - https://dbeaver.io/debs/dbeaver.gpg.key | sudo apt-key add -
    - Atualizar gerenciador de pacotes:
        - sudo apt-get update
    - Instalando programa:
        - sudo apt-get install dbeaver-ce

<br />

### Virtualenv
- **instalação**: pip3 install virtualenv
- **Create and Use Virtual Environments**
    - python3 -m venv .venv
- **Activate a virtual environment**
    - source .venv/bin/activate

<br />

### SQLAlchemy
- **instalação**: pip3 install SQLAlchemy
- **doc**: https://www.sqlalchemy.org/docs/

<br />

### Pytest
- **instalação**: pip3 install pytest
- **doc**: https://docs.pytest.org/en/stable/.

<br />

### Pylint
- Pylint é um analisador de código estático para python 2 ou 3.
- **instalação**: pip3 install pylint

<br />

### Pre-commit
- Um framework para gerenciar e manter pre-commits multilíngues
- instalação: pip3 install pre-commit -> pre-commit install

<br />

### Flask
- Framework de aplicação Web, que foi projetado com intuito de escalar aplicações web complexas, de uma maneira inicial rápida e fácil.
- instalação: pip3 install -U Flask

### Flask-Cors
- É uma extensão do Flask para lidar com Cross Origin Resource Sharing (CORS), tornando possível o cross-origin AJAX
- Basicamente para conseguirmos ter uma boa comunicação com o front-end, caso seja efetuado algum tipo de acesso
- instalação: pip3 install -U Flask-Cors

<br />

### Criando um arquivo geral de configuração Pylint
- pylint --generate-rcfile > .pylintrc

<br />

### Requirements
- Arquivo para registrar as dependências e quais são suas versões
- .venv/bin/pip3 freeze > requirements.txt    


___________________________________________________________________________________________________

## Anotações

- Entidade vs. Repositório
    - Repositório: É aonde realizamos as ações, inserimos dados, buscamos dados...

    - Entidade: Declaramos como que é a estrutura de armazenamento, por exemplo, nossa tabela Events.

- uuid
    - Estrutura de identidade com base em texto

- abrindo a session -> database.session
            
- fazendo uma querie em Events -> .query(Events)
            
- filtrando pelo id, aonde id do event tem que ser o id que vai 
ser enviado no metodo -> .filter(Events.id == event_id)
            
- retornando um único registro -> .one()
            
```
event = (
    database.session
        .query(Events)    
        .filter(Events.id == event_id)
        .one()
)
```

## Tratativa de Erros
- Para realizar a tratativa de erros de uma forma mais 'humanizada' podemos envolver a parte de lógica de inserção de dados com um bloco try-catch

```
def insert_event(self, events_info: Dict) -> Dict:
# entrando no contexto (criando a seção)
with db_connection_handler as database:
    try:
        event = Events(
            id = events_info.get("uuid"),
            title = events_info.get("title"),
            details = events_info.get("details"),
            slug = events_info.get("slug"),
            maximum_attendees = events_info.get("maximum_attendees")
        )
        database.session.add(event)
        database.session.commit()
    
        return events_info
    except Exception as exception:
        database.session.rollback()
```

## Respostas HTTP
- STATUS_CODE => retorno que vai ser recebido ao fazer uma request

- BODY => 'corpo' da response que será recebido após executar a request


## Criando um gerente de eventos
- teremos um construtor para utilizar nosso EventsRepository, ou seja, iremos usar uma instancia do EventsRepository, para que seja possível a classe toda utilizar os beneficios da mesma
- Método register, para registrar os eventos, aonde teremos um um http_request como param, para retornar o HttpResponse


```
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_response import HttpResponse

class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()
        
        
    def register(self, http_request) -> HttpResponse:
        pass
```

<!-- 6:43 -->