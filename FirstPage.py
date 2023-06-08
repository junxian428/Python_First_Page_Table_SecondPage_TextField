from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView
from PyQt5.QtCore import QAbstractTableModel
import sys


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return 1

    def data(self, index, role):
        if role == 0:
            return self.data[index.row()]

        return None


class FirstPage(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.table_view = QTableView()
        self.layout.addWidget(self.table_view)

        self.setLayout(self.layout)

    def updateTable(self, data):
        model = TableModel(data)
        self.table_view.setModel(model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    first_page = FirstPage()
    first_page.show()
    sys.exit(app.exec_())

