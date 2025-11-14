from PyQt6.QtWidgets import (QApplication, QAbstractItemView,
                             QInputDialog, QMessageBox,
                             QTableWidgetItem, QHeaderView,
                             QTableWidget,
                             QMainWindow)
import sys
import sqlite3
from thems import (dark_style as DARK_THEME,
                   light_style as LIGHT_THEME)
from table_search import Table_Search_CLASS
from addAnimal import AddAnimal_CLASS
from sql_querys import (create_db_query, search_query,
                        delete_query, create_row_query)


class Window(QMainWindow, ):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Учет сельскохозяйственых животных')
        self.setGeometry(100, 100, 1080, 720)
        with open('config.txt', mode='r', encoding='utf-8') as f:
            self.settings = f.read().split('\n')
        self.con = sqlite3.connect(self.settings[0])
        self.cur = self.con.cursor()
        self.modified = {}
        self.columnsinbd = {0: 'id',
                            1: 'name = "{}"',
                            2: 'type = "{}"',
                            3: 'day = {}',
                            4: 'month = {}',
                            5: 'year = {}',
                            6: 'breed = "{}"',
                            7: 'code = "{}"'}
        # создание менюшки
        menu_bar = self.menuBar()
        menu = menu_bar.addMenu('Таблица')
        open_act = menu.addAction('Выбрать другую таблицу')
        rename_act = menu.addAction('Переименовать таблицу')
        create_act = menu.addAction('Создать таблицу')
        delete_act = menu.addAction('Удалить Таблицу')
        theme_menu = menu_bar.addMenu('Тема')
        white_act = theme_menu.addAction('Светлая')
        black_act = theme_menu.addAction('Темная')
        # подлючение меню к функциям
        open_act.triggered.connect(self.open_file)
        rename_act.triggered.connect(self.rename_file)
        create_act.triggered.connect(self.create_file)
        delete_act.triggered.connect(self.delete_file)
        white_act.triggered.connect(self.apply_white)
        black_act.triggered.connect(self.apply_black)
        self.table_searchWidget = Table_Search_CLASS()
        self.addAnimalWidget = AddAnimal_CLASS()
        self.setCentralWidget(self.table_searchWidget)
        # подключение кнопки
        self.table_searchWidget.add_btn.clicked.\
            connect(lambda: self.addAnimalWidget.show())
        self.addAnimalWidget.save_btn.clicked.connect(self.save)
        self.addAnimalWidget.setWindowTitle('Запись информации')
        self.table_searchWidget.del_btn.clicked.connect(self.delete_animal)
        # подключение поисковой строки
        self.table_searchWidget.search_line.textChanged.\
            connect(self.load_table)
        # таблица
        self.table_searchWidget.tableWidget.setColumnCount(6)
        self.table_searchWidget.tableWidget.setRowCount(0)
        header = ['id', 'Имя', 'Вид', 'Дата рождения',
                  'Порода', 'Код на ушной бирке']
        self.table_searchWidget.tableWidget.setHorizontalHeaderLabels(header)
        header = self.table_searchWidget.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        # self.table_searchWidget.tableWidget.itemChanged.\
        #     connect(self.save_changes)
        self.load_table()
        self.setStyleSheet(LIGHT_THEME)
        self.table_searchWidget.setStyleSheet(LIGHT_THEME)
        self.addAnimalWidget.setStyleSheet(LIGHT_THEME)

    def apply_white(self):
        self.setStyleSheet(LIGHT_THEME)
        self.table_searchWidget.setStyleSheet(LIGHT_THEME)
        self.addAnimalWidget.setStyleSheet(LIGHT_THEME)

    def apply_black(self):
        self.setStyleSheet(DARK_THEME)
        self.table_searchWidget.setStyleSheet(DARK_THEME)
        self.addAnimalWidget.setStyleSheet(DARK_THEME)

    def load_table(self):
        s = self.table_searchWidget.search_line.text()
        res = self.cur.execute(search_query(s)).fetchall()
        self.table_searchWidget.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.table_searchWidget.tableWidget.setRowCount(
                self.table_searchWidget.tableWidget.rowCount() + 1)
            self.table_searchWidget.tableWidget.setItem(
                i, 0, QTableWidgetItem(str(row[0])))
            self.table_searchWidget.tableWidget.setItem(
                i, 1, QTableWidgetItem(str(row[1])))
            self.table_searchWidget.tableWidget.setItem(
                i, 2, QTableWidgetItem(str(row[2])))
            self.table_searchWidget.tableWidget.setItem(
                i, 3, QTableWidgetItem(str(f"{row[3]}.{row[4]}.{row[5]}")))
            self.table_searchWidget.tableWidget.setItem(
                i, 4, QTableWidgetItem(str(row[6])))
            self.table_searchWidget.tableWidget.setItem(
                i, 5, QTableWidgetItem(str(row[7])))
        self.modified = {}

    def open_file(self):
        pass

    def rename_file(self):
        pass

    def delete_file(self):
        pass

    def create_file(self):
        pass

    def delete_animal(self):
        row = self.table_searchWidget.tableWidget.currentRow()
        if row != -1:
            name = self.table_searchWidget.tableWidget.item(row,
                                                            1).text().strip()
            id = self.table_searchWidget.tableWidget.item(row, 0).text()
            reply = QMessageBox.question(
                self,
                "Вопрос",
                f"Вы уверены, что хотите удалить\
                      {name} ?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No)
            print(id)
            if reply == QMessageBox.StandardButton.Yes:
                self.cur.execute(delete_query(id))
                self.con.commit()
                self.load_table()
                print('delete')
#
#    def save_changes(self, item):
#        id = self.table_searchWidget.tableWidget.item(item.row(, 0).text()
#        self.modified[id] = item.text()
#        print(item.row(), item.text())

    def save(self):
        name = self.addAnimalWidget.name.text()
        breed = self.addAnimalWidget.breed.text()
        type = self.addAnimalWidget.species.currentText()
        year, month, day = self.addAnimalWidget.DateEdit.date().getDate()
        code = self.addAnimalWidget.code.text()
        print(name, type, day, month, year, breed, code)
        if all([name, breed, code]):
            self.cur.execute(create_row_query(name, type, day,
                                              month, year, code, breed))
            self.addAnimalWidget.close()
            self.con.commit()
            self.load_table()
        else:
            QMessageBox.information(
                self,
                "Скотина",
                "Все поля должны быть заполнены.",
                buttons=QMessageBox.StandardButton.Ok)

    def closeEvent(self, event):
        self.con.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
