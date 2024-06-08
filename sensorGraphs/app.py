from flask import Flask

from sensorGraphs.dht_read import dht_read_temperature

app = Flask(__name__)


@app.get('/sensor')
def get_temperature():
    return dht_read_temperature()


if __name__ == '__main__':
    app.run()
