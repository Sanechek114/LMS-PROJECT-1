dark_style = """
    QMainWindow {
        background-color: #4A4A4A;
    }
    QTableWidget QTableCornerButton::section {
        background: #6F6F6F;
        border: 0px outset black;
    }
    QHeaderView::section {
        background: #6F6F6F;
    }

    QWidget {
        background-color: #404040;
        color: #ffffff;
        font-family: Arial;
    }

    QPushButton {
        background-color: #6F6F6F;
        color: white;
        border: 1px solid #555;
        padding: 1px 16px;
        border-radius: 1px;
        font-size: 14px;
    }

    QPushButton:hover {
        background-color: #505050;
    }

    QPushButton:pressed {
        background-color: #606060;
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
        border: 1px solid #666;
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

    QTableWidget QTableCornerButton::section {
        background: #cccccc;
        border: 0px outset black;
    }

    QHeaderView::section {
        background: #cccccc;
    }

    QWidget {
        background-color: #f5f5f5;
        color: #333333;
        font-family: Arial;
    }

    QPushButton {
        background-color: #e0e0e0;
        color: #333333;
        border: 1px solid #ccc;
        padding: 8px 16px;
        border-radius: 4px;
        font-size: 14px;
    }

    QPushButton:hover {
        background-color: #d0d0d0;
    }

    QPushButton:pressed {
        background-color: #c0c0c0;
    }

    QLineEdit {
        background-color: white;
        color: #333333;
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 6px;
        font-size: 14px;
        selection-background-color: #0078d4;
        selection-color: white;
    }

    QLineEdit:focus {
        border: 1px solid #0078d4;
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
