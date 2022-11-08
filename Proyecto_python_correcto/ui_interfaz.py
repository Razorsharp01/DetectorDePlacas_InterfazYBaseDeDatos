# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazFjpzJH.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1156, 771)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 20, 1161, 751))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setIconSize(QSize(16, 16))
        self.visor_page = QWidget()
        self.visor_page.setObjectName(u"visor_page")
        self.visor_page.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"font: 100 12pt\"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(181, 217, 227);\n"
"border-radius:15px;\n"
"color: rgb(0, 0, 127);\n"
"font:100 12pt\"Arial Black\";\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(237, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border:0px;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"font:80 16pt \"Arial Black\";\n"
"}")
        self.camara_visual = QLabel(self.visor_page)
        self.camara_visual.setObjectName(u"camara_visual")
        self.camara_visual.setGeometry(QRect(10, 120, 500, 350))
        self.camara_visual.setMinimumSize(QSize(500, 350))
        self.camara_visual.setMaximumSize(QSize(500, 350))
        self.camara_visual.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.registrar_video_placa_bt = QPushButton(self.visor_page)
        self.registrar_video_placa_bt.setObjectName(u"registrar_video_placa_bt")
        self.registrar_video_placa_bt.setGeometry(QRect(790, 280, 150, 40))
        self.registrar_video_placa_bt.setMinimumSize(QSize(150, 40))
        self.registrar_video_placa_bt.setMaximumSize(QSize(150, 40))
        self.apagar_bt = QPushButton(self.visor_page)
        self.apagar_bt.setObjectName(u"apagar_bt")
        self.apagar_bt.setGeometry(QRect(260, 490, 150, 40))
        self.apagar_bt.setMinimumSize(QSize(150, 40))
        self.apagar_bt.setMaximumSize(QSize(150, 40))
        self.registra_archivo_bt = QPushButton(self.visor_page)
        self.registra_archivo_bt.setObjectName(u"registra_archivo_bt")
        self.registra_archivo_bt.setGeometry(QRect(820, 650, 150, 40))
        self.registra_archivo_bt.setMinimumSize(QSize(150, 40))
        self.registra_archivo_bt.setMaximumSize(QSize(150, 40))
        self.label_2 = QLabel(self.visor_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 10, 361, 81))
        self.explorar_imagen_bt = QPushButton(self.visor_page)
        self.explorar_imagen_bt.setObjectName(u"explorar_imagen_bt")
        self.explorar_imagen_bt.setGeometry(QRect(700, 410, 350, 40))
        self.explorar_imagen_bt.setMinimumSize(QSize(350, 40))
        self.explorar_imagen_bt.setMaximumSize(QSize(350, 40))
        self.pushButton_5 = QPushButton(self.visor_page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(80, 490, 150, 40))
        self.pushButton_5.setMinimumSize(QSize(150, 40))
        self.pushButton_5.setMaximumSize(QSize(150, 40))
        self.label_4 = QLabel(self.visor_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(720, 120, 301, 51))
        self.label_5 = QLabel(self.visor_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(720, 460, 301, 51))
        self.lcd_video_placa = QLineEdit(self.visor_page)
        self.lcd_video_placa.setObjectName(u"lcd_video_placa")
        self.lcd_video_placa.setGeometry(QRect(620, 170, 500, 100))
        self.lcd_video_placa.setMinimumSize(QSize(350, 100))
        self.lcd_video_placa.setMaximumSize(QSize(16777215, 100))
        self.lcd_archivo_placa = QLineEdit(self.visor_page)
        self.lcd_archivo_placa.setObjectName(u"lcd_archivo_placa")
        self.lcd_archivo_placa.setGeometry(QRect(630, 510, 500, 100))
        self.lcd_archivo_placa.setMinimumSize(QSize(350, 100))
        self.lcd_archivo_placa.setMaximumSize(QSize(16777215, 100))
        self.tabWidget.addTab(self.visor_page, "")
        self.camara_visual.raise_()
        self.apagar_bt.raise_()
        self.registra_archivo_bt.raise_()
        self.registrar_video_placa_bt.raise_()
        self.label_2.raise_()
        self.explorar_imagen_bt.raise_()
        self.pushButton_5.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lcd_video_placa.raise_()
        self.lcd_archivo_placa.raise_()
        self.base_page = QWidget()
        self.base_page.setObjectName(u"base_page")
        self.base_page.setStyleSheet(u"QTableWidget{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);\n"
"gridline-color:rgb(0,0,0);\n"
"font-size:12pt;\n"
"color:#000000;\n"
" }\n"
"\n"
"QHeaderView::section{\n"
"background-color:rgb(255,255,255);\n"
"border:1px solid rgb(0,0,0);\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton :: section{\n"
"background-color:rgb(0,0,0);\n"
"border:1px solid rgb(0,206,151);\n"
"}")
        self.label_3 = QLabel(self.base_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 0, 281, 91))
        self.tableWidget = QTableWidget(self.base_page)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 120, 1071, 381))
        self.tabWidget.addTab(self.base_page, "")
        self.cerrar_bt = QPushButton(self.centralwidget)
        self.cerrar_bt.setObjectName(u"cerrar_bt")
        self.cerrar_bt.setGeometry(QRect(1110, 0, 40, 40))
        self.cerrar_bt.setMinimumSize(QSize(40, 40))
        self.cerrar_bt.setMaximumSize(QSize(40, 40))
        self.cerrar_bt.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"font: 100 12pt\"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(234, 0, 0);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"font:100 12pt\"Arial Black\";\n"
"}\n"
"")
        self.cerrar_bt.setIconSize(QSize(13, 16))
        self.frame_barra = QFrame(self.centralwidget)
        self.frame_barra.setObjectName(u"frame_barra")
        self.frame_barra.setGeometry(QRect(0, 0, 1161, 41))
        self.frame_barra.setFrameShape(QFrame.StyledPanel)
        self.frame_barra.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_barra.raise_()
        self.tabWidget.raise_()
        self.cerrar_bt.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.camara_visual.setText("")
        self.registrar_video_placa_bt.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.apagar_bt.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.registra_archivo_bt.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Visor de placas</span></p></body></html>", None))
        self.explorar_imagen_bt.setText(QCoreApplication.translate("MainWindow", u"Abrir explorador de archivos", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Encender", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">N\u00famero de placa</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">N\u00famero de placa</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visor_page), QCoreApplication.translate("MainWindow", u"Visor de placas", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Base de datos</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Placa", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hora de entrada", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Hora de salida", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Monto de cobro", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Pago", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.base_page), QCoreApplication.translate("MainWindow", u"Base de datos", None))
        self.cerrar_bt.setText(QCoreApplication.translate("MainWindow", u"x", None))
    # retranslateUi

