from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QScrollArea, QLabel, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt

class WorkerWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.setWindowTitle("Окно работников")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Прокручиваемая область для заказов
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.orders_widget = QWidget()
        self.orders_layout = QVBoxLayout()
        self.orders_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.orders_widget.setLayout(self.orders_layout)

        self.scroll_area.setWidget(self.orders_widget)
        layout.addWidget(self.scroll_area)

        # Кнопка "Назад"
        self.btn_back = QPushButton("Назад в меню")
        self.btn_back.setFixedSize(200, 50)
        layout.addWidget(self.btn_back, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

        # Подключение кнопки
        self.btn_back.clicked.connect(self.main_app.show_main)

        # Храним активные окна с деталями заказов
        self.details_windows = []

    def add_order(self, order_id, order_info):
        """ Добавляет заказ в список """
        btn_order = QPushButton(f"Заказ {order_id}")
        btn_order.setFixedSize(200, 50)
        btn_order.clicked.connect(lambda: self.show_order_details(order_info))

        self.orders_layout.addWidget(btn_order, alignment=Qt.AlignmentFlag.AlignCenter)

        # Добавляем разделитель
        self.orders_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

    def show_order_details(self, order_info):
        """ Открывает окно с деталями заказа """
        details_window = QWidget()
        details_window.setWindowTitle("Детали заказа")
        details_layout = QVBoxLayout()

        label_info = QLabel(order_info)
        label_info.setWordWrap(True)

        btn_close = QPushButton("Закрыть")
        btn_close.clicked.connect(details_window.close)

        details_layout.addWidget(label_info)
        details_layout.addWidget(btn_close)
        details_window.setLayout(details_layout)
        details_window.setGeometry(200, 200, 300, 200)  # Размер окна

        self.details_windows.append(details_window)  # Сохраняем ссылку
        details_window.show()
