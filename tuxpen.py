import sys

from PySide6.QtCore import (
        Qt,
        QObject,
        QPoint,
        QRect,
)

from PySide6.QtWidgets import (
        QApplication,
        QMainWindow,
        QWidget,
        QLabel,
)

from PySide6.QtGui import (
        QPainter,
        QBrush,
        QPen,
        QCursor,
        QPixmap,
)

from tuxpen_ui import Ui_Tuxpen
from tuxpen_ui_board import Ui_TuxpenBoard


class TuxpenBoard(QWidget):
    def __init__(self, mainWindow):
        QWidget.__init__(self)
        self.mainWindow = mainWindow

        self.ui = Ui_TuxpenBoard()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.globalPos().y() >= self.mainWindow.pos().y() 		\
           and event.globalPos().y() <= self.mainWindow.pos().y()+420 	\
           and event.globalPos().x() >= self.mainWindow.pos().x() 	\
           and event.globalPos().x() <= self.mainWindow.pos().x()+122:
               self.mainWindow.activateWindow()
        else:
            self.activateWindow()

class Tuxpen(QMainWindow):
    def __init__(self, primaryScreen):
        QMainWindow.__init__(self)
        self.ui = Ui_Tuxpen()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(132, 430)
        self.offset = None
        self.primaryScreen = primaryScreen

        self.setMouseTracking(True)

        self.width = self.primaryScreen.availableGeometry().width()
        self.height = self.primaryScreen.availableGeometry().height()

        print(self.width, self.height)

        self.move(self.width-1.0, self.height/2.0 - 430/2)

        self.boardWindow = TuxpenBoard(self)

        self.ui.button_pen.clicked.connect(self.buttonPenEvent)
        self.ui.button_eraser.clicked.connect(self.buttonEraseEvent)
        self.ui.button_undo.clicked.connect(self.buttonUndoEvent)
        self.ui.button_redo.clicked.connect(self.buttonRedoEvent)
        self.ui.button_clear.clicked.connect(self.buttonClearEvent)
        self.ui.button_exit.clicked.connect(self.buttonExitEvent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def buttonPenEvent(self):
        if self.boardWindow:
            if self.boardWindow.isHidden():
                self.boardWindow.showFullScreen()
                self.boardWindow.show()
            elif self.boardWindow.isVisible():
                self.boardWindow.hide()

    def buttonEraseEvent(self):
        ...

    def buttonUndoEvent(self):
        ...

    def buttonRedoEvent(self):
        ...

    def buttonClearEvent(self):
        ...

    def buttonExitEvent(self):
        self.boardWindow.close()
        sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tuxpen(app.primaryScreen())
    window.show()
    sys.exit(app.exec())
