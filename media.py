import webbrowser

class Movie():
    ''' Movie class instances represent movies with some relevant informations
    about it
    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating):
        ''' Method that initializes movies objects
        movie_title (str): Movie title
        movie_storyline (str): Brief movie storyline
        poster_image (str): url with the movie poster (from wikipedia)
        trailer_youtube (str): url with the movie trailer (from youtube)
        rating (int): movie star rating (defined by the developer's taste)
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating

    def show_trailer(self):
        ''' Method to open movie trailers from url
        '''
        webbrowser.open(self.trailer_youtube_url)
