import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "A story of his boy and toys that come to life",
                        "http://images.m-magazine.com/uploads/posts/image/46533/toy-story-hotel.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
avatar.show_trailer()

starWars = media.Movie("Star Wars",
                       "Rebels fight the Galactic Empire",
                       "https://images.sobadsogood.com/rare-vintage-star-wars-movie-posters-youve-never-seen/1.jpg",
                       "https://www.youtube.com/watch?v=9gvqpFbRKtQ")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://youtube.com/watch?v=3PsUJFEBC74")

ratatoulle = media.Movie("Ratatoulle",
                          "A rat is a chef in Paris",
                          "http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://www.hungergamesdwtc.net/wp-content/uploads/2014/02/The-Hunger-Games-Poster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, school_of_rock, ratatoulle, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
