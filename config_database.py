import sqlite3,os

def connect_database():
    """connect to database """
    try:
        conn = sqlite3.connect("Database//database.db")
        config_database(conn)

    except sqlite3.OperationalError :
        os.system("mkdir Database")
        connect_database()
        print("Database successfully created")

def config_database(conn):
    try:   
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE Users(
            Id INTEGER PRIMARY KEY ,
            Fullname VARCHAR(25) NOT NULL ,
            Message VARCHAR(1000) NOT NULL ,
            Date VARCHAR(25) NOT NULL 
            )
        """)
        conn.close()

    except  sqlite3.OperationalError :
        print("Database already exits")

if __name__ == "__main__":
    connect_database()
