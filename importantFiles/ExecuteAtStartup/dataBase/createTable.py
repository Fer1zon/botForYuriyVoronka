
from ...helps import cur, conn




def createUserTable():#Создание юзерских таблиц

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
id TEXT PRIMARY KEY       
);

""")
    

    conn.commit()




def createAdminTable():#Создание админских таблиц
    pass