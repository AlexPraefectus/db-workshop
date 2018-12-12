# database populating script
from models import Author, Book, Genre, get_session
from datetime import date

session = get_session()

fiction = Genre(name='fiction')
adventures = Genre(name='adventures')
detective = Genre(name='detective')
child_l = Genre(name='child literature')
novel = Genre(name='novel')


# Veronica Roth
Veronica_Roth = Author(name="Veronica Roth", born=date(day=19, month=8, year=1988))

Divirgent = Book(name="Divirgent", page_amount=72, publication_year=2011,
                 author=Veronica_Roth)
Divirgent.genres.extend([fiction, adventures])

Insurgent = Book(name="Insurgent", page_amount=75, publication_year=2012,
                 author=Veronica_Roth)
Insurgent.genres.extend([fiction, adventures])
# session.add([Veronica_Roth, Divirgent, Insurgent])

# Agatha Christie
Agatha_Christie = Author(name='Agatha Christie',
                         born=date(day=15, month=9, year=1890),
                         dead=date(day=12, month=1, year=1976))

Evil = Book(name="Evil Under the Sun", page_amount=41, publication_year=2006,
            author=Agatha_Christie)
Evil.genres.append(detective)

Five = Book(name="Five Little Pigs", page_amount=37, publication_year=2007,
            author=Agatha_Christie)
Five.genres.append(detective)

Murder = Book(name="Murder in Mesopotamia", page_amount=48, publication_year=2007,
              author=Agatha_Christie)
Murder.genres.append(detective)
# session.add_all([Agatha_Christie, Evil, Five, Murder])

# Cowell Cressida
Cowell_Cressida = Author(name="Cowell Cressida",
                         born=date(day=15, month=4, year=1966))

Dragon = Book(name="How to Train Your Dragon", page_amount=256, publication_year=2010,
              author=Cowell_Cressida)
Dragon.genres.extend([child_l, fiction])

Pirate = Book(name="How to be a Pirate", page_amount=230, publication_year=2012,
              author=Cowell_Cressida)
Pirate.genres.extend([child_l, fiction])
# session.add_all([Cowell_Cressida, Dragon, Pirate])

# Steven King
Steven_King = Author(name="Stephen Edward King", born=date(day=21, month=9, year=1947))

Carrie = Book(name='Carrie', page_amount=199, publication_year=1974,
              author=Steven_King)
Carrie.genres.append(novel)

Talisman = Book(name='The Talisman', page_amount=646, publication_year=1984,
                author=Steven_King)
Talisman.genres.extend([novel, fiction])

Bag = Book(name="Bag of Bones", page_amount=529, publication_year=1998,
           author=Steven_King)
Bag.genres.append(novel)

Outsider = Book(name="The Outsider", page_amount=576, publication_year=2018,
                author=Steven_King)
Outsider.genres.extend([novel, detective])
# session.add_all([Steven_King, Carrie, Talisman, Bag, Outsider])


if __name__ == "__main__":
    for entity in globals().copy().values():
        if entity.__class__ in (Genre, Author, Book):
            session.add(entity)
    session.commit()
