from flask import Flask, request, Response

from sensorGraphs.dht_read import dht_read_data
from sensorGraphs.dht_write import dht_write_data

app = Flask(__name__)

print('Database connection is ok')


@app.post('/sensor')
def write_data():
    dados = request.get_json()
    dht_write_data(dados['temperature'], dados['humidity'])
    return Response(status=201)


@app.get('/sensor')
def get_temperature():
    return dht_read_data()


if __name__ == '__main__':
    app.run()
