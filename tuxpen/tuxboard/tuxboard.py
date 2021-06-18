from PySide6 import (
    QtCore,
    QtGui,
    QtWidgets
)

from .ui import board_ui


class TuxBoard(QtWidgets.QWidget):
    def __init__(self, tux_manager) -> None:
        QtWidgets.QWidget.__init__(self)

        self.tux_manager = tux_manager

        self.ui = board_ui.Ui_Tuxboard()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowState(QtCore.Qt.WindowMaximized)

        self.pen = QtGui.QPen(QtCore.Qt.black, 1)
        self.lastMousePoint = QtGui.QCursor().pos()
        self.endMousePoint = QtGui.QCursor().pos()
        self.pixMap = QtGui.QPixmap(1920, 1080)

    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        painterForPixmap = QtGui.QPainter(self.pixMap)
        painterForPixmap.setPen(self.pen)
        painterForPixmap.drawLine(self.lastMousePoint, self.endMousePoint)

        self.lastMousePoint = self.endMousePoint

        painterForBoard = QtGui.QPainter(self)
        painterForBoard.drawPixmap(0, 0, self.pixMap)

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if not self.tux_manager.coreWindow:
            return

        if e.buttons() == QtCore.Qt.MiddleButton \
                and self.tux_manager.coreWindow.pos().y() <= e.globalPosition().y() <= self.tux_manager.coreWindow.pos().y() + 420 \
                and self.tux_manager.coreWindow.pos().x() <= e.globalPosition().x() <= self.tux_manager.coreWindow.pos().x() + 122:
            self.tux_manager.coreWindow.activateWindow()
        else:
            self.activateWindow()

        if e.buttons() == QtCore.Qt.LeftButton:
            self.endMousePoint = e.pos()
            self.update()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.buttons() == QtCore.Qt.LeftButton:
            self.endMousePoint = e.pos()
            self.update()

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.buttons() == QtCore.Qt.LeftButton:
            self.endMousePoint = e.pos()
            self.update()

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if not self.tux_manager.coreWindow:
            return

        if e.key() == QtCore.Qt.Key_Escape:
            if self.tux_manager.coreWindow.isVisible():
                self.tux_manager.coreWindow.hide()
            else:
                self.tux_manager.coreWindow.show()
                self.activateWindow()

        if e.key() == QtCore.Qt.Key_1:
            self.pen.setWidth(1)
        if e.key() == QtCore.Qt.Key_2:
            self.pen.setWidth(2)
        if e.key() == QtCore.Qt.Key_3:
            self.pen.setWidth(3)
        if e.key() == QtCore.Qt.Key_4:
            self.pen.setWidth(4)
