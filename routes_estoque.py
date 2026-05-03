from flask import Flask, jsonify, request
from models.model import Estoque
from data_validacoes.validacoes import validar_campos, gerar_data_agora, gerar_horario_agora, validar_preco_quantidade


db = Estoque()
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'msg': 'Api conectada com sucesso !'}), 200

@app.route('/cadastrarprodutos', methods=['POST']) 
def cadastrar_produto():
    dados = request.get_json()
    if not dados:
        return jsonify({'msg': 'Requisição inválida'}), 404
    
    produto,preco,quantidade = dados.get('produto'), dados.get('preco'), dados.get('quantidade')

    if not validar_campos(produto,preco,quantidade):
        return jsonify({'msg': 'Campos obrigatórios não foram preenchidos !'}), 400
    if not validar_preco_quantidade(preco,quantidade):
        return jsonify({'msg': 'Valores negativos não são validos !'}), 400
    
    cadastrou = db.cad_produtos(produto,preco,quantidade,gerar_horario_agora(),gerar_data_agora())
    if not cadastrou:
        return jsonify({'msg': 'O produto já está cadastrado !'}), 400
    return jsonify({'cadastrado': cadastrou}), 201

@app.route('/listprodutos', methods=['GET'])
def listar_produtos():
    produtos = db.list_produtos()
    if not produtos:
        return jsonify({'msg': 'Não a produtos cadastrados'}), 200
    return jsonify(produtos), 200

@app.route('/buscarproduto/<int:id>', methods=['GET'])
def buscar_produto(id):
    produto = db.get_produto(id)
    if not produto:
        return jsonify({'msg': 'Produto não foi encontrado !'}), 404
    return jsonify(produto)

@app.route('/deletarprodutos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    deletou = db.delete_produto(id)
    if not deletou:
        return jsonify({'msg': 'Produto não foi encontrado !'}), 404
    return jsonify({'msg': f'Produto do id {id} deletado com sucesso'}), 200

@app.route('/atualizarprodutoall/<int:id>', methods=['PUT'])
def atualizar_produtos(id):
    dados = request.get_json()
        
    if not dados:
        return jsonify({'msg': 'Requisição inválida'}), 400
    
    nome,preco,qtd = dados.get('nome'),dados.get('preco'),dados.get('quantidade')
    
    atualizou =  db.update_produto_all(nome,preco,qtd,id)
    if atualizou:
        return jsonify({'msg': f'Produto id {id} atualizado com sucesso. Horário de atualização {gerar_horario_agora()}'}), 200
    return jsonify({'msg': 'Produto não foi encontrado !'}), 400

@app.route('/atualizarprodutoone/<int:id>', methods=['PATCH'])
def atualizar_produto(id):    
    dados = request.get_json()

    if not dados:
        return jsonify({'msg': 'Requisição inválida'}), 404
    
    nome,preco,qtd = dados.get('nome'),dados.get('preco'),dados.get('quantidade')

    atualizou =  db.update_produto_one(nome,preco,qtd,id)
    if not atualizou:
        return jsonify({'msg': 'Produto não foi encontrado !'}), 400
    return jsonify({'msg': 'Produto atualizado com sucesso !'}), 200

if __name__ == '__main__':
    app.run(debug=True)