from typing import Dict

'''
    CLASSE DEFINIDA NECESSARIAMENTE PARA
    RETIRAR TODAS AS INFOS DO PROTOCOLO
    HTTP E COLOCAR NOS PARAMS DE ENTRADA
'''
class HttpRequest:
    def __init__(
            self,
            # caso os elementos não seja inseridos/preenchidos, serão populados com None
            header: Dict = None,
            body: Dict = None,
            query_params: Dict = None,
        ) -> None:
        # salvando todos os elementos que entrarem no nosso método construtor
        self.header = header
        self.body = body
        self.query_params = query_params
