import pandas as pd
from models import Movie

def get_recommendations(preferences):
    movies = Movie.query.all()
    df = pd.DataFrame([(m.title, m.genre, m.actors, m.length, m.rating) for m in movies], 
                      columns=['title', 'genre', 'actors', 'length', 'rating'])

    filtered_movies = df[df['genre'].isin(preferences.split(','))]
    return filtered_movies.to_dict(orient='records')
