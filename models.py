from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,
                        create_engine,
                        Integer,
                        String,
                        Boolean,
                        ForeignKey,
                        Date,
                        LargeBinary,
                        DateTime,
                        Table, )
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql+pymysql://root:example@localhost:3306/test', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


def get_session() -> Session:
    return Session()


def delete_all():
    Base.metadata.drop_all(engine)


def create_all():
    Base.metadata.create_all(engine)


class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    born = Column(Date)
    dead = Column(Date)

    def __repr__(self):
        return "<{} ({} - {})>".format(self.name,
                                       self.born if self.born else " ",
                                       self.dead if self.dead else " ")


books_genres = Table('books-genres', Base.metadata,
                     Column('book_id', Integer, ForeignKey('books.book_id')),
                     Column('genre_id', Integer, ForeignKey('genres.genre_id')))


class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    page_amount = Column(Integer)
    publication_year = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    author = relationship('Author', backref='books')
    genres = relationship('Genre', secondary=books_genres, backref='books')

    def __repr__(self):
        return "<{} pages: {} published {}>".format(self.name,
                                                    self.page_amount,
                                                    self.publication_year)


class Genre(Base):
    __tablename__ = 'genres'

    genre_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)

    def __repr__(self):
        return "<{} genre>".format(self.name)


if __name__ == "__main__":
    delete_all()
    create_all()
