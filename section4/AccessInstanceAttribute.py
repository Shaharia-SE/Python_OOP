class Movie:
    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating


my_favorite_movie = Movie("Debdas", 2002, "Hindi", 9.9)
your_favorit_movie = Movie("Titanic", 1997, "English", 4.6)
print("My favorit Movie:")
print(my_favorite_movie.title)
print(my_favorite_movie.year)
print(my_favorite_movie.language)
print(my_favorite_movie.rating)

print("Your favorit Movie:")

print(your_favorit_movie.title)
print(your_favorit_movie.year)
print(your_favorit_movie.language)
print(your_favorit_movie.rating)
