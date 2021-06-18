# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_Tuxpen(object):
    def setupUi(self, Tuxpen):
        if not Tuxpen.objectName():
            Tuxpen.setObjectName(u"Tuxpen")
        Tuxpen.resize(983, 524)
        font = QFont()
        font.setFamilies([u"DejaVu Serif"])
        font.setBold(True)
        font.setItalic(True)
        Tuxpen.setFont(font)
        Tuxpen.setMouseTracking(True)
        Tuxpen.setFocusPolicy(Qt.StrongFocus)
        Tuxpen.setAutoFillBackground(True)
        self.centralwidget = QWidget(Tuxpen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMaximumSize(QSize(132, 430))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMaximumSize(QSize(132, 430))
        self.main_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0890511 rgba(47, 47, 47, 255), stop:0.455474 rgba(31, 31, 31, 255));\n"
"border-radius: 7px;")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title = QFrame(self.main_frame)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 16))
        self.title.setStyleSheet(u"background-color: none;")
        self.title.setFrameShape(QFrame.NoFrame)
        self.title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.text = QFrame(self.title)
        self.text.setObjectName(u"text")
        self.text.setFrameShape(QFrame.NoFrame)
        self.text.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.text)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(23, 0, 0, 0)
        self.label = QLabel(self.text)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Inconsolata Expanded Bold"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: none;")

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.text)


        self.verticalLayout.addWidget(self.title)

        self.body = QFrame(self.main_frame)
        self.body.setObjectName(u"body")
        self.body.setMaximumSize(QSize(132, 430))
        self.body.setStyleSheet(u"background-color: none;")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.body)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_pen = QFrame(self.body)
        self.frame_pen.setObjectName(u"frame_pen")
        self.frame_pen.setFrameShape(QFrame.NoFrame)
        self.frame_pen.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_pen)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.button_pen = QPushButton(self.frame_pen)
        self.button_pen.setObjectName(u"button_pen")
        self.button_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_pen.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(62, 62, 62);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/pen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_pen.setIcon(icon)
        self.button_pen.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.button_pen)


        self.verticalLayout_4.addWidget(self.frame_pen)

        self.frame_eraser = QFrame(self.body)
        self.frame_eraser.setObjectName(u"frame_eraser")
        self.frame_eraser.setFrameShape(QFrame.StyledPanel)
        self.frame_eraser.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_eraser)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.button_eraser = QPushButton(self.frame_eraser)
        self.button_eraser.setObjectName(u"button_eraser")
        self.button_eraser.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_eraser.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(62, 62, 62);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_eraser.setIcon(icon1)
        self.button_eraser.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.button_eraser)


        self.verticalLayout_4.addWidget(self.frame_eraser)

        self.frame_undo_redo = QFrame(self.body)
        self.frame_undo_redo.setObjectName(u"frame_undo_redo")
        self.frame_undo_redo.setFrameShape(QFrame.StyledPanel)
        self.frame_undo_redo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_undo_redo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_undo = QFrame(self.frame_undo_redo)
        self.frame_undo.setObjectName(u"frame_undo")
        self.frame_undo.setFrameShape(QFrame.StyledPanel)
        self.frame_undo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_undo)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.button_undo = QPushButton(self.frame_undo)
        self.button_undo.setObjectName(u"button_undo")
        self.button_undo.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_undo.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(62, 62, 62);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_undo.setIcon(icon2)
        self.button_undo.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.button_undo)


        self.horizontalLayout.addWidget(self.frame_undo)

        self.frame_redo = QFrame(self.frame_undo_redo)
        self.frame_redo.setObjectName(u"frame_redo")
        self.frame_redo.setFrameShape(QFrame.StyledPanel)
        self.frame_redo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_redo)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.button_redo = QPushButton(self.frame_redo)
        self.button_redo.setObjectName(u"button_redo")
        self.button_redo.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_redo.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(62, 62, 62);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/redo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_redo.setIcon(icon3)
        self.button_redo.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.button_redo)


        self.horizontalLayout.addWidget(self.frame_redo)


        self.verticalLayout_4.addWidget(self.frame_undo_redo)

        self.frame_clear = QFrame(self.body)
        self.frame_clear.setObjectName(u"frame_clear")
        self.frame_clear.setFrameShape(QFrame.StyledPanel)
        self.frame_clear.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_clear)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_clear = QPushButton(self.frame_clear)
        self.button_clear.setObjectName(u"button_clear")
        self.button_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_clear.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(62, 62, 62);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_clear.setIcon(icon4)
        self.button_clear.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.button_clear)


        self.verticalLayout_4.addWidget(self.frame_clear)

        self.frame_exit = QFrame(self.body)
        self.frame_exit.setObjectName(u"frame_exit")
        self.frame_exit.setFrameShape(QFrame.StyledPanel)
        self.frame_exit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_exit)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.button_exit = QPushButton(self.frame_exit)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_exit.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(62, 62, 62);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_exit.setIcon(icon5)
        self.button_exit.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.button_exit)


        self.verticalLayout_4.addWidget(self.frame_exit)


        self.verticalLayout.addWidget(self.body)

        self.color_box = QFrame(self.main_frame)
        self.color_box.setObjectName(u"color_box")
        self.color_box.setMaximumSize(QSize(16777215, 128))
        self.color_box.setStyleSheet(u"background-color: none;")
        self.color_box.setFrameShape(QFrame.StyledPanel)
        self.color_box.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.color_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 3, 3, 3)
        self.colors = QFrame(self.color_box)
        self.colors.setObjectName(u"colors")
        self.colors.setFrameShape(QFrame.StyledPanel)
        self.colors.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.colors)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.color_white = QPushButton(self.colors)
        self.color_white.setObjectName(u"color_white")
        self.color_white.setMaximumSize(QSize(27, 27))
        self.color_white.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_white.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"	background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 2px;\n"
