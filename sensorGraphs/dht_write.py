from db_connect import cursor, db


def dht_write_data(tem, hum):
    sql = "INSERT INTO dht_sensor (temperature, humidity) VALUES (%s, %s)"
    val = (tem, hum)
    cursor.execute(sql, val)

    db.commit()
