from sensorGraphs.db_connect import cursor


def dht_read_data():
    sql = "SELECT temperature, humidity FROM dht_sensor ORDER BY insertion_date DESC LIMIT 1"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data
