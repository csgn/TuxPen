import sys

from PySide6 import (
    QtCore,
    QtGui,
    QtWidgets,
)

from tuxboard import tuxboard

from .ui import base_ui


class Tuxcore(QtWidgets.QMainWindow):
    def __init__(self, primaryScreen) -> None:
        QtWidgets.QMainWindow.__init__(self)
        self.ui = base_ui.Ui_Tuxpen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(132, 430)
        self.offset = None
        self.primaryScreen = primaryScreen

        self.primaryWidth = self.primaryScreen.availableGeometry().width()
        self.primaryHeight = self.primaryScreen.availableGeometry().height()

        self.move(self.primaryWidth-1.0, self.primaryHeight/2.0 - 430/2)

        self.boardWindow = None

        self.ui.button_pen.clicked.connect(self.buttonPen)
        self.ui.button_eraser.clicked.connect(self.buttonErase)
        self.ui.button_undo.clicked.connect(self.buttonUndo)
        self.ui.button_redo.clicked.connect(self.buttonRedo)
        self.ui.button_clear.clicked.connect(self.buttonClear)
        self.ui.button_exit.clicked.connect(self.buttonExit)

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == QtCore.Qt.LeftButton:
            self.offset = e.pos()
        else:
            super().mousePressEvent(e)

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.offset is not None and e.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + e.pos() - self.offset)
        else:
            super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        self.offset = None
        super().mouseReleaseEvent(e)

    def buttonPen(self):
        if self.boardWindow:
            if self.boardWindow.isHidden():
                self.boardWindow.show()
            else:
                self.boardWindow.hide()

    def buttonErase(self):
        ...

    def buttonUndo(self):
        ...

    def buttonRedo(self):
        ...

    def buttonClear(self):
        ...

    def buttonExit(self):
        self.boardWindow.close()
        sys.exit(0)


def execute(*argv):
    app = QtWidgets.QApplication(*argv)

    window = Tuxcore(app.primaryScreen())
    board = tuxboard.TuxBoard()

    window.boardWindow = board
    board.mainWindow = window

    window.show()
    sys.exit(app.exec())
