# Project "Movie Trailer Website" *** ***
# the pupose os this project is to present a list of favorite movie trailers 
# This is a server-side code that imports required modules and contains
# execution code  
# 
import fresh_tomatoes  # third party module that provides broser functionality
import ds  # this module provides class Movie structure for storing data
Penguins_Antarctic = ds.Movie(
    "Penguins Antarctic Documentary",
    "https://upload.wikids.org/wikipedia/en/7/7d/The_Penguins_of_Madagascar_-_Dr._Blowhole_Returns_-_Again%21_Coverart.png",
    "https://www.youtube.com/watch?v=1y_kfWUCFDQ"
    )
MINIONS = ds.Movie("A Bug's life",
                      "https://upload.wikimedia.org/wikipedia/en/4/4d/Minions.png","https://www.youtube.com/watch?v=7AFUch5JZaQ")
Finding_Nemo = ds.Movie("Finding Nemo- Shark Scene- Bruce",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg","https://www.youtube.com/watch?v=XWuPGKLJXe8")
Ice_Age_3 = ds.Movie("Ice Age 3",
                        "https://upload.wikimedia.org/wikipedia/en/2/24/Ice_Age_Dawn_of_the_Dinosaurs_theatrical_poster.jpg","https://www.youtube.com/watch?v=Vi2gDjA7CB0")
For_The_Birds = ds.Movie("For The Birds",
                          "https://upload.wikimedia.org/wikipedia/en/7/77/For_the_Birds_%28film%29_poster.jpg","https://www.youtube.com/watch?v=vZYAHGwS3mA")
movies = [Penguins_Antarctic,MINIONS,Finding_Nemo,Ice_Age_3,For_The_Birds]
fresh_tomatoes.open_movies_page(movies)
print(ds.Movie.__doc__)
print(ds.Movie.__name__)
print(ds.Movie.__module__)
print(ds.__version__)
print(ds.__author__)



