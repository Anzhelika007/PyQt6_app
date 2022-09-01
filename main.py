# Для исполнения команд строки
import sys
import sqlite3
# Для динамической конвертации файла
from PyQt5 import uic
# Импортируем все виджеты, которые собираемся использовать в работе
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QHeaderView
from PyQt5 import QtWidgets


# Создали класс и наследуем главное окно


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load the ui file
        uic.loadUi("interface.ui", self)
        # Манипуляции
        #self.labetableWidgetl_11.setText('erthtzrjnsymzgs')
        # вызвали функцию показа таблицы
        self.load_db()

        self.addUserBtn.clicked.connect(self.reg)
        self.addUserBtn.clicked.connect(self.load_db)

        # вызвали функцию показа обновленную таблицы
        self.load_db()

    def reg(self):
        self.user_login = self.userName.text()
        self.user_email = self.email.text()
        self.user_phone = self.phoneNamber.text()
        self.user_value = (self.user_login, self.user_email, self.user_phone)
        print(self.user_value)

        self.conn = sqlite3.connect('database.db')
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users(Username_id, Email, PhoneNumber) VALUES (?,?,?)", self.user_value)
        self.conn.commit()
        cursor.close()

        self.userName.clear()
        self.email.clear()
        self.phoneNamber.clear()


    def load_db(self):
        self.conn = sqlite3.connect('database.db')
        cursor = self.conn.cursor()
        self.show_users = 'SELECT * FROM users'

        # кол-во строк
        self.tableWidget.setRowCount(10)

        self.table_row = 0
        for row in cursor.execute(self.show_users):
            self.tableWidget.setItem(self.table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(self.table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(self.table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.table_row = self.table_row + 1
        cursor.close()




        # show the app
        self.show()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
