import sqlite3

from lessons.database import (
    create_tables,
    add_student
)


if __name__ == "__main__":
    connection = sqlite3.connect(
        "database.db"
    )

    create_tables(connection)
    add_student(
        connection,
        'Artur',
        19,
        'Karakol'
    )
    add_student(
        connection,
        'Sardar',
        20,
        'Batken'
        )
    add_student(
        connection,
        'Adema',
        16,
        'Bishkek'
    )
    connection.close()