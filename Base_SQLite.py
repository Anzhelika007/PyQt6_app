import sqlite3

# --------------------------------------------------
# Создали таблицу БД
# --------------------------------------------------
with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    Username_id VARCHAR(30),   
    Email VARCHAR(30),
    PhoneNumber VARCHAR(15)
    )""")

    users_x = [('Yanitya', 'geffelleceffe-7860@yopmail.com', '9(3484)364-32-92'),
               ('Ricahav', 'kajaddunneito-2898@yopmail.com', '5(4119)578-75-50'),
               ('Corbert', 'tebrijofuyu-9922@yopmail.com', '4(04)160-64-89'),
               ('Xerxesar', 'houcrukefamu-5882@yopmail.com', '152(238)276-36-46')]

    cursor.executemany("INSERT INTO users(Username_id, Email, PhoneNumber) VALUES (?,?,?)", users_x)

    for i in cursor.execute('SELECT * FROM users'):
        print(i)

#     cursor.execute('''DELETE FROM users''')
