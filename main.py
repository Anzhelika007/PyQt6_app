from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import sqlite3

# --------------------------------------------------
# Создали таблицу БД
#--------------------------------------------------
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

Form, Window = uic.loadUiType('interface.ui')
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# def show_tabl():


def registration():
    # считываем данные с полей и записываем в кортеж
    user_login = form.userName.text()
    if len(user_login) == 0:
        print('Имя пользователя отсутствует!')

    user_email = form.email.text()
    if user_email == 0 and user_login not in '@':
        print('Неверная почта или ее не ввели')

    user_phone = form.phoneNamber.text()
    if len(user_phone) < 7:
        print('слишком короткий номер')

    user_value = (user_login, user_email, user_phone)
    print(user_login, user_email, user_phone, user_value)

    # очищаем поля
    form.form.userName.clear()
    form.email.clear()
    form.phoneNamber.clear()

    return user_value


# def add_user(user_value):
#     # записываем нового юзера
#     cursor = cconnection.cursor('database.db')
#     bd = ("""INSERT INTO users(Username, Email, PhoneNumber) VALUES (?,?,?)""", a, b, c)
#     cursor.execute(bd)
#     self.connection.commit()
#     cursor.close()



form.addUserBtn.clicked.connect(registration)

app.exec_()
