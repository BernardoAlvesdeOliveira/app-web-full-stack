import sqlite3

from flask import Blueprint, request, jsonify
from db_utils import get_db_connection

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    connection = get_db_connection()
    if not connection:
        return jsonify({"erro": "Database connection failed"}), 500

    try:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, product_name, amount, data_cadastro "
            "FROM product ORDER BY id DESC"
        )
        products = [dict(row) for row in cursor.fetchall()]
        cursor.close()
        return jsonify(products), 200
    except Exception as e:
        return jsonify({"erro": f"Error fetching products: {e}"}), 500
    finally:
        connection.close()

@product_bp.route('/save', methods=['POST'])
def data_save():
    try:
        if not request.is_json:
            return jsonify({"error": "The content type is not JSON. Expected application/json"}), 415
        
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"erro": "Error processing JSON"}), 400
        
        product_name = data.get('product_name')
        amount = data.get('amount')
        if not product_name or not isinstance(amount, int):
            return jsonify({"erro": "Invalid data. Please provide the product name and quantity."}), 400
        
        connection = get_db_connection()
        if not connection:
            return jsonify({"erro": "Database connection failed"}), 500
        
        curso = connection.cursor()
        query = "INSERT INTO product (product_name, amount) VALUES (?, ?)"
        curso.execute(query, (product_name, amount))
        connection.commit()

        return jsonify({"mensagem": "Data saved successfully!"}), 201
    
    except Exception as e:
        return jsonify({"erro": f"Unexpected error: {e}"}), 500
    
    finally:
        if "curso" in locals() and curso:
            curso.close()
        if "connection" in locals() and connection:
            connection.close()