import webbrowser

class Movie():
    '''
        Method that initializes movies objects
        movie_title (str): Movie title
        movie_storyline (str): Brief movie storyline
        poster_image (str): url with the movie poster (from wikipedia)
        trailer_youtube (str): url with the movie trailer (from youtube)
        rating (int): movie star rating (defined by the developer's taste)
    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
    '''
        Method to open movie trailers from url        
    '''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
