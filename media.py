import tmdbsimple as tmdb
tmdb.API_KEY = 'c8385eb8708b5c75026cee112688f1a9'
image_base_url = 'https://image.tmdb.org/t/p/w500/'
youtube_base_url = 'https://www.youtube.com/watch?v='


class MovieID:
    def __init__(self, movie_id):
        # Access the Movie Database and return info about movie_id
        movie = tmdb.Movies(movie_id)
        movie.info()
        self.title = movie.title + "\n" + str(int(movie.vote_average * 10)) \
                     + "%"
        self.storyline = movie.overview
        movie.videos()
        self.poster_image_url = image_base_url + movie.poster_path
        key = movie.results[0]['key']
        self.trailer_youtube_url = youtube_base_url + key


class Movie:
    def __init__(self, index):
        # Acess the Movie Database and retrieve movie_id of a current movie base on index
        movie = tmdb.Movies()
        movie.now_playing()
        movie_id = movie.results[index]['id']
        # Return information
        movie = tmdb.Movies(movie_id)
        movie.info()
        self.title = movie.title + "\n" + str(int(movie.vote_average * 10)) \
                     + "%"
        self.storyline = movie.overview
        movie.videos()
        self.poster_image_url = image_base_url + movie.poster_path
        key = movie.results[0]['key']
        self.trailer_youtube_url = youtube_base_url + key
