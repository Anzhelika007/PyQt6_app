import sys
from PyQt6.QtWidgets import QApplication, QDialog
from ui_imagedialog import Ui_MainWindow

from Base_SQLite import Interaction



app = QApplication(sys.argv)
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec())

