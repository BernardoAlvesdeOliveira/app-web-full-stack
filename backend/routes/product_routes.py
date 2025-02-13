from flask import Blueprint, request, jsonify
from db_utils import get_db_connection

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/save', methods=['POST'])
def data_save():
    try:
        if not request.is_json:
            return jsonify({"error": "Aparentemente o tipo do conteúdo NÃO é um json. Esperando application/json"}), 415
        
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"erro": "Erro ao processar json"}), 400
        
        name = data.get('name')
        amount = data.get('amount')
        if not name or not isinstance(amount, int):
            return jsonify({"erro": "Dados, inválidos, por favor informe o nome do produto e a quantidade!"}), 400
        
        connection = get_db_connection()
        if not connection:
            return jsonify({"erro": "Falha na conexão com o banco de dados"}), 500
        
        curso = connection.cursor()
        query = "INSERT INTO product (name, amount) VALUES (%s, %s)"
        curso.execute(query, (name, amount))
        connection.commit()

        return jsonify({"mensagem": "Dados salvos com sucesso!"}), 201
    
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado: {e}"}), 500
    
    finally:
        if "curso" in locals() and curso:
            curso.close
        if "connection" in locals() and connection:
            connection.close()