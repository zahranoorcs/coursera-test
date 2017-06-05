import fresh_tomatoes
import media
#self argument is ignored because it is by default by python
toy_story = media.Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar=media.Movie("Avatar",
                   "A marie on an alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock=media.Movie("School of Rock", "Using rock music to learn",
                "https://upload.wikimedia.org/wikipedia/en/3/3b/School_of_Rock_%28TV_series%29_poster.jpg",
                "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
ratatouille=media.Movie("Ratatouille","A rat is a chef in Paris",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris=media.Movie("Midnight in Paris","Going back in time to meet authors",
                              "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                              "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games=media.Movie("Hunger Games","A really real reality show",
                         "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                         "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies=[toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

