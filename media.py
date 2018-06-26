import tmdbsimple as tmdb
tmdb.API_KEY = 'c8385eb8708b5c75026cee112688f1a9'
image_base_url = 'https://image.tmdb.org/t/p/w500/'
youtube_base_url = 'https://www.youtube.com/watch?v='

class Movie_id:
    def __init__(self, movie_id):
        movie = tmdb.Movies(movie_id)
        movie.info()
        self.title = str(movie.title) + "\n" + str(int(movie.vote_average * 10)) +"%"
        self.storyline = movie.overview
        movie.videos()
        self.poster_image_url = image_base_url + movie.poster_path
        self.trailer_youtube_url = youtube_base_url + movie.results[0]['key']

class Movie:
    def __init__(self, result_element):
        movie = tmdb.Movies()
        movie.now_playing()
        movie_id = movie.results[result_element]['id']
        # same code as above object
        movie = tmdb.Movies(movie_id)
        movie.info()
        self.title = str(movie.title) + "\n" + str(int(movie.vote_average * 10)) + "%"
        self.storyline = movie.overview
        self.poster_image_url = image_base_url + movie.poster_path
        movie.videos()
        key = movie.results[0]['key']
        self.trailer_youtube_url = youtube_base_url + key
