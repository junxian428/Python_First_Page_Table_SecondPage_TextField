from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSignal
import sys
from FirstPage import FirstPage


class SecondPage(QWidget):
    sendData = pyqtSignal(list)

    def __init__(self, first_page):
        super().__init__()

        self.first_page = first_page

        self.layout = QVBoxLayout()

        self.label = QLabel("Data to Update First Page:")
        self.layout.addWidget(self.label)

        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit)

        self.button = QPushButton("Update First Page")
        self.button.clicked.connect(self.sendDataToFirstPage)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def sendDataToFirstPage(self):
        data = self.line_edit.text()
        self.sendData.emit([data])

        self.line_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    first_page = FirstPage()
    second_page = SecondPage(first_page)

    second_page.sendData.connect(first_page.updateTable)

    first_page.show()
    second_page.show()
    sys.exit(app.exec_())
