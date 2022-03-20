class Movie:
    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        print("Calling the getter")
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        print("calling setter")
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 10:
            self._rating = new_rating
        else:
            print("Please enter valid rating")


my_movie = Movie("Debdas", 8.7)
print(my_movie.rating)
my_movie.rating = 4.5
print(my_movie.rating)
