import sys

from PySide6 import (
    QtCore,
    QtGui,
    QtWidgets,
)

from .ui import base_ui


class TuxCore(QtWidgets.QMainWindow):
    def __init__(self, tux_manager) -> None:
        QtWidgets.QMainWindow.__init__(self)

        self.tux_manager = tux_manager

        self.ui = base_ui.Ui_Tuxpen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(132, 430)

        self.offset = None

        self.move(self.tux_manager.monitorWidth,
                  self.tux_manager.monitorHeight/2.0 - (self.tux_manager.monitorHeight/2)/2)

        self.ui.button_pen.clicked.connect(self.buttonPen)
        self.ui.button_eraser.clicked.connect(self.buttonErase)
        self.ui.button_undo.clicked.connect(self.buttonUndo)
        self.ui.button_redo.clicked.connect(self.buttonRedo)
        self.ui.button_clear.clicked.connect(self.buttonClear)
        self.ui.button_exit.clicked.connect(self.buttonExit)

        self.ui.color_white.clicked.connect(self.buttonColorWhite)
        self.ui.color_black.clicked.connect(self.buttonColorBlack)
        self.ui.color_red.clicked.connect(self.buttonColorRed)
        self.ui.color_green.clicked.connect(self.buttonColorGreen)
        self.ui.color_blue.clicked.connect(self.buttonColorBlue)
        self.ui.color_yellow.clicked.connect(self.buttonColorYellow)

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

    def buttonPen(self) -> None:
        if self.tux_manager.boardWindow:
            if self.tux_manager.boardWindow.isHidden():
                self.tux_manager.boardWindow.show()
            else:
                self.tux_manager.boardWindow.hide()

    def buttonErase(self):
        pass

    def buttonUndo(self):
        pass

    def buttonRedo(self):
        pass

    def buttonClear(self):
        pass

    def buttonExit(self):
        self.tux_manager.boardWindow.close()
        sys.exit(0)

    def buttonColorWhite(self):
        self.tux_manager.boardWindow.pen.setBrush(QtCore.Qt.white)

    def buttonColorBlack(self):
        self.tux_manager.boardWindow.pen.setBrush(QtCore.Qt.black)

    def buttonColorRed(self):
        self.tux_manager.boardWindow.pen.setBrush(QtCore.Qt.red)

    def buttonColorGreen(self):
        self.tux_manager.boardWindow.pen.setBrush(QtCore.Qt.green)

    def buttonColorBlue(self):
        self.tux_manager.boardWindow.pen.setBrush(QtCore.Qt.blue)

    def buttonColorYellow(self):
        self.tux_manager.boardWindow.pen.setBrush(QtCore.Qt.yellow)
