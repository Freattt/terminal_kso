import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton,
    QScrollArea, QWidget, QLabel, QGridLayout, QStackedWidget, QDialog, QTableWidget, QTableWidgetItem
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class TerminalWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("")

        layout = QVBoxLayout()

        self.btn_to_terminal = QPushButton("Перейти в терминал")
        self.btn_to_terminal.clicked.connect(self.controller.show_terminal)

        layout.addWidget(self.btn_to_terminal)
        self.setLayout(layout)

class SelfServiceTerminal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Терминал самообслуживания")
        self.showFullScreen()  # Открытие окна на весь экран
        self.product_counter = 1  # Уникальный номер для каждого товара
        self.order_counter = 1  # Уникальный номер заказа

        # Основной виджет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Основной вертикальный layout (корзина снизу)
        main_layout = QVBoxLayout(central_widget)

        # Верхняя часть: категории и товары
        top_layout = QHBoxLayout()

        # Прокручиваемая область для категорий (слева)
        self.category_scroll_area = QScrollArea(self)
        self.category_scroll_area.setWidgetResizable(True)
        category_container = QWidget()
        category_layout = QVBoxLayout(category_container)

        # Создаем кнопки категорий
        self.categories = ["Бургеры", "Напитки", "Десерты"]
        for i, category in enumerate(self.categories):
            button = QPushButton(category)
            button.setFixedHeight(80)  # Высота кнопок категорий
            button.setStyleSheet("border: none; background-color: white;")
            button.clicked.connect(lambda _, idx=i: self.show_category(idx))
            category_layout.addWidget(button)

        self.category_scroll_area.setWidget(category_container)
        self.category_scroll_area.setFixedWidth(200)  # Ширина панели категорий
        top_layout.addWidget(self.category_scroll_area)

        # Динамическая область для товаров (центральная часть)
        self.stacked_widget = QStackedWidget(self)
        self.category_pages = []

        # Словарь для товаров и их изображений
        self.product_images = {
            "Бургеры": ["burger1.jpg", "burger2.jpg", "burger3.jpg", "burger4.jpg", "burger5.jpg", "burger6.jpg", "burger7.jpg", "burger8.jpg", "burger9.jpg"],
            "Напитки": ["drink1.png", "drink1.png", "drink1.png", "drink1.png", "drink1.png", "drink1.png", "drink1.png", "drink1.png", "drink1.png"],
            "Десерты": ["dessert1.jpg", "dessert1.jpg", "dessert1.jpg", "dessert1.jpg", "dessert1.jpg", "dessert1.jpg", "dessert1.jpg", "dessert1.jpg", "dessert1.jpg"]
        }

        for category in self.categories:
            page = QWidget()
            grid_layout = QGridLayout(page)

            # Добавляем товары в каждую категорию
            for row in range(3):  # 3 строки продуктов
                for col in range(3):  # 3 столбца продуктов
                    product_index = row * 3 + col
                    if product_index < len(self.product_images[category]):
                        product_name = f"{category} {product_index + 1}"
                        product_image = self.product_images[category][product_index]
                        product_button = self.create_product_button(
                            product_name,
                            100,  # Цена товара
                            product_image
                        )
                        grid_layout.addWidget(product_button, row, col)

            self.stacked_widget.addWidget(page)
            self.category_pages.append(page)

        top_layout.addWidget(self.stacked_widget)

        # Добавляем верхнюю часть в основной layout
        main_layout.addLayout(top_layout)

        # Нижняя часть: корзина
        cart_layout = QHBoxLayout()

        # Информация о корзине (слева внизу)
        self.cart_info = QLabel("Товаров: 0\nИтого: 0₽")
        self.cart_info.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.cart_info.setStyleSheet("background-color: white; border: none;")
        cart_layout.addWidget(self.cart_info)

        # Кнопка "Показать корзину" (справа внизу)
        show_cart_button = QPushButton("Показать корзину")
        show_cart_button.setFixedSize(200, 60)
        show_cart_button.setStyleSheet("border: none; background-color: white;")
        show_cart_button.clicked.connect(self.show_cart)
        cart_layout.addWidget(show_cart_button)

        # Добавляем корзину в основной layout
        main_layout.addLayout(cart_layout)

        # Параметры корзины
        self.cart_total_items = 0
        self.cart_total_price = 0
        self.cart_items = []  # Список товаров в корзине

    def create_product_button(self, name, price, image_path):
        """Создаёт кнопку продукта с изображением, названием и ценой."""
        button = QPushButton()
        button.setFixedSize(180, 240)  # Пропорции кнопки под формат 4:3
        button.setStyleSheet("border: none; background-color: white;")

        # Устанавливаем изображение на кнопку
        icon = QIcon(image_path)
        button.setIcon(icon)
        button.setIconSize(QSize(180, 135))  # Формат 4:3

        # Устанавливаем текст под изображением
        button.setText(f"{name}\n{price}₽")
        button.setStyleSheet("text-align: bottom; background-color: white; border: none;")

        button.clicked.connect(lambda: self.add_to_cart(name, price))
        return button

    def show_category(self, index):
        """Показываем товары выбранной категории."""
        self.stacked_widget.setCurrentIndex(index)

    def add_to_cart(self, name, price):
        """Добавляем товар в корзину с уникальным номером."""
        self.cart_total_items += 1
        self.cart_total_price += price
        item_with_number = f"{name} #{self.product_counter}"
        self.cart_items.append((item_with_number, price))
        self.product_counter += 1  # Увеличиваем счётчик товаров
        self.update_cart_info()

    def update_cart_info(self):
        """Обновление информации в корзине."""
        self.cart_info.setText(f"Товаров: {self.cart_total_items}\nИтого: {self.cart_total_price}₽")

    def show_cart(self):
        """Открытие окна корзины с возможностью удаления товаров."""
        try:
            dialog = QDialog(self)
            dialog.setWindowTitle("Корзина")
            dialog.showFullScreen()  # Открытие корзины на весь экран

            layout = QVBoxLayout(dialog)

            # Таблица товаров в корзине
            table = QTableWidget(len(self.cart_items), 3)  # Три колонки: Название, Цена, Удалить
            table.setStyleSheet("border: none; font-size: 16px;")  # Убираем рамку таблицы

            # Заполнение таблицы
            for row, (name, price) in enumerate(self.cart_items):
                table.setItem(row, 0, QTableWidgetItem(name))
                table.setItem(row, 1, QTableWidgetItem(f"{price}₽"))

                # Создаем кнопку "Удалить"
                delete_button = QPushButton("Удалить")
                delete_button.setStyleSheet("background-color: red; color: white; font-size: 14px;")
                delete_button.clicked.connect(lambda _, r=row: self.remove_from_cart(r, dialog))
                table.setCellWidget(row, 2, delete_button)

            table.horizontalHeader().hide()  # Скрываем заголовки таблицы
            table.verticalHeader().hide()
            table.setShowGrid(False)

            # Настройка размеров столбцов таблицы
            header = table.horizontalHeader()
            header.setStretchLastSection(True)
            header.setSectionResizeMode(0, header.ResizeMode.Stretch)
            header.setSectionResizeMode(1, header.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(2, header.ResizeMode.ResizeToContents)

            layout.addWidget(table)

            # Кнопка "Назад"
            back_button = QPushButton("Назад")
            back_button.setFixedSize(150, 60)
            back_button.clicked.connect(dialog.close)
            layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)

            # Кнопка "Оформить заказ"
            confirm_button = QPushButton("Оформить заказ")
            confirm_button.setFixedSize(200, 60)
            confirm_button.clicked.connect(lambda: self.confirm_order(dialog))
            layout.addWidget(confirm_button, alignment=Qt.AlignmentFlag.AlignRight)

            dialog.exec()
        except Exception as e:
            print(f"Ошибка при открытии корзины: {e}")

    def confirm_order(self, dialog):
        """Подтверждение заказа с выводом информации и кнопкой возврата."""
        order_code = f"{self.order_counter:04}"  # Код заказа из 4 цифр
        self.order_counter += 1  # Увеличиваем счётчик заказов

        # Закрываем окно корзины
        dialog.close()

        # Создаем новое окно для информации о заказе
        confirmation_dialog = QDialog(self)
        confirmation_dialog.setWindowTitle("Заказ оформлен")
        confirmation_dialog.setStyleSheet("font-size: 18px;")
        confirmation_dialog.showFullScreen()  # Открываем на весь экран

        # Создаем layout для окна подтверждения
        layout = QVBoxLayout(confirmation_dialog)

        # Сообщение об успехе
        success_label = QLabel(
            f"Ваш заказ принят!\n\nКод заказа: {order_code}\n"
            f"Товаров: {self.cart_total_items}\nИтого: {self.cart_total_price}₽"
        )
        success_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        success_label.setStyleSheet("font-size: 24px; padding: 20px;")
        layout.addWidget(success_label)

        # Кнопка "Закрыть" для возврата на основной экран
        close_button = QPushButton("Закрыть")
        close_button.setFixedSize(200, 60)
        close_button.setStyleSheet("font-size: 18px; background-color: lightgray;")
        close_button.clicked.connect(confirmation_dialog.close)
        layout.addWidget(close_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Сбрасываем корзину
        self.cart_total_items = 0
        self.cart_total_price = 0
        self.cart_items = []
        self.update_cart_info()

        # Отображаем окно
        confirmation_dialog.exec()

    def remove_from_cart(self, row, dialog):
        """Удаляет товар из корзины."""
        try:
            name, price = self.cart_items[row]
            self.cart_total_items -= 1
            self.cart_total_price -= price
            del self.cart_items[row]  # Удаляем товар из корзины

            # Обновляем информацию и таблицу корзины
            self.update_cart_info()
            dialog.close()  # Закрываем окно корзины
            self.show_cart()  # Перезапускаем окно корзины для обновления
        except IndexError:
            print("Ошибка удаления: неверный индекс товара.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelfServiceTerminal()
    window.show()
    sys.exit(app.exec())
