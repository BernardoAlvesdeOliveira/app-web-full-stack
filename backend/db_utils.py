from mariadb import mariadb, Error
from config import DB_CONFIG

def get_db_connection():
    try:
        connection = mariadb.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Erro ao tentar conectar ao banco de dados, ERRO: {e}")
        return None