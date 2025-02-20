import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QInputDialog, QMessageBox
from ui.main_window import MainWindow
from ui.admin_window import AdminWindow
from ui.terminal import TerminalWindow
from ui.okno_vidachi import OrderWindow
from ui.worker_window import WorkerWindow

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Касса самообслуживания")
        self.setGeometry(100, 100, 800, 600)

        # Создаем менеджер окон
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Добавляем окна
        self.main_window = MainWindow(self)
        self.admin_window = AdminWindow(self)
        self.terminal_window = TerminalWindow(self)
        self.order_window = OrderWindow(self)
        self.worker_window = WorkerWindow(self)

        self.stack.addWidget(self.main_window)      # Главное меню
        self.stack.addWidget(self.admin_window)     # Администратор
        self.stack.addWidget(self.terminal_window)  # Терминал
        self.stack.addWidget(self.order_window)     # Окно выдачи
        self.stack.addWidget(self.worker_window)    # Окно работников

        self.show_main()  # Стартуем с главного меню

        self.admin_password = "1234"  # Пароль администратора (можно менять в коде)

    def show_main(self):
        """Показать главное меню"""
        self.stack.setCurrentWidget(self.main_window)

    def show_admin(self):
        """Показать окно администратора (только после успешного ввода пароля)"""
        password, ok = QInputDialog.getText(self, "Вход", "Введите пароль:",)
        if ok:
            if password == self.admin_password:
                self.stack.setCurrentWidget(self.admin_window)
            else:
                QMessageBox.warning(self, "Ошибка", "Вход запрещен!")

    def show_terminal(self):
        """Показать терминал"""
        self.stack.setCurrentWidget(self.terminal_window)

    def show_order_window(self):
        """ Открывает окно выдачи заказов """
        self.order_window = OrderWindow(self.main_app)
        self.order_window.show()

    def show_order(self):
        """Показать заказы"""
        self.stack.setCurrentWidget(self.order_window)

    def show_worker(self):
        """Показать окно работников"""
        self.stack.setCurrentWidget(self.worker_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
