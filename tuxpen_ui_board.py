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


class Ui_TuxpenBoard(object):
    def setupUi(self, TuxpenBoard):
        if not TuxpenBoard.objectName():
            TuxpenBoard.setObjectName(u"TuxpenBoard")
        TuxpenBoard.resize(640, 480)
        self.verticalLayout = QVBoxLayout(TuxpenBoard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(TuxpenBoard)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(TuxpenBoard)

        QMetaObject.connectSlotsByName(TuxpenBoard)
    # setupUi

    def retranslateUi(self, TuxpenBoard):
        TuxpenBoard.setWindowTitle(QCoreApplication.translate("TuxpenBoard", u"Form", None))
    # retranslateUi

