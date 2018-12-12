from models import get_session, Book, Genre, Author


if __name__ == "__main__":
    session = get_session()
    before_2000 = session.query(Book).filter(Book.publication_year < 2000).\
        order_by(Book.publication_year.desc()).all()
    print('*'*40)
    print('Query raw result:')
    print("\n".join(map(str, before_2000)))
    print('*'*40)
    print('Books published before 2000 in descending order:\n' + '\n'.join(
        "{} - {}".format(book.name, book.publication_year) for book in before_2000))
    print("*"*40)
    after_2000 = session.query(Book).filter(Book.publication_year > 2000).\
        order_by(Book.publication_year).all()
    print('*'*40)
    print('Books published after 2000 in ascending order:\n' + '\n'.join(
        "{} - {}".format(book.name, book.publication_year) for book in after_2000))
    print('*'*40)
    live = session.query(Author).filter(Author.dead.is_(None)). \
        order_by(Author.born).all()
    print('*'*40)
    print('List of alive authors (eldest first):')
    print('\n'.join('{} - born at {}'.format(author.name, author.born) for author in live))



