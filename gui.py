
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from mainwindow import Ui_mainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load the ui file #
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # Hide sliders wich are not active
        self.ui.durationFrame.hide()
        self.ui.frequencyFrame.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
