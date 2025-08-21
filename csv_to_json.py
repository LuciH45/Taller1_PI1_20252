import pandas as pd
import json

# Lee el archivo CSV
df = pd.read_csv('movies_initial.csv')

# Guarda el DataFrame como JSON
df.to_json('movies.json', orient='records')

# Lee el archivo JSON
with open('movies.json', 'r') as file:
    movies = json.load(file)

# Muestra los primeros 100 registros (aunque aquí se rompe en el primero por el break)
for i in range(100):
    movie = movies[i]
    print(movie)
    break