"}")

        self.gridLayout_2.addWidget(self.color_white, 0, 0, 1, 1)

        self.color_black = QPushButton(self.colors)
        self.color_black.setObjectName(u"color_black")
        self.color_black.setMaximumSize(QSize(27, 27))
        self.color_black.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_black.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"	background-color: rgb(98, 98, 98);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 2px;\n"
"}")

        self.gridLayout_2.addWidget(self.color_black, 0, 1, 1, 1)

        self.color_red = QPushButton(self.colors)
        self.color_red.setObjectName(u"color_red")
        self.color_red.setMaximumSize(QSize(27, 27))
        self.color_red.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_red.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"	background-color: rgb(255, 6, 81);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 2px;\n"
"}")

        self.gridLayout_2.addWidget(self.color_red, 1, 0, 1, 1)

        self.color_green = QPushButton(self.colors)
        self.color_green.setObjectName(u"color_green")
        self.color_green.setMaximumSize(QSize(27, 27))
        self.color_green.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_green.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"	background-color: rgb(75, 213, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 2px;\n"
"}")

        self.gridLayout_2.addWidget(self.color_green, 1, 1, 1, 1)

        self.color_blue = QPushButton(self.colors)
        self.color_blue.setObjectName(u"color_blue")
        self.color_blue.setMaximumSize(QSize(27, 27))
        self.color_blue.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_blue.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"	background-color: rgb(2, 85, 173);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 2px;\n"
"}")

        self.gridLayout_2.addWidget(self.color_blue, 2, 0, 1, 1)

        self.color_yellow = QPushButton(self.colors)
        self.color_yellow.setObjectName(u"color_yellow")
        self.color_yellow.setMaximumSize(QSize(27, 27))
        self.color_yellow.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_yellow.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"	background-color: rgb(255, 226, 5);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 2px;\n"
"}")

        self.gridLayout_2.addWidget(self.color_yellow, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.colors, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.color_box)


        self.horizontalLayout_2.addWidget(self.main_frame)

        Tuxpen.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.button_pen, self.button_eraser)
        QWidget.setTabOrder(self.button_eraser, self.button_clear)
        QWidget.setTabOrder(self.button_clear, self.button_exit)
        QWidget.setTabOrder(self.button_exit, self.color_white)
        QWidget.setTabOrder(self.color_white, self.color_black)
        QWidget.setTabOrder(self.color_black, self.color_red)
        QWidget.setTabOrder(self.color_red, self.color_green)
        QWidget.setTabOrder(self.color_green, self.color_blue)
        QWidget.setTabOrder(self.color_blue, self.color_yellow)

        self.retranslateUi(Tuxpen)

        QMetaObject.connectSlotsByName(Tuxpen)
    # setupUi

    def retranslateUi(self, Tuxpen):
        Tuxpen.setWindowTitle(QCoreApplication.translate("Tuxpen", u"Tuxpen", None))
        self.label.setText(QCoreApplication.translate("Tuxpen", u"Tuxpen", None))
        self.button_pen.setText("")
        self.button_eraser.setText("")
        self.button_undo.setText("")
        self.button_redo.setText("")
        self.button_clear.setText("")
        self.button_exit.setText("")
        self.color_white.setText("")
        self.color_black.setText("")
        self.color_red.setText("")
        self.color_green.setText("")
        self.color_blue.setText("")
        self.color_yellow.setText("")
    # retranslateUi

