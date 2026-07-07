# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(818, 735)
        Widget.setMinimumSize(QSize(818, 0))
        Widget.setMaximumSize(QSize(818, 16777215))
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 130, 721, 481))
        self.layout = QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.Save_File = QPushButton(Widget)
        self.Save_File.setObjectName(u"Save_File")
        self.Save_File.setGeometry(QRect(80, 10, 61, 24))
        self.Open_File = QPushButton(Widget)
        self.Open_File.setObjectName(u"Open_File")
        self.Open_File.setGeometry(QRect(9, 9, 61, 24))
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(90, 640, 701, 71))
        self.stack_box = QComboBox(Widget)
        self.stack_box.addItem("")
        self.stack_box.addItem("")
        self.stack_box.setObjectName(u"stack_box")
        self.stack_box.setGeometry(QRect(150, 10, 111, 24))
        self.filterButton = QPushButton(Widget)
        self.filterButton.setObjectName(u"filterButton")
        self.filterButton.setGeometry(QRect(10, 40, 131, 24))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.Save_File.setText(QCoreApplication.translate("Widget", u"Save File", None))
        self.Open_File.setText(QCoreApplication.translate("Widget", u"Open File", None))
        self.stack_box.setItemText(0, QCoreApplication.translate("Widget", u"non-stack chart", None))
        self.stack_box.setItemText(1, QCoreApplication.translate("Widget", u"stack chart", None))

        self.filterButton.setText(QCoreApplication.translate("Widget", u"Savitzky-Golay filter", None))
    # retranslateUi

