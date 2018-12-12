select distinct authors.name from (authors
join
    books on authors.author_id = books.author_id
join
    `books-genres` on books.book_id = `books-genres`.book_id
join
    (select genres.name, genre_id from genres
         where genres.name like 'fi%' or
               genres.name = 'detective') as g
    on `books-genres`.genre_id = g.genre_id)