# PyQt6_app
ВЕТКА PQ Designer
1. Оформили дизайн в Qt Desinger > coхранили файл .ui
2. Сформировали файл в консоль  pyuic6 interface.ui 
3. Затем получаем файл .py конвертации верстки из .ui файла (название файла куда конвертируем в документации ui_imagedialog.py)
4. Затем из документации берем код запуска. Обращаем внимание на название импортируемого класса:
    from ui_imagedialog import Ui_MainWindow
    ui = Ui_MainWindow()

    Код из документации:

    import sys
    from PyQt6.QtWidgets import QApplication, QDialog
    from ui_imagedialog import Ui_MainWindow

    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec())
5. Запускаем (смотрим, если мы создавали свои классы в PQ Designer - то нужно создать еще один модуль 
с нашими классами отдельно - описать их там. В файле ui_imagedialog.py в конце будут строки импорта. Только потом запустить, иначе ошибка)
6. 