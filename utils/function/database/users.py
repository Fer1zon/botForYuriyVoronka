from sqlite3 import Cursor, Connection


def checkUserInDB(userId : int, cur : Cursor) -> bool:
    if cur.execute("SELECT * FROM users WHERE id = ?", (userId,)).fetchone() is None:
        return False
    
    return True



def addInDB(userId : int, cur : Cursor, conn : Connection) -> None:
    cur.execute("INSERT INTO users VALUES(?)", (userId,))
    conn.commit()



def getAllUsers(cur:Cursor):
    return cur.execute("SELECT * FROM users").fetchall()


