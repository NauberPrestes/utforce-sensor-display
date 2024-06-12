import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

db_connection_str = "mysql://nauber:135086Elgom.%2C@localhost/sensor"
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT id, temperature FROM dht_sensor', con=db_connection)
time = df['id']
temperature = df['temperature']

plt.plot(time, temperature)
plt.show()
