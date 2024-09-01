from flask import Flask, render_template, request, redirect, url_for, g
from models import db, Movie, User
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

def get_db_connection():
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        preferences = request.form['preferences']
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Username already exists!"

        new_user = User(username=username, preferences=preferences)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('search', username=username))
    
    return render_template('register.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    username = request.form['username']
    user = User.query.filter_by(username=username).first()
    if not user:
        return "User not found!"

    return redirect(url_for('search', username=username))

@app.route('/search_results')
def search_results():
    genre = request.args.get('genre')
    length = request.args.get('length')
    actors = request.args.get('actors')
    director = request.args.get('director')
    rating = request.args.get('rating')

    movies = get_movies(genre=genre, length=length, actors=actors, director=director, rating=rating)

    return render_template('search_results.html', movies=movies)



def get_movies(genre=None, length=None, actors=None, director=None, rating=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM movies WHERE 1=1"
    params = []

    if genre:
        query += " AND genre LIKE ?"
        params.append(f"%{genre}%")
    if length:
        query += " AND length LIKE ?"
        params.append(f"%{length}%")
    if actors:
        query += " AND actors LIKE ?"
        params.append(f"%{actors}%")
    if director:
        query += " AND director LIKE ?"
        params.append(f"%{director}%")
    if rating:
        query += " AND rating LIKE ?"
        params.append(f"%{rating}%")

    cursor.execute(query, params)
    movies = cursor.fetchall()
    conn.close()
    
    return movies


@app.route('/search', methods=['GET'])
def search():
    genre = request.args.get('genre', '')
    length = request.args.get('length', '')
    director = request.args.get('director', '')
    actors = request.args.get('actors', '')
    rating = request.args.get('rating', '')

    query = "SELECT * FROM movies WHERE 1=1"
    params = []

    if genre:
        query += " AND genre LIKE ?"
        params.append(f"%{genre}%")
    
    if length:
        if '-' in length:
            min_len, max_len = length.split('-')
            query += " AND length BETWEEN ? AND ?"
            params.append(min_len)
            params.append(max_len)
        else:
            query += " AND length = ?"
            params.append(length)
    
    if director:
        query += " AND director LIKE ?"
        params.append(f"%{director}%")
    
    if actors:
        query += " AND actors LIKE ?"
        params.append(f"%{actors}%")

    if rating:
        query += " AND rating LIKE ?"
        params.append(f"%{rating}%")

    cursor = get_db_connection().cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()

    return render_template('search.html', 
                           results=results, 
                           genre=genre, 
                           length=length, 
                           director=director, 
                           actors=actors,
                           rating=rating)




@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    field = request.args.get('field')
    query = request.args.get('query')

    if field not in ['genre', 'length', 'director', 'actors', 'rating']:
        return jsonify({'suggestions': []})

    cursor = get_db_connection().cursor()
    cursor.execute(f"SELECT DISTINCT {field} FROM movies WHERE {field} LIKE ?", (f"%{query}%",))
    suggestions = [row[field] for row in cursor.fetchall()]

    return jsonify({'suggestions': suggestions})


@app.route('/search_suggestions')
def search_suggestions():
    type = request.args.get('type')
    query = request.args.get('query', '').lower()

    if type == 'genre':
        items = [m.genre for m in Movie.query.distinct(Movie.genre) if query in m.genre.lower()]
    elif type == 'length':
        items = [f"{m.length}" for m in Movie.query.distinct(Movie.length) if query in str(m.length)]
    elif type == 'actors':
        items = [actors for actors in set(a.strip() for m in Movie.query.all() for a in m.actors.split(',') if query in a.strip().lower())]
    elif type == 'director':
        items = [m.director for m in Movie.query.distinct(Movie.director) if query in m.director.lower()]
    elif type == 'rating':
        items = [m.rating for m in Movie.query.distinct(Movie.rating) if query in m.rating.lower()]

    return jsonify(items)
    


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
