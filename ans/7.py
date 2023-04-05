# 7.
from movies import *
import random

class RandomMovie(Movie,Cinema):
    
    
    def __init__(self):
        super().__init__()

    def RandomCinema(self):
        cinema = Cinema()
        movie = input()
        ranNum = random.randrange(1,len(cinema.cinema_list))
        print(movie,cinema.cinema_list[ranNum])

rand = RandomMovie()
rand.RandomCinema()

