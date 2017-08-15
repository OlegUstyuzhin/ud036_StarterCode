# Project "Movie Trailer Website"
# the purpose of this project is to present a list of favorite movie trailers 
# This is a server-side code that imports required modules and contains
# execution code  
# import fresh_tomatoes  
# third party module that provides browser functionality import ds  
# this module provides class Movie structure for storing data
# The below ds class instances form the content of the page;
# usage:
# <class_instance_name> = ds.Movie(
#	"<Movie Title>",
#	"<Poster Image>",
#	"<YouTube URL address link>"
#)

mv01 = ds.Movie(
	"Dogma",
	"https://upload.wikimedia.org/wikipedia/en/1/1e/Dogma_%28movie%29.jpg",
	"https://www.youtube.com/watch?v=WL4VJmpwuP8"
)

mv02 = ds.Movie(
	"The Fifth Element",
	"https://upload.wikimedia.org/wikipedia/commons/d/df/Stone_of_the_Fifth_Element.jpg",
	"https://www.youtube.com/watch?v=fQ9RqgcR24g"
)

mv03 = ds.Movie(
	"The Godfather",
	"https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
	"https://www.youtube.com/watch?v=i96VS_z8y7g"
)

mv04 = ds.Movie(
	"The Back-up Plan",
	"https://upload.wikimedia.org/wikipedia/en/d/d8/Newbupp.jpg",
	"https://www.youtube.com/watch?v=cut4IW0oz1w"
)

mv05 = ds.Movie(
	"Bless the Child",
	"https://upload.wikimedia.org/wikipedia/en/7/70/Bless_the_Child_film.jpg",
	"https://www.youtube.com/watch?v=PbO-OMzEJSM"
)

mv06 = ds.Movie(
	"Ocean's Twelve",
	"https://upload.wikimedia.org/wikipedia/en/8/83/Ocean%27s12Poster1.gif",
	"https://www.youtube.com/watch?v=w_o3xenrUGs"
)

movies = [mv01,mv02,mv03,mv04,mv05,mv06]  # prepare a list of trailers
fresh_tomatoes.open_movies_page(movies)  # call the 3rd party module to generate an html file

# print related documentation out in the console
print("General information for class " + ds.__name__ + ds.__doc__)
#print(ds.Movie.__doc__)
#print(ds.Movie.__name__)
#print(ds.Movie.__module__)
#print(ds.__version__)
#print(ds.__author__)
