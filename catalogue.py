from models import get_session, Book, Author, Genre
from sqlalchemy.orm import joinedload


def var1():
    session = get_session()
    query = session.query(Book).order_by(Book.publication_year).all()
    # print('\n'.join(map(str, query)))
    for book in query:
        print("{} - {} ({}): {}".format(book.author.name,
                                                   book.name,
                                                   book.publication_year,
                                                   [genre.name for genre in book.genres.all()]))


def var2():
    session = get_session()
    query = session.query(Book). \
        order_by(Book.publication_year). \
        options(joinedload(Book.author)). \
        options(joinedload(Book.genres)).all()
    for book in query:
        print("{} - {} ({}): {}".format(book.author.name,
                                        book.name,
                                        book.publication_year,
                                        [genre.name for genre in book.genres]))


if __name__ == '__main__':
    var2()
