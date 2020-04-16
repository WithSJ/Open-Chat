import sqlite3
import datetime
def id_number():
    conn = sqlite3.connect("Database//database.db")
    curr = conn.cursor()
    
    curr.execute("""
        SELECT COUNT(*) FROM Users
    """)
    Id =curr.fetchone()
    conn.close()
    
    return Id[0]+1
def post(Fullname,Message):
    Id = id_number()
    Date = str(datetime.datetime.now()).split('.')[0]
    conn = sqlite3.connect("Database//database.db")
    curr = conn.cursor()
    
    curr.execute("""
        INSERT INTO Users(Id,Fullname,Message,Date)
        VALUES(?,?,?,?)
    """,(Id,Fullname,Message,Date))

    conn.commit()
    conn.close()
def get_data():
    conn = sqlite3.connect("Database//database.db")
    curr = conn.cursor()
    
    curr.execute("""
        SELECT * FROM Users
        ORDER BY Id DESC
    """)
    result = curr.fetchall()
    conn.close()
    return result
