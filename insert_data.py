import sqlite3

def insert_data():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    movies = [
    ("The Shawshank Redemption", "Drama", "142", "Tim Robbins, Morgan Freeman", "Frank Darabont", "Inspiring", "https://example.com/shawshank.jpg", "https://letterboxd.com/film/the-shawshank-redemption/"),
    ("The Godfather", "Crime, Drama", "175", "Marlon Brando, Al Pacino", "Francis Ford Coppola", "Epic", "https://example.com/godfather.jpg", "https://letterboxd.com/film/the-godfather/"),
    ("The Dark Knight", "Action, Crime, Drama", "152", "Christian Bale, Heath Ledger", "Christopher Nolan", "Thrilling", "https://example.com/dark_knight.jpg", "https://letterboxd.com/film/the-dark-knight/"),
    ("Pulp Fiction", "Crime, Drama", "154", "John Travolta, Uma Thurman", "Quentin Tarantino", "Cool", "https://example.com/pulp_fiction.jpg", "https://letterboxd.com/film/pulp-fiction/"),
    ("Schindler's List", "Biography, Drama, History", "195", "Liam Neeson, Ralph Fiennes", "Steven Spielberg", "Heart-Wrenching", "https://example.com/schindlers_list.jpg", "https://letterboxd.com/film/schindlers-list/"),
    ("Forrest Gump", "Drama, Romance", "142", "Tom Hanks, Robin Wright", "Robert Zemeckis", "Heartwarming", "https://example.com/forrest_gump.jpg", "https://letterboxd.com/film/forrest-gump/"),
    ("Inception", "Action, Adventure, Sci-Fi", "148", "Leonardo DiCaprio, Joseph Gordon-Levitt", "Christopher Nolan", "Mind-Bending", "https://example.com/inception.jpg", "https://letterboxd.com/film/inception/"),
    ("Fight Club", "Drama", "139", "Brad Pitt, Edward Norton", "David Fincher", "Dark", "https://example.com/fight_club.jpg", "https://letterboxd.com/film/fight-club/"),
    ("The Matrix", "Action, Sci-Fi", "136", "Keanu Reeves, Laurence Fishburne", "The Wachowskis", "Revolutionary", "https://example.com/matrix.jpg", "https://letterboxd.com/film/the-matrix/"),
    ("Goodfellas", "Biography, Crime, Drama", "146", "Robert De Niro, Ray Liotta", "Martin Scorsese", "Gritty", "https://example.com/goodfellas.jpg", "https://letterboxd.com/film/goodfellas/"),
    ("The Silence of the Lambs", "Crime, Drama, Thriller", "118", "Jodie Foster, Anthony Hopkins", "Jonathan Demme", "Chilling", "https://example.com/silence_of_lambs.jpg", "https://letterboxd.com/film/the-silence-of-the-lambs/"),
    ("Se7en", "Crime, Drama, Mystery", "127", "Brad Pitt, Morgan Freeman", "David Fincher", "Dark", "https://example.com/se7en.jpg", "https://letterboxd.com/film/se7en/"),
    ("Interstellar", "Adventure, Drama, Sci-Fi", "169", "Matthew McConaughey, Anne Hathaway", "Christopher Nolan", "Epic", "https://example.com/interstellar.jpg", "https://letterboxd.com/film/interstellar/"),
    ("Gladiator", "Action, Adventure, Drama", "155", "Russell Crowe, Joaquin Phoenix", "Ridley Scott", "Epic", "https://example.com/gladiator.jpg", "https://letterboxd.com/film/gladiator/"),
    ("The Lion King", "Animation, Adventure, Drama", "88", "Matthew Broderick, Jeremy Irons", "Roger Allers, Rob Minkoff", "Heartwarming", "https://example.com/lion_king.jpg", "https://letterboxd.com/film/the-lion-king/"),
    ("Saving Private Ryan", "Drama, War", "169", "Tom Hanks, Matt Damon", "Steven Spielberg", "Intense", "https://example.com/saving_private_ryan.jpg", "https://letterboxd.com/film/saving-private-ryan/"),
    ("The Green Mile", "Crime, Drama, Fantasy", "189", "Tom Hanks, Michael Clarke Duncan", "Frank Darabont", "Heart-Wrenching", "https://example.com/green_mile.jpg", "https://letterboxd.com/film/the-green-mile/"),
    ("Star Wars: Episode V - The Empire Strikes Back", "Action, Adventure, Fantasy", "124", "Mark Hamill, Harrison Ford", "Irvin Kershner", "Epic", "https://example.com/empire_strikes_back.jpg", "https://letterboxd.com/film/star-wars-episode-v-the-empire-strikes-back/"),
    ("Parasite", "Comedy, Drama, Thriller", "132", "Kang-ho Song, Sun-kyun Lee", "Bong Joon Ho", "Satirical", "https://example.com/parasite.jpg", "https://letterboxd.com/film/parasite-2019/"),
    ("Whiplash", "Drama, Music", "106", "Miles Teller, J.K. Simmons", "Damien Chazelle", "Intense", "https://example.com/whiplash.jpg", "https://letterboxd.com/film/whiplash-2014/"),
    ("The Prestige", "Drama, Mystery, Sci-Fi", "130", "Christian Bale, Hugh Jackman", "Christopher Nolan", "Mind-Bending", "https://example.com/prestige.jpg", "https://letterboxd.com/film/the-prestige/"),
    ("The Departed", "Crime, Drama, Thriller", "151", "Leonardo DiCaprio, Matt Damon", "Martin Scorsese", "Gritty", "https://example.com/departed.jpg", "https://letterboxd.com/film/the-departed/"),
    ("The Usual Suspects", "Crime, Drama, Mystery", "106", "Kevin Spacey, Gabriel Byrne", "Bryan Singer", "Twisty", "https://example.com/usual_suspects.jpg", "https://letterboxd.com/film/the-usual-suspects/"),
    ("The Pianist", "Biography, Drama, Music", "150", "Adrien Brody, Thomas Kretschmann", "Roman Polanski", "Heart-Wrenching", "https://example.com/pianist.jpg", "https://letterboxd.com/film/the-pianist/"),
    ("Memento", "Mystery, Thriller", "113", "Guy Pearce, Carrie-Anne Moss", "Christopher Nolan", "Mind-Bending", "https://example.com/memento.jpg", "https://letterboxd.com/film/memento/"),
    ("Joker", "Crime, Drama, Thriller", "122", "Joaquin Phoenix, Robert De Niro", "Todd Phillips", "Dark", "https://example.com/joker.jpg", "https://letterboxd.com/film/joker-2019/"),
    ("Braveheart", "Biography, Drama, History", "178", "Mel Gibson, Sophie Marceau", "Mel Gibson", "Epic", "https://example.com/braveheart.jpg", "https://letterboxd.com/film/braveheart/"),
    ("The Social Network", "Biography, Drama", "120", "Jesse Eisenberg, Andrew Garfield", "David Fincher", "Intriguing", "https://example.com/social_network.jpg", "https://letterboxd.com/film/the-social-network/"),
    ("The Shining", "Drama, Horror", "146", "Jack Nicholson, Shelley Duvall", "Stanley Kubrick", "Terrifying", "https://example.com/shining.jpg", "https://letterboxd.com/film/the-shining/"),
    ("Spirited Away", "Animation, Adventure, Family", "125", "Rumi Hiiragi, Miyu Irino", "Hayao Miyazaki", "Magical", "https://example.com/spirited_away.jpg", "https://letterboxd.com/film/spirited-away/"),
    ("The Wolf of Wall Street", "Biography, Crime, Drama", "180", "Leonardo DiCaprio, Jonah Hill", "Martin Scorsese", "Excessive", "https://example.com/wolf_of_wall_street.jpg", "https://letterboxd.com/film/the-wolf-of-wall-street/"),
    ("Alien", "Horror, Sci-Fi", "117", "Sigourney Weaver, Tom Skerritt", "Ridley Scott", "Terrifying", "https://example.com/alien.jpg", "https://letterboxd.com/film/alien/"),
    ("Apocalypse Now", "Drama, War", "153", "Martin Sheen, Marlon Brando", "Francis Ford Coppola", "Intense", "https://example.com/apocalypse_now.jpg", "https://letterboxd.com/film/apocalypse-now/"),
    ("Blade Runner 2049", "Action, Drama, Mystery", "164", "Ryan Gosling, Harrison Ford", "Denis Villeneuve", "Thought-Provoking", "https://example.com/blade_runner_2049.jpg", "https://letterboxd.com/film/blade-runner-2049/"),
    ("The Grand Budapest Hotel", "Adventure, Comedy, Crime", "99", "Ralph Fiennes, F. Murray Abraham", "Wes Anderson", "Whimsical", "https://example.com/grand_budapest_hotel.jpg", "https://letterboxd.com/film/the-grand-budapest-hotel/"),
    ("La La Land", "Comedy, Drama, Music", "128", "Ryan Gosling, Emma Stone", "Damien Chazelle", "Romantic", "https://example.com/la_la_land.jpg", "https://letterboxd.com/film/la-la-land/"),
    ("Moonlight", "Drama", "111", "Mahershala Ali, Naomie Harris", "Barry Jenkins", "Touching", "https://example.com/moonlight.jpg", "https://letterboxd.com/film/moonlight/"),
    ("Django Unchained", "Drama, Western", "165", "Jamie Foxx, Christoph Waltz", "Quentin Tarantino", "Revenge", "https://example.com/django_unchained.jpg", "https://letterboxd.com/film/django-unchained/"),
    ("The Truman Show", "Comedy, Drama", "103", "Jim Carrey, Ed Harris", "Peter Weir", "Thought-Provoking", "https://example.com/truman_show.jpg", "https://letterboxd.com/film/the-truman-show/"),
    ("Requiem for a Dream", "Drama", "102", "Ellen Burstyn, Jared Leto", "Darren Aronofsky", "Disturbing", "https://example.com/requiem_for_a_dream.jpg", "https://letterboxd.com/film/requiem-for-a-dream/"),
    ("Mad Max: Fury Road", "Action, Adventure, Sci-Fi", "120", "Tom Hardy, Charlize Theron", "George Miller", "Intense", "https://example.com/mad_max_fury_road.jpg", "https://letterboxd.com/film/mad-max-fury-road/"),
    ("WALL·E", "Animation, Adventure, Family", "98", "Ben Burtt, Elissa Knight", "Andrew Stanton", "Heartwarming", "https://example.com/wall_e.jpg", "https://letterboxd.com/film/wall-e/"),
    ("No Country for Old Men", "Crime, Drama, Thriller", "122", "Tommy Lee Jones, Javier Bardem", "Joel Coen, Ethan Coen", "Intense", "https://example.com/no_country.jpg", "https://letterboxd.com/film/no-country-for-old-men/"),
    ("A Beautiful Mind", "Biography, Drama", "135", "Russell Crowe, Ed Harris", "Ron Howard", "Inspirational", "https://example.com/beautiful_mind.jpg", "https://letterboxd.com/film/a-beautiful-mind/"),
    ("The Big Lebowski", "Comedy, Crime", "117", "Jeff Bridges, John Goodman", "Joel Coen, Ethan Coen", "Cult", "https://example.com/big_lebowski.jpg", "https://letterboxd.com/film/the-big-lebowski/"),
    ("The Lord of the Rings: The Fellowship of the Ring", "Action, Adventure, Drama", "178", "Elijah Wood, Ian McKellen", "Peter Jackson", "Epic", "https://example.com/lotr_fellowship.jpg", "https://letterboxd.com/film/the-lord-of-the-rings-the-fellowship-of-the-ring/"),
    ("Her", "Drama, Romance, Sci-Fi", "126", "Joaquin Phoenix, Amy Adams", "Spike Jonze", "Thought-Provoking", "https://example.com/her.jpg", "https://letterboxd.com/film/her/"),
    ("The Hateful Eight", "Crime, Drama, Mystery", "168", "Samuel L. Jackson, Kurt Russell", "Quentin Tarantino", "Tense", "https://example.com/hateful_eight.jpg", "https://letterboxd.com/film/the-hateful-eight/"),
    ("Gone Girl", "Drama, Mystery, Thriller", "149", "Ben Affleck, Rosamund Pike", "David Fincher", "Twisty", "https://example.com/gone_girl.jpg", "https://letterboxd.com/film/gone-girl/"),
    ("Inglourious Basterds", "Adventure, Drama, War", "153", "Brad Pitt, Diane Kruger", "Quentin Tarantino", "Revenge", "https://example.com/inglourious_basterds.jpg", "https://letterboxd.com/film/inglourious-basterds/")
    ]

    movie_ratings = [
        ("The Godfather", 4.8),
        ("The Dark Knight", 4.7),
        ("Pulp Fiction", 4.6),
        ("Fight Club", 4.5),
        ("Forrest Gump", 4.4),
        ("Inception", 4.5),
        ("The Matrix", 4.6),
        ("Goodfellas", 4.6),
        ("Se7en", 4.5),
        ("The Silence of the Lambs", 4.4),
        ("Interstellar", 4.6),
        ("The Green Mile", 4.5),
        ("Schindler's List", 4.9),
        ("The Shawshank Redemption", 4.9),
        ("Saving Private Ryan", 4.6),
        ("Gladiator", 4.4),
        ("Braveheart", 4.3),
        ("The Prestige", 4.5),
        ("Memento", 4.4),
        ("The Departed", 4.5),
        ("The Pianist", 4.5),
        ("Black Swan", 4.3),
        ("The Wolf of Wall Street", 4.4),
        ("Mad Max: Fury Road", 4.3),
        ("Joker", 4.4),
        ("Parasite", 4.6),
        ("12 Years a Slave", 4.4),
        ("Django Unchained", 4.5),
        ("The Revenant", 4.4),
        ("A Beautiful Mind", 4.4),
        ("The Social Network", 4.3),
        ("Whiplash", 4.6),
        ("La La Land", 4.5),
        ("Moonlight", 4.3),
        ("Blade Runner 2049", 4.5),
        ("Her", 4.4),
        ("Birdman", 4.3),
        ("The Grand Budapest Hotel", 4.3),
        ("The Lighthouse", 4.2),
        ("Manchester by the Sea", 4.3),
        ("Lady Bird", 4.2),
        ("The Shape of Water", 4.2),
        ("Jojo Rabbit", 4.3),
        ("Once Upon a Time in Hollywood", 4.4),
        ("1917", 4.4),
        ("Arrival", 4.3),
        ("The Irishman", 4.3),
        ("The Hateful Eight", 4.2),
        ("The Big Short", 4.4),
        ("Drive", 4.3)
    ]

    for title, rating in movie_ratings:
        cursor.execute('UPDATE movies SET rating = ? WHERE title = ?', (rating, title))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()
    print("Data inserted successfully.")
