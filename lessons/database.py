def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)

#CRUD - create, read, update, delete 
#добавлени, читение, обновление, удаление. 

def add_student(
        conn,
        name,
        age,
        city
):
    conn.execute("""
    INSERT INTO students VALUES
    (?, ?, ?)
    """,
        (name, age, city))
    conn.commit()