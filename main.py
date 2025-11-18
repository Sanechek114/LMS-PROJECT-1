from PyQt6.QtWidgets import (QApplication,
                             QInputDialog, QMessageBox,
                             QTableWidgetItem, QHeaderView,
                             QMainWindow)
from PyQt6.QtGui import QIcon
import sys
import sqlite3
from random import choices
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
        self.setWindowIcon(QIcon('res/ico.png'))
        self.setGeometry(100, 100, 1080, 720)
        self.run = False
        self.table_searchWidget = Table_Search_CLASS()
        self.addAnimalWidget = AddAnimal_CLASS()
        self.con = sqlite3.connect('animals_db.sqlite')
        self.cur = self.con.cursor()
        self.load_TR = False
        self.tables = []
        with open('config.txt', mode='r', encoding='utf-8') as f:
            self.settings = f.read().strip()
            while self.settings == '':
                self.open_file()
        self.modified = {}
        self.columns_in_bd = {
            0: 'id',
            1: 'name = ',
            2: 'type = ',
            3: 'year = ',
            4: 'breed = ',
            5: 'code = '}
        # создание менюшки
        self.status_bar = self.statusBar()
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
        self.table_searchWidget.tableWidget.verticalHeader().setVisible(False)
        self.table_searchWidget.tableWidget.setHorizontalHeaderLabels(header)
        header = self.table_searchWidget.tableWidget.horizontalHeader()
        header.setDisabled(False)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        self.table_searchWidget.tableWidget.itemChanged.connect(
            self.save_changes)
        self.load_table()
        with open('theme.txt', mode='r', encoding='utf-8') as f:
            self.theme = f.read()
        if self.theme == 'light':
            self.apply_white()
        else:
            self.apply_black()

    def apply_white(self):
        self.setStyleSheet(LIGHT_THEME)
        self.table_searchWidget.setStyleSheet(LIGHT_THEME)
        self.addAnimalWidget.setStyleSheet(LIGHT_THEME)
        with open('theme.txt', mode='w', encoding='utf-8') as f:
            self.theme = f.write('light')

    def apply_black(self):
        self.setStyleSheet(DARK_THEME)
        self.table_searchWidget.setStyleSheet(DARK_THEME)
        self.addAnimalWidget.setStyleSheet(DARK_THEME)
        with open('theme.txt', mode='w', encoding='utf-8') as f:
            self.theme = f.write('dark')

    def load_table(self):
        self.run = False
        s = self.table_searchWidget.search_line.text()
        res = self.cur.execute(search_query(s, self.settings)).fetchall()
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
        self.table_searchWidget.label.setText(
            f"Поиск по таблице {self.settings}:")
        self.run = True

    def open_file(self):
        self.run = False
        self.tables = list(map(lambda x: x[0], self.cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table';").fetchall()))
        self.tables.remove('sqlite_sequence')
        if len(self.tables) == 0:
            self.create_file()
            print('no table')
        else:
            table, ok_pressed = QInputDialog.getItem(
                self, "Выберите вашу таблицу", "",
                tuple(self.tables), 1, False)
            if table != '' and ok_pressed:
                self.settings = table

            with open('config.txt', mode='w+', encoding='utf-8') as f:
                f.write(self.settings)
            self.load_table()
            if self.load_TR:
                self.load_table()
            else:
                self.load_TR = True
        self.run = True

    def rename_file(self):
        self.run = False
        name, ok_presed = QInputDialog.getText(
            self, 'Ввод', 'Введите название таблицы:')
        if ok_presed:
            self.cur.execute(
                f'ALTER TABLE {self.settings} RENAME TO {name};')
            self.settings = name
            self.load_table()
            with open('config.txt', mode='w+', encoding='utf-8') as f:
                f.write(self.settings)
        self.con.commit()
        self.run = True

    def delete_file(self):
        reply = QMessageBox.question(
            self,
            "Вопрос",
            f"Вы уверены, что хотите удалить\
                      {self.settings} ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.cur.execute(f'DROP TABLE {self.settings}')

            self.con.commit()
            self.open_file()

    def create_file(self):
        with open('config.txt', mode='w+', encoding='utf-8') as f:
            self.settings = f.read().strip()
            if self.settings == '':
                self.settings, ok = QInputDialog.getText(
                    self, 'Ввод', 'Введите название таблицы:')
                if not ok:
                    self.settings = (
                        ''.join(choices('qwertyuiopasdfghjklzxcvbnm',
                                        k=10)))
            f.write(self.settings)
            self.tables.append(self.settings)
            self.cur.execute(create_db_query(self.settings))
            self.con.commit()
        self.load_table()

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
            if reply == QMessageBox.StandardButton.Yes:
                self.cur.execute(delete_query(id, self.settings))
                self.con.commit()
                self.load_table()

    def changed(self, item):
        self.save_changes(item)

    def save_changes(self, item):
        if self.run:
            id = self.table_searchWidget.tableWidget.item(item.row(), 0).text()

            data = []
            for i in range(6):
                data.append(self.table_searchWidget.tableWidget.item(
                    item.row(), i).text())
            day, month, year = tuple(data[3].split('.'))
            self.cur.execute(f"UPDATE {self.settings} SET name = '{data[1]}', \
                                type = '{data[2]}', day = '{day}', \
                                month = {month}, year = {year}, \
                                breed = '{data[4]}', code = '{data[5]}' \
                                WHERE id = {id};")
            self.con.commit()

    def save(self):
        name = self.addAnimalWidget.name.text()
        breed = self.addAnimalWidget.breed.text()
        type = self.addAnimalWidget.species.currentText()
        year, month, day = self.addAnimalWidget.DateEdit.date().getDate()
        code = self.addAnimalWidget.code.text()
        if all([name, breed, code]):
            self.cur.execute(create_row_query(
                self.settings, name, type, day, month, year, code, breed))
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
