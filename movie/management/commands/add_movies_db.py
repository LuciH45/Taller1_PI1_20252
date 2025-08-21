from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movie_descriptions.json into the Movie model'

    def handle(self, *args, **kwargs):
        # Construye la ruta completa al archivo JSON
        # Recuerden que la consola está ubicada en la carpeta DjangoProjectBase.
        # El path del archivo movie_descriptions con respecto a DjangoProjectBase sería la carpeta anterior
        json_file_path = "movie/management/commands/movies.json"

        # Cargar datos desde el JSON
        with open(json_file_path, 'r') as file:
            movies = json.load(file)

        # Insertar películas en la base de datos
        for i in range(100):
            movie = movies[i]
            exist = Movie.objects.filter(title=movie['title']).first()  # Se asegura de no duplicar
            if not exist:
                Movie.objects.create(
                    title=movie['title'],
                    image='movie/images/default.jpg',
                    genre=movie['genre'],
                    year=movie['year'],
                    description=movie['plot']
                )
