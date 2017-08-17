# Project "Movie Trailer Website"
# the purpose of this project is to present a list of favorite movie trailers
# This is a server-side code that imports required modules and contains
# execution code
#
import fresh_tomatoes  # third party module that provides broser functionality
import ds  # this module provides class Movie structure for storing data
# The below ds class instances form the content of the page;
# usage:
# <class_instance_name> = ds.Movie(
#    "<Movie Title>",
#    "<Poster Image>",
#    "<YouTube URL address link>"
# )
mv_Dogma = ds.Movie(
    "Dogma",
    "https://upload.wikimedia.org/wikipedia/en/1/1e/Dogma_%28movie%29.jpg",
    "https://www.youtube.com/watch?v=WL4VJmpwuP8"
)
mv_FifthElement = ds.Movie(
    "The Fifth Element",
    "https://upload.wikimedia.org/wikipedia/commons/d/df/" +
    "Stone_of_the_Fifth_Element.jpg",
    "https://www.youtube.com/watch?v=fQ9RqgcR24g"
)
mv_Godfather = ds.Movie(
    "The Godfather",
    "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
    "https://www.youtube.com/watch?v=i96VS_z8y7g"
)
mv_BackupPlan = ds.Movie(
    "The Back-up Plan",
    "https://upload.wikimedia.org/wikipedia/en/d/d8/Newbupp.jpg",
    "https://www.youtube.com/watch?v=cut4IW0oz1w"
)
mv_BlessTheChild = ds.Movie(
    "Bless the Child",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Bless_the_Child_film.jpg",
    "https://www.youtube.com/watch?v=PbO-OMzEJSM"
)
mv_Oceans12 = ds.Movie(
    "Ocean's Twelve",
    "https://upload.wikimedia.org/wikipedia/en/8/83/Ocean%27s12Poster1.gif",
    "https://www.youtube.com/watch?v=w_o3xenrUGs"
)

movies = [  # prepare a list of trailers
    mv_Dogma,
    mv_FifthElement,
    mv_Godfather,
    mv_BackupPlan,
    mv_BlessTheChild,
    mv_Oceans12
]
# getting html code using the 3rd party module
fresh_tomatoes.open_movies_page(movies)

# print related documentation out in the console
print("General information for class " + ds.__name__ + ds.__doc__)
