class Movie:
    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title


my_move = Movie("Debdas", 9.8)
print("My best Movie is:",my_move.get_title(),"and rating is: ",my_move.rating)
