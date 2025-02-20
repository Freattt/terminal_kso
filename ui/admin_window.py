from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QHBoxLayout, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class AdminWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app

        self.setWindowTitle("Окно администратора")
        self.setFixedSize(600, 500)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем всё

        # Заголовок
        self.label = QLabel("Управление меню")
        self.label.setFont(QFont("Arial", 18))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Выравниваем по центру

        # Список категорий
        self.category_list = QListWidget()
        self.category_list.addItems(["Горячие блюда", "Напитки", "Десерты"])  # Заглушка
        self.category_list.setFixedHeight(80)

        # Поле для ввода новой категории
        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("Введите новую категорию")

        # Кнопки управления категориями
        self.btn_add_category = QPushButton("Добавить категорию")
        self.btn_remove_category = QPushButton("Удалить категорию")

        # Список товаров
        self.product_list = QListWidget()
        self.product_list.addItems(["Борщ", "Кофе", "Тирамису"])  # Заглушка
        self.product_list.setFixedHeight(80)

        # Поле для ввода нового товара
        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText("Введите новый товар")

        # Кнопки управления товарами
        self.btn_add_product = QPushButton("Добавить товар")
        self.btn_remove_product = QPushButton("Удалить товар")

        # Кнопка назад
        self.btn_back = QPushButton("Назад в меню")
        self.btn_back.clicked.connect(self.main_app.show_main)

        # Добавляем элементы в Layout
        layout.addWidget(self.label)

        layout.addWidget(QLabel("Категории:"))
        layout.addWidget(self.category_list)

        cat_layout = QHBoxLayout()
        cat_layout.addWidget(self.category_input)
        cat_layout.addWidget(self.btn_add_category)
        layout.addLayout(cat_layout)
        layout.addWidget(self.btn_remove_category)

        layout.addWidget(QLabel("Товары:"))
        layout.addWidget(self.product_list)

        prod_layout = QHBoxLayout()
        prod_layout.addWidget(self.product_input)
        prod_layout.addWidget(self.btn_add_product)
        layout.addLayout(prod_layout)
        layout.addWidget(self.btn_remove_product)

        layout.addWidget(self.btn_back)

        # Стилизация
        self.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                height: 40px;
                border-radius: 8px;
                background-color: #1976D2;
                color: white;
            }
            QPushButton:hover {
                background-color: #1565C0;
            }
            QListWidget {
                border: 1px solid #ccc;
                padding: 5px;
                font-size: 14px;
            }
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit {
                height: 30px;
                font-size: 14px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        self.setLayout(layout)
