import mysql.connector

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="nauber",
            password="135086Elgom.,",
            database="sensor"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        raise

db = mysql.connector.connect(
      host="localhost",
      user="nauber",
      password="135086Elgom.,",
      database= "sensor"
)

cursor = db.cursor()

