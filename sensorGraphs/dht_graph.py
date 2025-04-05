import matplotlib.pyplot as plt
import matplotlib.dates
import pandas as pd
from sqlalchemy import create_engine

db_connection_str = "mysql://nauber:135086Elgom.%2C@localhost/sensor"
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT id, humidity FROM dht_sensor LIMIT 12', con=db_connection)
time = df['id']
temperature = df['humidity']

plt.plot(time, temperature)

plt.title("DHT11 Data")
plt.xlabel("ID")
plt.ylabel("Humidity, %")

plt.gcf().autofmt_xdate()

plt.show()
