import media
import fresh_tomatoes

#Creating the movies instances
toy_story = media.Movie("Toy Story",
                        "Toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        5)

avatar = media.Movie("Avatar",
                     "Weird adult smurfs",
                     "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                     2)

django = media.Movie("Django Unchained",
                     "Tarantino's racist western",
                     "https://upload.wikimedia.org/wikipedia/pt/8/8b/Django_Unchained_Poster.jpg",
                     "https://www.youtube.com/watch?v=eUdM9vrCbow",
                     5)

titanic = media.Movie("Titanic",
                      "Big ships that sinks",
                      "https://upload.wikimedia.org/wikipedia/pt/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=PH11P_6OqVI",
                      4)

inside_out = media.Movie("Inside Out",
                         "How feelings have feelings",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY",
                         4)

little_rascals = media.Movie("Little Rascals",
                             "Cute kids driving karts",
                             "https://upload.wikimedia.org/wikipedia/pt/7/70/The_Little_Rascals.jpg",
                             "https://www.youtube.com/watch?v=MsV6r1nbSGk",
                             2)

#Adding movies instances to array to be presented on the web page
movies = (toy_story, avatar, django, titanic, inside_out, little_rascals)

#Open movies pages on fresh tomatoes front end module
fresh_tomatoes.open_movies_page(movies)


