from PySide6 import QtWidgets, QtCore

from tuxcore import tuxcore
from tuxboard import tuxboard


class TuxManager:
    def __init__(self, app):
        self.__app = app
        self.__monitorWidth = self.app.primaryScreen().availableGeometry().width()
        self.__monitorHeight = self.app.primaryScreen().availableGeometry().height()

        self.__coreWindow = tuxcore.TuxCore(self)
        self.__boardWindow = tuxboard.TuxBoard(self)

    @property
    def app(self) -> QtWidgets.QApplication:
        return self.__app

    @property
    def monitorWidth(self):
        return self.__monitorWidth

    @property
    def monitorHeight(self):
        return self.__monitorHeight

    @property
    def coreWindow(self):
        return self.__coreWindow

    @property
    def boardWindow(self):
        return self.__boardWindow
