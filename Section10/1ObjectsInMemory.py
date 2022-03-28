print(object)
print(isinstance([1, 2, 3, 4, 5], object))
print(isinstance((1, 2, 3, 4, 5), object))
print(isinstance("Hellow Rony", object))
print(isinstance({"a": 5, "b": 6}, object))
print(isinstance(True, object))


def f(x):
    return x * 2


print(isinstance(f, object))


class Movie:
    def __init__(self, title):
        self.title = title


print(isinstance(Movie, object))
