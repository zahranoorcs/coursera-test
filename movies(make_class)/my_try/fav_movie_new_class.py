import webbrowser
class Movie():
    def __init__(self,title,storyline,poster_url,trailer_url):
        self.movie_title=title
        self.movie_storyline=storyline
        self.movie_poster=poster_url
        self.trailer=trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer)
