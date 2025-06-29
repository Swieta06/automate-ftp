import pyodbc
import pandas as pd
from config import DB_CONFIG


def get_db_connection():
    conn_str = (
        f"DRIVER={DB_CONFIG['driver']};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['username']};"
        f"PWD={DB_CONFIG['password']}"
    )
    return pyodbc.connect(conn_str)


def check_duplicate(cursor, id_value):
    cursor.execute("SELECT COUNT(*) FROM users WHERE id = ?", id_value)
    count = cursor.fetchone()[0]
    return count > 0


def insert_to_db(df: pd.DataFrame):
    conn = get_db_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        if not check_duplicate(cursor, row['id']):
            cursor.execute("""
                INSERT INTO users (id, nama, norek, cif, deskripsi)
                VALUES (?, ?, ?, ?, ?)
            """, row['id'], row['nama'], row['norek'], row['cif'], row['deskripsi'])
    conn.commit()
    conn.close()
