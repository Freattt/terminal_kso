from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class OrderWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app

        self.setWindowTitle("Просмотр заказов")
        self.setFixedSize(800, 600)

        # Основной layout
        layout = QVBoxLayout()

        # Заголовок
        self.label_title = QLabel("Состояние заказов")
        self.label_title.setFont(QFont("Arial", 20))
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_title)

        # Создание горизонтального layout для двух списков
        list_layout = QHBoxLayout()

        # Колонка "Готовится"
        self.label_preparing = QLabel("Готовится")
        self.label_preparing.setFont(QFont("Arial", 16))
        self.label_preparing.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.list_preparing = QListWidget()

        preparing_layout = QVBoxLayout()
        preparing_layout.addWidget(self.label_preparing)
        preparing_layout.addWidget(self.list_preparing)

        # Колонка "Готово"
        self.label_ready = QLabel("Готово")
        self.label_ready.setFont(QFont("Arial", 16))
        self.label_ready.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.list_ready = QListWidget()

        ready_layout = QVBoxLayout()
        ready_layout.addWidget(self.label_ready)
        ready_layout.addWidget(self.list_ready)

        # Добавляем колонки в горизонтальный layout
        list_layout.addLayout(preparing_layout)
        list_layout.addLayout(ready_layout)

        layout.addLayout(list_layout)

        self.setLayout(layout)

        # Стилизация
        self.setStyleSheet("""
            QListWidget {
                border: 1px solid #ccc;
                padding: 5px;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }
        """)
