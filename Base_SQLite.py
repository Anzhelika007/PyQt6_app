import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username VARCHAR(30),   
    Email VARCHAR(30),
    PhoneNumber VARCHAR(15)
    )""")

    cursor.execute(
        "INSERT INTO users VALUES ('Yanitya','geffelleceffe-7860@yopmail.com','9(3484)364-32-92'), ('Ricahav','kajaddunneito-2898@yopmail.com','5(4119)578-75-50'), ('Corbert','tebrijofuyu-9922@yopmail.com','4(04)160-64-89'), ('Xerxesar','houcrukefamu-5882@yopmail.com','152(238)276-36-46')")

    # cursor.execute('''SELECT * FROM users''')
    # print(cursor.fetchall())


class Interaction:
    def __init__(self):
        # подключились к базе
        self.connection = sqlite3.connect('database.db')

    def add_user(self, Username, Email, PhoneNumber):
        # записываем нового юзера
        cursor = self.connection.cursor()
        bd = ("""INSERT INTO users(Username, Email, PhoneNumber) VALUES (?,?,?)""", a, b, c)
        cursor.execute(bd)
        self.connection.commit()
        cursor.close()

    def show_users(self):
        # показать всех
        cursor = self.connection.cursor()
        bd = ("""SELECT * FROM users""")
        cursor.execute(bd)
        show_all = cursor.fetchall()
        return show_all
        cursor.close()
