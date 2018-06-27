import media
import fresh_tomatoes

movie_display = 9

ex_machina = media.MovieID(264660)
her = media.MovieID(152601)
the_imitation_game = media.MovieID(205596)
# the_social_network = media.Movie_id(37799)
# steve_jobs = media.Movie_id(321697)
movies_list = [the_imitation_game, her, ex_machina]

# Create movie objects equal to movie_display and add to list
for i in range(movie_display):
    movies_list.append(media.Movie(i))

fresh_tomatoes.open_movies_page(movies_list)

