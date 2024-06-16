import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('your_ui_file.ui', self)  # Replace 'your_ui_file' with your UI file name

        self.value = 0  # Initialize the value
        self.increment_button.clicked.connect(self.increment_value)

    def increment_value(self):
        if self.increment_button.text() == "Increment by 1":
            self.value += 1
        elif self.increment_button.text() == "Increment by 5":
            self.value += 5
        elif self.increment_button.text() == "Increment by 10":
            self.value += 10
        # Add more conditions for other increment amounts as needed

        self.lineEdit.setText(str(self.value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
