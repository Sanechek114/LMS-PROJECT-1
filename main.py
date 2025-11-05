from PyQt6.QtWidgets import (QApplication, QStackedWidget, QWidget,
                             QMainWindow)
import sys
from table_search import Ui_form as TS_ui
from addAnimal import Ui_Form as AA_ui


class Table_Search_CLASS(QWidget, TS_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class AddAnimal_CLASS(QWidget, AA_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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
        table_searchWidget = Table_Search_CLASS()
        addAnimalWidget = AddAnimal_CLASS()
        self.layout = QStackedWidget()
        self.layout.addWidget(table_searchWidget)
        self.layout.addWidget(addAnimalWidget)
        self.setCentralWidget(self.layout)
        # подключение кнопки
        table_searchWidget.add_btn.clicked.connect(self.add_animal)

        addAnimalWidget.save_btn.clicked.connect(self.save)

    def open_file(self):
        pass

    def rename_file(self):
        pass

    def delete_file(self):
        pass

    def add_animal(self):
        self.layout.setCurrentIndex(1)

    def edit_pet(self):
        pass

    def save(self):
        self.layout.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
