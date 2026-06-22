import sqlite3 as book


def create_table():
    connection = book.connect('my_baza.db')

    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

    connection.commit()
    connection.close()


def insert_books():
    connection = book.connect('my_baza.db')

    books = [
        ('Book1', 'Author1', 2001, 'Drama', 300, 5),
        ('Book2', 'Author1', 2002, 'Action', 250, 3),
        ('Book3', 'Author2', 2003, 'Fantasy', 400, 7),
        ('Book4', 'Author3', 2004, 'Horror', 350, 2),
        ('Book5', 'Author2', 2005, 'Sci-Fi', 500, 6),
        ('Book6', 'Author4', 2006, 'Romance', 280, 4),
        ('Book7', 'Author5', 2007, 'Mystery', 320, 8),
        ('Book8', 'Author1', 2008, 'Thriller', 360, 5),
        ('Book9', 'Author3', 2009, 'Adventure', 420, 9),
        ('Book10', 'Author2', 2010, 'History', 310, 1),
    ]

    for b in books:
        connection.execute("""
            INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
            VALUES (?, ?, ?, ?, ?, ?)
        """, b)

    connection.commit()
    connection.close()


def get_books_by_author(author):
    connection = book.connect('my_baza.db')
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM books WHERE author = ?
    """, (author,))

    result = cursor.fetchall()
    connection.close()

    return result


def delete_book_by_id(book_id):
    connection = book.connect('my_baza.db')

    connection.execute("""
        DELETE FROM books WHERE id = ?
    """, (book_id,))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_table()
    insert_books()

    print(get_books_by_author("Author1"))
    delete_book_by_id(1)