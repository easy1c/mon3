import sqlite3
from pathlib import Path
def init_db():
    global db, cursor
    db = sqlite3.connect(
        Path(__file__).parent.parent / "db.sqlite"
    )
    cursor = db.cursor()

def create_tables():

    cursor.execute(""" 
        --sql 
        DROP TABLE IF EXISTS books; 
    """)


    cursor.execute(""" 
        --sql 
        DROP TABLE IF EXISTS types; 
    """)
    cursor.execute(""" 
        --sql 
        CREATE TABLE IF NOT EXISTS books ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT,  
            price INTEGER ,
            id_type INTEGER,
            FOREIGN KEY (id_type) REFERENCES types(id)           
        ); 
    """)

    cursor.execute(""" 
        --sql 
        CREATE TABLE IF NOT EXISTS types ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT
        ); 
    """)
    db.commit()

def populate_db():
    cursor.execute(""" 
        --sql 
        INSERT INTO books (name, price, id_type) VALUES 
            ("Pudge", 500, 1), 
            ("Tinker", 500, 1), 
            ("Abbadon", 600, 2), 
            ("Puck", 600, 3), 
            ("Zeus", 400, 3) 
        """
    )

    cursor.execute(""" 
        --sql 
        INSERT INTO types (name) VALUES 
            ("books"), 
            ("Manga"), 
            ("Comics") 
        """
    )
    db.commit()
def get_courses():
    cursor.execute(""" 
        --sql 
        SELECT * FROM books 
    """)
    return cursor.fetchall()

def get_books_by_type(id):
    cursor.execute("""
    SELECT * FROM  books WHERE id_type = :id_type""",
                   {'id_type' : id})
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_db()









