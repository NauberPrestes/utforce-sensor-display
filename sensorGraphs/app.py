from flask import Flask, request, Response

from sensorGraphs.dht_read import dht_read_data
from sensorGraphs.dht_write import dht_write_data
from sensorGraphs.db_write import db_write_data

app = Flask(__name__)


@app.post('/sensor/dht')
def dht_post_data():
    data = request.get_json()
    dht_write_data(data['temperature_dht'], data['humidity'])
    return Response(status=201)


@app.post('/sensor/angle')
def angle_post_data():
    data = request.get_json()
    table = 'angle_sensor'
    column = 'angle'
    value = data['angle']
    db_write_data(table, column, value)
    return Response(status=201)


@app.post('/sensor/max')
def max_post_data():
    data = request.get_json()
    table = 'max_sensor'
    column = 'temperature'
    value = data['temperature_max']
    db_write_data(table, column, value)
    return Response(status=201)


@app.get('/sensor/dht')
def get_temperature():
    return dht_read_data()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
