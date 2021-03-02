from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

import sys


def application():
    app = QApplication(sys.argv)
    window = QWidget()

    window.setWindowTitle("Первый Слой")
    window.resize(300, 250)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
