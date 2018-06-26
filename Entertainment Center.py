import media
import fresh_tomatoes

ex_machina = media.Movie_id(264660)
her = media.Movie_id(152601)
the_imitation_game = media.Movie_id(205596)
# the_social_network = media.Movie_id(37799)
# steve_jobs = media.Movie_id(321697)
movies_list = [the_imitation_game, her, ex_machina]

for i in range(9):
   movies_list.append(media.Movie(i))

fresh_tomatoes.open_movies_page(movies_list)

