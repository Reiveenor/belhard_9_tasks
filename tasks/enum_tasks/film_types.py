"""
Написать класс FilmTypes, который будет наследоваться от Enum и содержать
константы-названия жанров фильмов.
"""
from enum import Enum


class FilmTypes(Enum):
    COMEDY = 1
    DRAMA = 2
    FANTASY = 3
    COMICS = 4
    HORROR = 5
    MYSTERY = 6
    THRILLER = 7
    WESTERN = 8
    SITCOM = 9
