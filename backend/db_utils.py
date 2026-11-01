import sqlite3
from pathlib import Path

from config import DB_PATH

def get_db_connection():
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(DB_PATH)
        schema_path = Path(__file__).resolve().parent.parent / "database" / "init.sql"
        connection.executescript(schema_path.read_text(encoding="utf-8"))
        return connection
    except sqlite3.Error as e:
        print(f"Erro ao tentar conectar ao banco de dados, ERRO: {e}")
        return None