import mysql.connector
from db_connect import get_db_connection

def db_read_data(table, column):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(f"SELECT {column} FROM {table} ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        
        if result:
            return result[0]
        return None
        
    except mysql.connector.Error as e:
        print(f"Error reading from database: {e}")
        return None
        
    finally:
        cursor.close()
        conn.close() 