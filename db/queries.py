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
        CREATE TABLE IF NOT EXISTS books ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT,  
            price INTEGER 
        ); 
    """)
    db.commit()
def populate_db():
    cursor.execute(""" 
        --sql 
        INSERT INTO books (name, price) VALUES 
            ("Pudge", 5), 
            ("Tinker", 5), 
            ("Abbadon", 6), 
            ("Puck", 6), 
            ("Zeus", 4) 
        """
    )
    db.commit()
def get_courses():
    cursor.execute(""" 
        --sql 
        SELECT * FROM books 
    """)
    return cursor.fetchall()

if __name__ == "__main__":
    init_db()
    create_tables()
    populate_db()









