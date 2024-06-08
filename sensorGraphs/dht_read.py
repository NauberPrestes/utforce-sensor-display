from sensorGraphs.db_connect import cursor


def dht_read_temperature():
    sql = "SELECT temperature FROM dht_sensor ORDER BY id DESC LIMIT 1"
    cursor.execute(sql)
    temperature = cursor.fetchall()
    return temperature
