from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QHBoxLayout, QLineEdit, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем всё

        self.btn_admin = QPushButton("Войти как администратор")
        self.btn_terminal = QPushButton("Открыть терминал")
        self.btn_order = QPushButton("Просмотр заказов")
        self.btn_worker = QPushButton("Окно работников")

        self.btn_admin.clicked.connect(self.main_app.show_admin)
        self.btn_terminal.clicked.connect(self.main_app.show_terminal)
        self.btn_order.clicked.connect(self.show_order_window)  # Открываем окно выдачи
        self.btn_worker.clicked.connect(self.main_app.show_worker)

        layout.addWidget(self.btn_admin)
        layout.addWidget(self.btn_terminal)
        layout.addWidget(self.btn_order)
        layout.addWidget(self.btn_worker)

        # Стилизация
        self.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                height: 45px;
                border-radius: 10px;
                background-color: #4CAF50;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.setLayout(layout)

    def show_order_window(self):
        """ Открывает окно выдачи заказов """
        self.order_window = OrderWindow(self.main_app)
        self.order_window.show()



    def show_password_window(self):
        """ Показывает окно с запросом пароля """
        self.password_window = QWidget()
        self.password_window.setWindowTitle("Авторизация администратора")
        self.password_window.setFixedSize(300, 150)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_password = QLabel("Введите пароль:")
        self.label_password.setFont(QFont("Arial", 12))

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Скрытие символов

        self.btn_check_password = QPushButton("Войти")
        self.btn_check_password.clicked.connect(self.check_password)

        layout.addWidget(self.label_password)
        layout.addWidget(self.password_input)
        layout.addWidget(self.btn_check_password)

        self.password_window.setLayout(layout)
        self.password_window.show()

    def check_password(self):
        """ Проверяет введённый пароль """
        if self.password_input.text() == self.admin_password:
            self.password_window.close()
            self.setup_ui()  # Загружаем админский интерфейс
            self.show()  # Показываем окно администратора
        else:
            QMessageBox.warning(self.password_window, "Ошибка", "Вход запрещен!")  # Сообщение о неверном пароле

    def setup_ui(self):
        """ Создаёт интерфейс окна администратора после успешного входа """
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("Управление меню")
        self.label.setFont(QFont("Arial", 16))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Список категорий
        self.category_list = QListWidget()
        self.category_list.addItems(["Горячие блюда", "Напитки", "Десерты"])  # Заглушка

        # Поле для ввода новой категории
        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("Введите новую категорию")

        # Кнопки управления категориями
        self.btn_add_category = QPushButton("Добавить категорию")
        self.btn_remove_category = QPushButton("Удалить категорию")

        # Список товаров
        self.product_list = QListWidget()
        self.product_list.addItems(["Борщ", "Кофе", "Тирамису"])  # Заглушка

        # Поле для ввода нового товара
        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText("Введите новый товар")

        # Кнопки управления товарами
        self.btn_add_product = QPushButton("Добавить товар")
        self.btn_remove_product = QPushButton("Удалить товар")

        # Кнопка назад
        self.btn_back = QPushButton("Назад в меню")
        self.btn_back.clicked.connect(self.main_app.show_main)

        # Центрирование содержимого
        center_layout = QVBoxLayout()
        center_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        center_layout.addWidget(self.label)
        center_layout.addWidget(QLabel("Категории:"))
        center_layout.addWidget(self.category_list)

        cat_layout = QHBoxLayout()
        cat_layout.addWidget(self.category_input)
        cat_layout.addWidget(self.btn_add_category)
        center_layout.addLayout(cat_layout)
        center_layout.addWidget(self.btn_remove_category)

        center_layout.addWidget(QLabel("Товары:"))
        center_layout.addWidget(self.product_list)

        prod_layout = QHBoxLayout()
        prod_layout.addWidget(self.product_input)
        prod_layout.addWidget(self.btn_add_product)
        center_layout.addLayout(prod_layout)
        center_layout.addWidget(self.btn_remove_product)

        center_layout.addWidget(self.btn_back)

        layout.addLayout(center_layout)

        # Стилизация
        self.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                height: 35px;
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
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit {
                padding: 5px;
            }
        """)

        self.setLayout(layout)
