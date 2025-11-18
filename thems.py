dark_style = """
    QMainWindow {
        background-color: #3a4a3f;
    }

    QWidget {
        background-color: #292929;
        color: #ffffff;
        font-family: Arial;
    }
    QMenu::item {
    border: 1px solid #007ae3;
    border-radius: 4px;
    padding: 2px 2px;
    background-color: #333333;
    }
    QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    }
    QMenuBar::item {
    border: 1px solid #007ae3;
    spacing: 3px;
    background: #004078;
    padding: 4px 4px;
    border-radius: 1px;
    }

    QGroupBox {
    border: 2px solid gray;
    border-radius: 5px;
    margin-top: 10px;
    }

    QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0px 20px;
    }

    QPushButton {
        background-color: #007ae3;
        color: white;
        border: 1px solid #004078;
        padding: 8px 16px;
        border-radius: 4px;
        font-size: 14px;
    }

    QHeaderView::section {
        background: #004078;
    }

    QPushButton:hover {
        background-color: #52afff;
    }

    QPushButton:pressed {
        background-color: #a7d4fa;
    }

    QLineEdit {
        background-color: #232323;
        color: white;
        border: 1px solid #555;
        border-radius: 4px;
        padding: 6px;
        font-size: 14px;
        selection-background-color: #4a4a4a;
    }

    QLineEdit:focus {
        border: 1px solid #005eff;
    }

    QTextBrowser {
        background-color: #232323;
        color: #ffffff;
        border: 1px solid #555;
        border-radius: 4px;
        padding: 8px;
        font-size: 14px;
    }

    QScrollBar:vertical {
        background-color: #2b2b2b;
        width: 15px;
        margin: 0px;
    }

    QScrollBar::handle:vertical {
        background-color: #404040;
        border-radius: 7px;
        min-height: 20px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #505050;
    }
"""

light_style = """
    QMainWindow {
        background-color: #f5f5f5;
    }

    QWidget {
        background-color: #f5f5f5;
        color: #333333;
        font-family: Arial;
    }

    QMenu::item {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 2px 2px;
    background-color: #bcf279;
    }

    QMenuBar::item {
    border: 1px solid #ccc;
    spacing: 3px;
    background: #94e630;
    padding: 4px 4px;
    border-radius: 1px;
    }

    QGroupBox {
    border: 2px solid gray;
    border-radius: 5px;
    margin-top: 10px;
    }
    QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0px 20px;
    }

    QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 2px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    }

    QHeaderView::section {
        background: #bcf279;
    }

    QPushButton {
        background-color: #94e630;
        color: #333333;
        border: 1px solid #ccc;
        padding: 8px 16px;
        border-radius: 4px;
        font-size: 14px;
    }

    QPushButton:hover {
        background-color: #b4ff59;
    }

    QPushButton:pressed {
        background-color: #ceff91;
    }

    QLineEdit {
        background-color: white;
        color: #222222;
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 6px;
        font-size: 14px;
        selection-background-color: #0078d4;
        selection-color: white;
    }

    QLineEdit:focus {
        border: 1px solid #b9d100;
    }

    QTextBrowser {
        background-color: white;
        color: #333333;
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 8px;
        font-size: 14px;
    }

    QScrollBar:vertical {
        background-color: #f5f5f5;
        width: 15px;
        margin: 0px;
    }

    QScrollBar::handle:vertical {
        background-color: #c0c0c0;
        border-radius: 7px;
        min-height: 20px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #a0a0a0;
    }
"""
