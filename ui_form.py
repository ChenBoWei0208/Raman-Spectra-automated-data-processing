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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.Open_File = QPushButton(Widget)
        self.Open_File.setObjectName(u"Open_File")
        self.Open_File.setGeometry(QRect(230, 220, 80, 24))
        self.view = QTextEdit(Widget)
        self.view.setObjectName(u"view")
        self.view.setGeometry(QRect(340, 150, 291, 201))
        self.Save_File = QPushButton(Widget)
        self.Save_File.setObjectName(u"Save_File")
        self.Save_File.setGeometry(QRect(230, 280, 80, 24))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.Open_File.setText(QCoreApplication.translate("Widget", u"Open File", None))
        self.Save_File.setText(QCoreApplication.translate("Widget", u"Save File", None))
    # retranslateUi

