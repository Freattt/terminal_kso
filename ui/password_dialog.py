from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PasswordDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Введите пароль")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Пароль:")
        self.input_field = QLineEdit()
        self.input_field.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_ok = QPushButton("ОК")
        self.btn_cancel = QPushButton("Отмена")

        self.btn_ok.clicked.connect(self.check_password)
        self.btn_cancel.clicked.connect(self.reject)

        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.btn_ok)
        layout.addWidget(self.btn_cancel)

        self.setLayout(layout)

    def check_password(self):
        if self.input_field.text() == "1234":  # Пароль можно менять здесь
            self.accept()
        else:
            self.label.setText("Неверный пароль!")
            self.label.setStyleSheet("color: red;")
