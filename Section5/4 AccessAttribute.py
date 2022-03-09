
# outside the classs access attribute

class MyEditorialBook:
    has_cover = True
    editorial_code = 39012

    def __init__(self, title, num_pages, published):
        self.title = title
        self.num_pages = num_pages
        self.published = published


# Add your variables below this line
cover = MyEditorialBook.has_cover
code = MyEditorialBook.editorial_code