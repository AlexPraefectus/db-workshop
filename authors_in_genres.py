from models import Author, Book, Genre, get_session
from sqlalchemy import or_

if __name__ == '__main__':
    session = get_session()
    result = session.query(Author). \
        join(Author.books). \
        join(Book.genres).filter(or_(Genre.name.like('fi%'),
                                     Genre.name == 'detective')). \
        distinct().all()
    print('*'*40)
    print('\n'.join(map(str, result)))
    print('*'*40)
