class Movie:
    id_counter = 1

    def __init__(self, title, rating):
        self.id = Movie.id_counter
        self.title = title
        self.rating = rating
        Movie.id_counter += 1


my_move = Movie("Debdas", 9)
your_move = Movie("idots", 9.3)
print(my_move.id)
print(your_move.id)
