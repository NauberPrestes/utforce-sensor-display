from flask import Flask, request, Response, jsonify
import time

from dht_read import dht_read_data
from dht_write import dht_write_data
from db_write import db_write_data
from db_read import db_read_data

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


@app.get('/sensor/all')
def get_all_sensor_data():
    try:
        dht_temperature_data = db_read_data('dht_sensor', 'temperature')
        dht_humidity_data = db_read_data('dht_sensor', 'humidity')
        
        angle_data = db_read_data('angle_sensor', 'angle')
        
        max_data = db_read_data('max_sensor', 'temperature')
        
        sensor_data = {
            "DHT - Temperatura": float(dht_temperature_data) if dht_temperature_data is not None else 0,
            "DHT - Umidade": float(dht_humidity_data) if dht_humidity_data is not None else 0,
            "MAX - Temperatura": float(max_data) if max_data is not None else 0,
            "Volante - Ângulo": float(angle_data) if angle_data is not None else 0
        }
        
        return jsonify(sensor_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
