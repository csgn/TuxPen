import os
import sys
import copy
import pickle
import shutil

from PyQt5 import QtGui

from PyQt5.QtCore import QPoint, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QColorDialog, QLabel, QMainWindow, QPushButton, QWidget

from ui import Ui_Tuxpen


class TxBuffer:
    @staticmethod
    def dump(session, buffer):
        if len(buffer) <= 0:
            return

        file = f"txpen{session}.pkl"
        with open(file, "wb+") as f:
            pickle.dump(buffer, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load(session):
        file = f"txpen{session}.pkl"

        if os.path.exists(file):
            with open(file, "rb") as f:
                return pickle.load(f)

        return []

    @staticmethod
    def clear(session):
        file = f"txpen{session}.pkl"

        if os.path.exists(file):
            os.remove(file)


class TxPoint:
    def __init__(self, x: QPoint, y: QPoint):
        self.x = x
        self.y = y


class TxPenAttr:
    def __init__(self, c, t, s):
        self.c = c
        self.t = t
        self.s = s


class TxBoard(QWidget):
    def __init__(self, session: int) -> None:
        super().__init__()

        self.session = session
        self.isDrawing = False

        self.lastWindowPosition = None
        self.lastMousePosition = None
        self.currentMousePosition = None

        self.tempBuffer = []
        self.undoBuffer = []
        self.redoBuffer = []

        self.penAttr = TxPenAttr(Qt.red, 3, Qt.SolidLine)

        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle(f"Board {self.session}")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowState(Qt.WindowMaximized)

    def setGeometry(self) -> None:
        super().setGeometry(self.lastWindowPosition)

    def show(self) -> None:
        self.undoBuffer = TxBuffer.load(self.session)
        super().show()

    def hide(self) -> None:
        TxBuffer.dump(self.session, self.undoBuffer)
        self.undoBuffer = []
        super().hide()

    def undo(self) -> None:
        if len(self.undoBuffer) > 0:
            self.redoBuffer.append(self.undoBuffer.pop())
            self.update()

    def redo(self) -> None:
        if len(self.redoBuffer) > 0:
            self.undoBuffer.append(self.redoBuffer.pop())
            self.update()

    def clear(self) -> None:
        self.tempBuffer = []
        self.undoBuffer = []
        self.redoBuffer = []

        TxBuffer.clear(self.session)

        self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        if self.isDrawing:
            pen = QtGui.QPen(self.penAttr.c, self.penAttr.t, self.penAttr.s)

            txpoint = TxPoint(self.lastMousePosition,
                              self.currentMousePosition)

            self.tempBuffer.append([self.penAttr, txpoint])
            self.lastMousePosition = self.currentMousePosition

            painter.setPen(pen)
            for b in self.tempBuffer:
                point = b[1]
                painter.drawLine(point.x, point.y)

        for b in self.undoBuffer:
            for p in b:
                buffer_txpen = p[0]
                buffer_point = p[1]
                buffer_pen = QtGui.QPen(
                    buffer_txpen.c, buffer_txpen.t, buffer_txpen.s)

                painter.setPen(buffer_pen)
                painter.drawLine(buffer_point.x, buffer_point.y)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        #print(f"(Board {self.session} - Mouse Clicked)")

        self.currentMousePosition = a0.pos()
        self.isDrawing = True

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        # print(
        # f"(Board {self.session} - Mouse Position - ({a0.x()}, {a0.y()})")

        self.lastMousePosition = self.currentMousePosition
        self.currentMousePosition = a0.pos()

        self.update()

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        #print(f"(Board {self.session} - Mouse Released)")
        self.isDrawing = False

        self.undoBuffer.append(copy.deepcopy(self.tempBuffer))
        self.tempBuffer.clear()


class TxWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.txboards_limit = 4
        self.txboards = self.txboards_limit*[None]
        self.currentBoard = None
        self.offset = None

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(132, 430)

        self.ui = Ui_Tuxpen()
        self.ui.setupUi(self)

        self.initConnections()

        self.show()

    def initConnections(self):
        self.ui.button_pen.clicked.connect(lambda: self.on_openBoard(0))
        self.ui.button_eraser.clicked.connect(self.on_eraserButton)
        self.ui.button_clear.clicked.connect(self.on_clearButton)
        self.ui.button_undo.clicked.connect(self.on_undoButton)
        self.ui.button_redo.clicked.connect(self.on_redoButton)
        self.ui.button_exit.clicked.connect(self.close)

    def on_eraserButton(self):
        pass

    def on_changeBoard(self, session):
        pass

    def on_clearButton(self):
        if self.currentBoard:
            self.currentBoard.clear()

    def on_pickColor(self):
        colorDialog = QColorDialog().getColor()

        if colorDialog and self.currentBoard:
            self.currentBoard.penAttr.c = colorDialog

    def on_openBoard(self, session):
        if len(self.txboards) <= 0:
            return

        if not self.txboards[session]:
            if self.currentBoard:
                self.currentBoard.hide()

            self.txboards[session] = TxBoard(session)
            self.currentBoard = self.txboards[session]

        if self.currentBoard:
            if session == self.currentBoard.session:
                if not self.currentBoard.isVisible():
                    self.currentBoard.show()
                else:
                    self.currentBoard.hide()
            else:
                self.currentBoard.hide()
                self.currentBoard = self.txboards[session]
                self.currentBoard.show()

    def on_undoButton(self):
        if self.currentBoard:
            self.currentBoard.undo()

    def on_redoButton(self):
        if self.currentBoard:
            self.currentBoard.redo()

    def close(self) -> None:
        del self.currentBoard
        del self.txboards
        return super().close()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.offset = e.pos()
        else:
            super().mousePressEvent(e)

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.offset is not None and e.buttons() == Qt.LeftButton:
            self.move(self.pos() + e.pos() - self.offset)
        else:
            super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        self.offset = None
        super().mouseReleaseEvent(e)


if __name__ == '__main__':
    txapp = QApplication(sys.argv)
    txwindow = TxWindow()
    txapp.exec_()
