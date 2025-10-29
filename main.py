from PyQt6.QtWidgets import (QApplication,
                             QMainWindow)
import sys
from ui_file import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.setWindowTitle('Учет сельскохозяйственых животных')
        self.setGeometry(100, 100, 1080, 720)
        # создание менюшки
        menu_bar = self.menuBar()
        menu = menu_bar.addMenu('файл')
        open_act = menu.addAction('открыть файл')
        rename_act = menu.addAction('переименовать файл')
        delete_act = menu.addAction('удалить файл')
        # подлючение меню к функциям
        open_act.triggered.connect(self.open_file)
        rename_act.triggered.connect(self.rename_file)
        delete_act.triggered.connect(self.delete_file)
        # подключение кнопки
        self.add_btn.clicked.connect(self.add_animal)

    def open_file(self):
        pass

    def rename_file(self):
        pass

    def delete_file(self):
        pass

    def add_animal(self):
        pass

    def edit_pet(self):
        pass

    def refresh_table():
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
