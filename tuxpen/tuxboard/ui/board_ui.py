# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'board.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Tuxboard(object):
    def setupUi(self, Tuxboard):
        if not Tuxboard.objectName():
            Tuxboard.setObjectName(u"Tuxboard")
        Tuxboard.resize(640, 480)
        Tuxboard.setCursor(QCursor(Qt.CrossCursor))
        self.verticalLayout = QVBoxLayout(Tuxboard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Tuxboard)
        self.frame.setObjectName(u"frame")
        self.frame.setMouseTracking(True)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Tuxboard)

        QMetaObject.connectSlotsByName(Tuxboard)
    # setupUi

    def retranslateUi(self, Tuxboard):
        Tuxboard.setWindowTitle(QCoreApplication.translate("Tuxboard", u"Form", None))
    # retranslateUi

