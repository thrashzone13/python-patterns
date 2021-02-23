# initial class


class Book:
    __page = 0

    def open(self):
        self.__page = 1

    def close(self):
        self.__page = 0

    def turn_page(self):
        self.__page += 1

    def get_page(self):
        return self.__page

# it's a book but kinda diffrent ...


class EBook:
    __page = 0

    def __init__(self, total_pages) -> None:
        self.total_pages = total_pages

    def start(self):
        self.__page = 1

    def exit(self):
        self.__page = 0

    def next_page(self):
        self.__page += 1

    def get_status(self):
        return {'current': self.__page, 'total': self.total_pages}

# adapter is in charge of handling the differences


class EBookAdapter:
    def __init__(self, e_book: EBook) -> None:
        self.e_book = e_book

    def open(self):
        self.e_book.start()

    def close(self):
        self.e_book.exit()

    def turn_page(self):
        self.e_book.next_page()

    def get_page(self):
        return self.e_book.get_status().get('current')


kindle = EBook(100)
ebook_like_book = EBookAdapter(kindle)

ebook_like_book.open()
ebook_like_book.turn_page()  # page 2
ebook_like_book.turn_page()  # page 3
print(ebook_like_book.get_page())
