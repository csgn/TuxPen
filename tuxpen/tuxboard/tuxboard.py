from PySide6 import (
    QtCore,
    QtGui,
    QtWidgets
)

from .ui import board_ui


class TuxBoard(QtWidgets.QWidget):
    def __init__(self, tux_manager: object) -> None:
        QtWidgets.QWidget.__init__(self)
        self.setMouseTracking(True)

        self.tux_manager = tux_manager

        self.ui = board_ui.Ui_Tuxboard()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowState(QtCore.Qt.WindowMaximized)

        self.isDrawing = False
        self.pen = QtGui.QPen(QtCore.Qt.white, 2)
        self.beginMousePoint = QtCore.QPoint(0, 0)
        self.endMousePoint = QtCore.QPoint(0, 0)
        self.pixMap = None
        self.clearPixmap()

        self.paintUBuffer = []
        self.paintRBuffer = []

    def clearPixmap(self):
        self.pixMap = QtGui.QPixmap(self.tux_manager.monitorWidth,
                                    self.tux_manager.monitorHeight)

    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        painterPixmap = QtGui.QPainter(self.pixMap)
        painterPixmap.setPen(self.pen)
        painterPixmap.drawLine(self.beginMousePoint, self.endMousePoint)

        painterBoard = QtGui.QPainter(self)
        painterBoard.drawPixmap(0, 0, self.pixMap)

        self.beginMousePoint = self.endMousePoint

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.isDrawing:
            self.endMousePoint = e.pos()
            self.update()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        # FOCUSING CORE WINDOW
        corePos = self.tux_manager.coreWindow.pos()
        if e.buttons() == QtCore.Qt.MiddleButton \
                and corePos.y() <= e.globalPosition().y() \
                <= corePos.y() + 420 \
                and corePos.x() <= e.globalPosition().x() \
                <= corePos.x() + 122:
            self.tux_manager.coreWindow.activateWindow()
        else:
            self.activateWindow()

        if e.buttons() == QtCore.Qt.LeftButton:
            self.isDrawing = True
            self.beginMousePoint = self.endMousePoint = e.pos()

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == QtCore.Qt.LeftButton:
            self.isDrawing = False
            self.endMousePoint = e.pos()
            self.update()
            self.paintUBuffer.append(self.pixMap.copy())

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
