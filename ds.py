# Project "Movie Trailer Website"
# the purpose of this project is to present a list of favorite movie trailers
# This is a server-side code that contains the Movie class
#

"""

 ds.py

    This script contains the Movie class
    accepted parameters (all parameters are mandatory)
    - movie_title: a string that represents a movie title
    - poster_image: a sting that contains a URL address to the poster image
    - trailer_youtube: a sting that contains a URL address to the trailer

    Please note that the script will not validate the URL links; broken links
    will be incorrectly displayed in the imbedded player

 created:         2017-08-14
 author:          Oleg Ustyuzhin oleg,ustyuzhin@dhl.com

 Assumptions:

 - this module is used by other scripts for new Movie class instances creation

"""
import webbrowser
__version__ = '0.0.1'
__author__ = 'oleg ustyuzhin'


class Movie():

    """ __init__ function will initialize a new instance of this class

    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title  # get the movie title
        self.poster_image_url = poster_image  # get the poster image
        self.trailer_youtube_url = trailer_youtube  # get the YouTube URL link

    """ show_trailer function will invoke a default browser and play the URL
        given as the parameter 'trailer_youtube_url'

    """
    # this function will invoke the default web browser and pass
    # the YouTube URL link as a parameter

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
