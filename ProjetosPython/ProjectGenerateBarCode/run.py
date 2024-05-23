# levantando o servidor
from src.main.server.server import app

# criando método main
# rodar em localhost, na porta 3000 e com debug ativado
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
