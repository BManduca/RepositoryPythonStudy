from flask import Flask, request, jsonify
#Code128 é uma codificação para criar a tag
from barcode import Code128
from barcode.writer import ImageWriter

# criando um servidor em flask
app = Flask(__name__)


# decorador para construir nossas rotas
@app.route('/create_tag', methods=["POST"])

# function create_tag
def create_tag():
    body = request.json
    product_code = body.get('product_code')
    
    generate_tag = Code128(product_code, writer=ImageWriter())
    
    path_from_tag = f'./Public/BarCodeGenerate/{generate_tag}'
    generate_tag.save(path_from_tag)
    
    return jsonify({"tag path": path_from_tag})

# função main em python
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
