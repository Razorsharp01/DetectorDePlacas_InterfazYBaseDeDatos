#conectar interfaz
import os
import sys
import time
from tkinter.filedialog import askopenfile
from interfaz import *
from PySide2 import QtCore
from tkinter import messagebox
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore,QtWidgets
from PySide2.QtCore import QTimer
from PySide2.QtGui import QImage
from PySide2.QtCore import QThread, Signal
import cv2
import numpy as np
import random
import threading
import easyocr
import pytesseract
import pandas as pd
import sqlite3
import datetime
import re
import db
from db import conectar
from hilos import *
class visor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cnn=conectar()
        #Clean title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        #Move window
        self.ui.frame_barra.mouseMoveEvent = self.mover_ventana
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #cerrar
        self.ui.cerrar_bt.clicked.connect(lambda: self.close())

        #actualizar
        self.ui.actualizar_tabla_bt.clicked.connect(lambda: self.rellenar_tabla())
        #iniciar camara
        self.ui.pushButton_5.clicked.connect(self.iniciar_camara)
        #capturar imagen
        self.ui.capturar_bt.clicked.connect(self.capturar_imagen)
        #abrir explorador\
        self.ui.explorar_imagen_bt.clicked.connect(self.abrir_ecplorer)
        #registrar llegada
        self.ui.registra_archivo_bt.clicked.connect(self.insertar_datos_archivo)
        self.ui.registrar_video_placa_bt.clicked.connect(self.insertar_datos_video)
        #pagos
        self.ui.calcular_cobro_bt.clicked.connect(self.calcular_cobro)
        self.ui.pago_hecho_bt.clicked.connect(self.pago_realizado)
    #iniciar camara dentro de un hilo
    def iniciar_camara(self):
        self.hilos=camara_actualizar()
        self.cap=self.hilos.start()
        self.hilos.camara_signal.connect(self.update_frame)

    def update_frame(self,frame):
        self.ui.camara_visual.setPixmap(QPixmap.fromImage(frame))
        self.ui.camara_visual.setScaledContents(True)

    def abrir_ecplorer(self):
        imagen=askopenfile(mode='r',filetypes=[('Image Files', '*.jpg *.png *.jpeg *.bmp')])
        #convertir la imagen a jpg
        img=cv2.imread(imagen.name)
        #crear nombre aleatorio para la imagen
        fecha=datetime.datetime.now()
        fecha1=fecha.strftime('%d-%m-%Y')
        hora=fecha.strftime('%H-%M-%S')
        nombre_aleatorio=str('imagen'+str(fecha1)+str(hora)+'.jpg')
        nueva=cv2.imwrite(nombre_aleatorio,img)
        #extraer ruta de la imagen
        ruta=os.path.abspath(nombre_aleatorio)
        placa=self.placa(ruta)
        self.ui.lcd_archivo_placa.setText(placa)
        self.iniciar_camara()
    #captura imagnen de camara_visual
    def capturar_imagen(self):
        #capturar imagen
        pixmap = self.ui.camara_visual.pixmap()
        fecha=datetime.datetime.now()
        fecha1=fecha.strftime('%d-%m-%Y')
        hora=fecha.strftime('%H-%M-%S')
        nombre_imagen=str('imagen'+str(fecha1)+str(hora)+'.jpg')
        pixmap.save(nombre_imagen)
        #extraer ruta de la imagen
        ruta=os.path.abspath(nombre_imagen)
        placa=self.placa(ruta)
        self.ui.lcd_video_placa.setText(placa)

    def mejorar_iamgen(self, imagen):
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        imagen = cv2.resize(imagen, (640, 480))
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        return imagen

    def placa(self,ruta):
        reader = easyocr.Reader(['es'], gpu=True)
        resultado = reader.readtext(ruta,detail=1,paragraph=False)
        df=pd.DataFrame(resultado,columns=['coordenadas','texto','probabilidad'])
        for i in range(len(df)):
            #usar expresion regular para extraer la placa xxx-xxx-xxx
            placa=re.findall('[A-Z]{3}-[0-9]{3}-[A-Z]{3}',df['texto'][i])
            if len(placa)>0:
                return placa[0]
            elif len(placa)==0:
                #usar expresion regular para extraer la placa xxx-xxx
                placa=re.findall('[A-Z]{3}-[0-9]{3}',df['texto'][i])
                if len(placa)>0:
                    return placa[0]
                elif len(placa)==0:
                    #usar expresion regular para extraer la placa xxx-xx-xx
                    placa=re.findall('[A-Z]{3}-[0-9]{2}-[0-9]{2}',df['texto'][i])
                    if len(placa)>0:
                        return placa[0]
                    elif len(placa)==0:
                        #usar expresion regular para extraer la placa xxx-xxx-x
                        placa=re.findall('[A-Z]{3}-[0-9]{3}-[A-Z]{1}',df['texto'][i])
                        if len(placa)>0:
                            return placa[0]
                        elif len(placa)==0:
                            #usar expresion regular para extraer la placa xx-xxx
                            placa=re.findall('[A-Z]{2}-[0-9]{3}',df['texto'][i])
                            if len(placa)>0:
                                return placa[0]
                            elif len(placa)==0:
                                #usar expresion regular para extraer la placa xx-xx-xxx
                                placa=re.findall('[A-Z]{2}-[0-9]{2}-[0-9]{3}',df['texto'][i])
                                if len(placa)>0:
                                    return placa[0]
                                elif len(placa)==0:
                                    #usar expresion regular para extraer la placa xxx-xxx
                                    placa=re.findall('[0-9]{3}-[A-Z]{3}',df['texto'][i])
                                    if len(placa)>0:
                                        return placa[0]
                                    elif len(placa)==0:
                                        #usar expresion regular para extraer la placa xx-xx
                                        placa=re.findall('[A-Z]{2}-[0-9]{2}',df['texto'][i])
                                        if len(placa)>0:
                                            return placa[0]
                                        elif len(placa)==0:
                                            #usar expresion regular para extraer la placa x-xxx-xxx
                                            placa=re.findall('[A-Z]{1}-[0-9]{3}-[A-Z]{3}',df['texto'][i])
                                            if len(placa)>0:
                                                return placa[0]
        return 'No se encontro placa'
    def insertar_datos_video(self):
        if self.ui.lcd_video_placa.text()=='No se encontro placa':
            QMessageBox.warning(self,'Error','No se encontro placa')
        elif self.ui.lcd_video_placa.text()=='':
            QMessageBox.warning(self,'Error','No hay placas')
        else:
            placa=self.ui.lcd_video_placa.text()
            consulta_placa=self.cnn.verificar_placa(placa)
            if consulta_placa==[]:
                placa=self.ui.lcd_video_placa.text()
                self.placas=placa
                hora1=datetime.datetime.now()
                hora1=hora1.strftime('%H:%M:%S')
                fecha=self.fecha()
                hora2=''
                cobro=''
                pago=0
                print(placa,fecha,hora1,hora2,cobro,pago)
                self.cnn.insertar_datos_video(placa,fecha,hora1,hora2,cobro,pago)
                messagebox.showinfo('Mensaje','Datos insertados correctamente')
                self.ui.lcd_video_placa.setText('')
                self.rellenar_tabla()
            else:
                cobro_placa=self.cnn.pago_consulta(placa)
                if cobro_placa==[]:
                    prueba=self.cnn.volver(placa)
                    if prueba==True:
                        messagebox.showinfo('Mensaje','Debe pagar su estacionamiento')
                        self.ui.lcd_video_placa.setText('')
                        self.rellenar_tabla()
                    else:
                        placa=self.ui.lcd_video_placa.text()
                        self.placas=placa
                        hora1=datetime.datetime.now()
                        hora1=hora1.strftime('%H:%M:%S')
                        fecha=self.fecha()
                        hora2=''
                        cobro=''
                        pago=0
                        #print(placa,fecha,hora1,hora2,cobro,pago)
                        self.cnn.insertar_datos_video(placa,fecha,hora1,hora2,cobro,pago)
                        messagebox.showinfo('Mensaje','Datos dddd insertados correctamente')
                        self.ui.lcd_video_placa.setText('')
                        self.rellenar_tabla()
                else:
                    #print(placa)
                    self.cnn.actualizar_salida(placa)
                    messagebox.showinfo('Mensaje','Puede salir')
                    self.ui.lcd_video_placa.setText('')
                    self.rellenar_tabla()
    def insertar_datos_archivo(self):
        if self.ui.lcd_archivo_placa.text()=='No se encontro placa':
            QMessageBox.warning(self,'Error','No se encontro placa')
        elif self.ui.lcd_archivo_placa.text()=='':
            QMessageBox.warning(self,'Error','No hay placas')
        else:
            placa=self.ui.lcd_archivo_placa.text()
            consulta_placa=self.cnn.verificar_placa(placa)
            if consulta_placa==[]:
                placa=self.ui.lcd_archivo_placa.text()
                self.placas=placa
                hora1=datetime.datetime.now()
                hora1=hora1.strftime('%H:%M:%S')
                fecha=self.fecha()
                hora2=''
                cobro=''
                pago=0
                print(placa,fecha,hora1,hora2,cobro,pago)
                self.cnn.insertar_datos_video(placa,fecha,hora1,hora2,cobro,pago)
                messagebox.showinfo('Mensaje','Datos insertados correctamente')
                self.ui.lcd_archivo_placa.setText('')
                self.rellenar_tabla()
            else:
                cobro_placa=self.cnn.pago_consulta(placa)
                if cobro_placa==[]:
                    prueba=self.cnn.volver(placa)
                    if prueba==True:
                        messagebox.showinfo('Mensaje','Debe pagar su estacionamiento')
                        self.ui.lcd_archivo_placa.setText('')
                        self.rellenar_tabla()
                    else:
                        placa=self.ui.lcd_archivo_placa.text()
                        self.placas=placa
                        hora1=datetime.datetime.now()
                        hora1=hora1.strftime('%H:%M:%S')
                        fecha=self.fecha()
                        hora2=''
                        cobro=''
                        pago=0
                        #print(placa,fecha,hora1,hora2,cobro,pago)
                        self.cnn.insertar_datos_video(placa,fecha,hora1,hora2,cobro,pago)
                        messagebox.showinfo('Mensaje','Datos dddd insertados correctamente')
                        self.ui.lcd_archivo_placa.setText('')
                        self.rellenar_tabla()
                else:
                    #print(placa)
                    self.cnn.actualizar_salida(placa)
                    messagebox.showinfo('Mensaje','Puede salir')
                    self.ui.lcd_archivo_placa.setText('')
                    self.rellenar_tabla()
    def calcular_cobro(self):
        #obtener psoicion de la fila seleccionada
        fila=self.ui.tableWidget.currentRow()
        #obtener el valor de la placa
        placa=self.ui.tableWidget.item(fila,0).text()
        print(placa)
        cobro=self.cnn.cobro(placa)
        if cobro==1:
            messagebox.showinfo('Mensaje','Ya pago')
            self.rellenar_tabla()
        else:
            messagebox.showinfo('Mensaje','Se actualizo el cobro')
            self.rellenar_tabla()

    def mover_menu(self):
        if True:
            width = self.ui.frame_lateral.width()
            normal = 0
            if width==0:
                extender = 250
            else:
                extender= normal
            self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
            self.animacion.setDuration (300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve (QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    ## Sizegrip
    def rellenar_tabla(self):
        datos=self.cnn.rellenar_tabla()
        i=len(datos)
        tablerow=0
        self.ui.tableWidget.setRowCount(i)
        for row in datos:
            self.Id=row[0]
            self.ui.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[5])))
            self.ui.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(str(row[6])))
            tablerow+=1
    def pago_realizado(self):
        fila=self.ui.tableWidget.currentRow()
        placa=self.ui.tableWidget.item(fila,0).text()
        self.cnn.actualizar_pago(placa)
        messagebox.showinfo('Mensaje','Pago realizado correctamente')
        self.rellenar_tabla()
    def registrar_llegada(self):
        conexion=sqlite3.connect('parking.db')
        hllegada=self.hora_llegada()
        fecha=self.fecha()
        cursor=conexion.cursor()

    def hora_llegada(self):
        hllegada=datetime.datetime.now()
        hllegada=hllegada.strftime('%H:%M:%S')
        return hllegada

    def hora_salida(self):
        hsalida=datetime.datetime.now()
        hsalida=hsalida.strftime('%H:%M:%S')
        return hsalida
    
    def fecha(self):
        fecha=datetime.date.today()
        fecha=str(fecha)
        return fecha

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    ## window move
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos () + event.globalPos () - self.clickPosition)
                self.clickPosition = event.globalPos ()
                event.accept()

        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()
    

if __name__=="__main__":
    Mapp = QApplication(sys.argv)
    app = visor()
    app.show()
    sys.exit(Mapp.exec_())