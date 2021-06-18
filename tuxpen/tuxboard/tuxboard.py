from PySide6 import (
    QtCore,
    QtGui,
    QtWidgets
)

from .ui import board_ui


class TuxBoard(QtWidgets.QWidget):
    def __init__(self) -> None:
        QtWidgets.QWidget.__init__(self)

        self.ui = board_ui.Ui_Tuxboard()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowState(QtCore.Qt.WindowMaximized)

        self.mainWindow = None

        self.isDrawing = False
        self.lastMousePoint = QtCore.QPoint()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if not self.mainWindow:
            return

        if e.buttons() == QtCore.Qt.MiddleButton \
                and self.mainWindow.pos().y() <= e.globalPosition().y() <= self.mainWindow.pos().y() + 420 \
                and self.mainWindow.pos().x() <= e.globalPosition().x() <= self.mainWindow.pos().x() + 122:
            self.mainWindow.activateWindow()
        else:
            self.activateWindow()

        if e.buttons() == QtCore.Qt.LeftButton:
            self.isDrawing = True
            self.lastMousePoint = e.pos()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        ...

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.isDrawing:
            self.isDrawing = False

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if not self.mainWindow:
            return

        if e.key() == QtCore.Qt.Key_Escape:
            if self.mainWindow.isVisible():
                self.mainWindow.hide()
            else:
                self.mainWindow.show()
                self.activateWindow()
