import sys
import copy

from PyQt5 import QtGui

from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QColorDialog, QLabel, QMainWindow, QPushButton, QWidget


class TxCore:
    def __init__(self, *args, **kwargs) -> None:
        self.__txapp = TxApplication(*args, *kwargs)

    def exec(self):
        sys.exit(self.__txapp.exec_())


class TxApplication(QApplication):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__txwindow = TxWindow()


class TxBoard(QWidget):
    def __init__(self, session: int) -> None:
        super().__init__()

        self.session = session
        self.isDrawing = False

        self.lastWindowPosition = None
        self.lastMousePosition = None
        self.currentMousePosition = None

        self.buffer = []
        self.undoBuffer = []
        self.redoBuffer = []

        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle(f"Board {self.session}")

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowState(Qt.WindowMaximized)

    def setGeometry(self) -> None:
        super().setGeometry(self.lastWindowPosition)

    def show(self) -> None:
        super().show()

    def hide(self) -> None:
        super().hide()

    def undo(self) -> None:
        if len(self.undoBuffer) > 0:
            self.redoBuffer.append(self.undoBuffer.pop())
            self.update()

    def redo(self) -> None:
        if len(self.redoBuffer) > 0:
            self.undoBuffer.append(self.redoBuffer.pop())
            self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if not self.lastMousePosition and not self.currentMousePosition:
            return

        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(Qt.red, 3, Qt.SolidLine))

        if self.isDrawing:
            self.buffer.append(
                (self.lastMousePosition, self.currentMousePosition))

            self.lastMousePosition = self.currentMousePosition

            for pos in self.buffer:
                painter.drawLine(*pos)

        for ub in self.undoBuffer:
            for p in ub:
                painter.drawLine(*p)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print(f"(Board {self.session} - Mouse Clicked)")

        self.currentMousePosition = a0.pos()
        self.isDrawing = True

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        print(f"(Board {self.session} - Mouse Released)")
        self.isDrawing = False

        if len(self.buffer) > 0:
            self.undoBuffer.append(copy.deepcopy(self.buffer))
            self.buffer = []
            self.update()

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        print(
            f"(Board {self.session} - Mouse Position - ({a0.x()}, {a0.y()})")

        self.lastMousePosition = self.currentMousePosition
        self.currentMousePosition = a0.pos()

        self.update()


class TxWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.txboards_limit = 4
        self.txboards = self.txboards_limit*[None]
        self.currentBoard = None

        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("Tuxpen")
        self.setGeometry(100, 100, 150, 480)

        self.undoButton = QPushButton("Undo", self)
        self.undoButton.clicked.connect(self.on_UndoButton)
        self.undoButton.move(0, 10)

        self.redoButton = QPushButton("Redo", self)
        self.redoButton.clicked.connect(self.on_RedoButton)
        self.redoButton.move(0, 50)

        self.boardButton0 = QPushButton(f"{0}", self)
        self.boardButton0.clicked.connect(lambda: self.on_openBoard(0))
        self.boardButton0.move(0, 100)

        self.boardButton1 = QPushButton(f"{1}", self)
        self.boardButton1.clicked.connect(lambda: self.on_openBoard(1))
        self.boardButton1.move(0, 150)

        self.boardButton2 = QPushButton(f"{2}", self)
        self.boardButton2.clicked.connect(lambda: self.on_openBoard(2))
        self.boardButton2.move(0, 200)

        self.boardButton3 = QPushButton(f"{3}", self)
        self.boardButton3.clicked.connect(lambda: self.on_openBoard(3))
        self.boardButton3.move(0, 250)

        self.normalMode = QPushButton("Normal Mode", self)
        self.normalMode.clicked.connect(self.on_normalMode)
        self.normalMode.move(0, 300)

    def on_normalMode(self):
        if self.currentBoard:
            self.currentBoard.hide()
            self.currentBoard = None

    def on_openBoard(self, session):
        if len(self.txboards) <= 0:
            return

        if not self.txboards[session]:
            if self.currentBoard:
                self.currentBoard.hide()

            self.txboards[session] = TxBoard(session)
            self.currentBoard = self.txboards[session]

        if self.currentBoard and session == self.currentBoard.session:
            if not self.currentBoard.isVisible():
                self.currentBoard.show()
            else:
                self.currentBoard.hide()
        else:
            self.currentBoard.hide()
            self.currentBoard = self.txboards[session]
            self.currentBoard.show()

    def on_UndoButton(self):
        if self.currentBoard:
            self.currentBoard.undo()

    def on_RedoButton(self):
        if self.currentBoard:
            self.currentBoard.redo()

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        print(f"(Main Mouse Position - ({a0.x()}, {a0.y()}))")

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        del self.currentBoard
        del self.txboards
        return super().closeEvent(a0)


if __name__ == '__main__':
    txcore = TxCore(sys.argv)
    txcore.exec()
