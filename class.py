class Movie:
    # self is like this in Javascript
    def __init__(self, title, year, imdb_score, have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

    def print_movie(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)


film_1 = Movie("Life of Brian", 1979, 8.1, True)
film_2 = Movie("The Holy Grail", 1975, 8.2, True)

# film_1.print_movie()
# Same as
# Movie.print_movie(film_1)

# films = [film_1, film_2]
# print(films[1].title, films[0].title)
# films[0].print_movie()

# Classes are blueprints
# Objects are the actual things you built
# variables => attributes
# functions => methods


class Person:
    def move(self):
        print("Move 4 paces")

    def rest(self):
        print("Gains 4 health points")


class Doctor(Person):  # Inherits from Person
    # pass  # Doctor class will be identical to Person when we write the pass keyword
    def heal(self):
        print("Heals 10 health points")


class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")

    def move(self):  # it can override the original inherited function
        print("Moves 6 paces")


class Wizzard(Doctor, Fighter):
    def cast_spell(self):
        print("Turns invisble")

    def heal(self):
        print("Heals 15 health points")


character = Wizzard()
character.move()  # from Person
character.heal()  # from Wizzard, overriden Doctor
character.fight()  # from Fighter
