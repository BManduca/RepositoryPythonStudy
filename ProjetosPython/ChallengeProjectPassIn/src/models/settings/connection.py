from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# para evitar a exportação da classe DBConnectionHandler, declaramos ela como privada.
class __DBConnectionHandler:
    # método construtor
    def __init__(self) -> None:
        self.__connection_string = "{}:///{}".format(
            "sqlite",
            "storage.db"
        )
        # motor de conexão com nosso DB
        self.__engine = None
        self.session = None
        
    def connect_to_db(self) -> None:
        # passando a nossa string de conexão para criação da nossa engine
        self.__engine = create_engine(self.__connection_string)
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        # UMA SESSÃO BASEADA NO MECANISMO DE CONEXÃO QUE TEMOS COM NOSSO DB
        self.session = session_maker(bind=self.__engine)
        return self
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        # FECHANDO CONEXÃO
        self.session.close()

# objeto único para toda aplicação        
db_connection_handler = __DBConnectionHandler()
        