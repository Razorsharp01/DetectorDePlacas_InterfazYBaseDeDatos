from pprint import pprint
import numpy as np
import pandas as pd
import sqlite3
import datetime
import re

class conectar():
    def __init__(self):
        self.connect=sqlite3.connect('parking.db')
    
    def insertar_datos_archivo(self,placa,fecha,hora,horasal,cobro,pago):
        cursor=self.connect.cursor()
        db='''INSERT INTO placas (Placa,Fecha,Horaentrada,Horasalida,Cobro,Pago,Entrada,Salida) VALUES(?,?,?,?,?,?,?,?)'''
        cursor.execute(db,(placa,fecha,hora,horasal,cobro,pago,1,0))
        self.connect.commit()
        cursor.close()
    def insertar_datos_video(self,placa,fecha,hora,horasal,cobro,pago):
        cursor=self.connect.cursor()
        db='''INSERT INTO placas (Placa,Fecha,Horaentrada,Horasalida,Cobro,Pago,Entrada,Salida) VALUES(?,?,?,?,?,?,?,?)'''
        cursor.execute(db,(placa,fecha,hora,horasal,cobro,pago,1,0))
        self.connect.commit()
        cursor.close()
    def rellenar_tabla(self):
        cursor=self.connect.cursor()
        fecha=str(datetime.date.today())
        bd="SELECT * FROM placas WHERE Fecha='{}'".format(fecha)
        cursor.execute(bd)
        datos=cursor.fetchall()
        return datos
    def pago_consulta(self,placa):
        fecha=str(datetime.date.today())
        cursor=self.connect.cursor()
        pago="SELECT * FROM placas WHERE Placa='{}' AND Fecha='{}' AND Pago='1' AND Salida='0'".format(placa,fecha)
        cursor.execute(pago)
        datos=cursor.fetchall()
        return datos
    def volver(self,placa):
        fecha=str(datetime.date.today())
        cursor=self.connect.cursor()
        consulta="SELECT * FROM placas WHERE Placa='{}' AND Fecha='{}'".format(placa,fecha)
        cursor.execute(consulta)
        datos=cursor.fetchall()
        panda=pd.DataFrame(datos)
        print('Datos de la placa: ',placa)
        print(panda)
        #tomar el ultimo elemento del dataframe
        ultimo=panda.iloc[-1]
        print(ultimo)
        if ultimo[6]==0:
            return True
        else:
            return False
    def actualizar_salida(self,placa):
        cursor=self.connect.cursor()
        ids=self.verificar_id_pagado(placa)
        print(ids)
        pago="UPDATE placas SET Salida='1' WHERE ID='{}'".format(ids)
        cursor.execute(pago)
        self.connect.commit()
        cursor.close()
    def cobro(self,placa):
        fecha=str(datetime.date.today())
        cursor=self.connect.cursor()
        pagp=self.pago_consulta(placa)
        #si pago esta vacio se cobrara
        if pagp==[]:
            hsalida=datetime.datetime.now()
            hsalida=hsalida.strftime('%H:%M:%S')
            #extraer hora de entrada
            ids=self.verificar_id(placa)
            #print(ids)
            hora="SELECT * FROM placas WHERE ID='{}'".format(ids)
            cursor.execute(hora)
            datos=cursor.fetchall()
            #print(datos)
            hentrada=datos[0][3]
            #calcular cobro
            hentrada1=datetime.datetime.strptime(hentrada,'%H:%M:%S')
            hsalida1=datetime.datetime.strptime(hsalida,'%H:%M:%S')
            cobro=hsalida1-hentrada1
            #print(cobro)
            cobro=str(cobro)
            cobro=cobro.split(':')
            cobro=cobro[0]
            cobro=int(cobro)
            cobro=cobro*15
            cobro=str(cobro)
            #actualizar hora de salida
            horasalidae="UPDATE placas SET Horasalida='{}' WHERE ID='{}'".format(hsalida,ids)
            cursor.execute(horasalidae)
            self.connect.commit()
            #actualizar cobro
            cobro="UPDATE placas SET Cobro='{}' WHERE Id='{}'".format(cobro,ids)
            cursor.execute(cobro)
            self.connect.commit()
            cursor.close()
        else:
            return 1
    def entra(self,placa):
        fecha=str(datetime.date.today())
        hora=datetime.datetime.now()
        hora=hora.strftime('%H:%M:%S')
        cursor=self.connect.cursor()
        va_entro=33

    def verificar_placa(self,placa):
        cursor=self.connect.cursor()
        fecha=str(datetime.date.today())
        placa="SELECT * FROM placas WHERE Placa='{}' AND Fecha='{}' AND Salida='0'".format(placa,fecha)
        cursor.execute(placa)
        datos=cursor.fetchall()
        return datos

    def verificar_id(self,placa):
        cursor=self.connect.cursor()
        fecha=str(datetime.date.today())
        pago=0
        placa="SELECT * FROM placas WHERE Placa='{}' AND Fecha='{}' AND Pago='{}' AND Salida='0'".format(placa,fecha,pago)
        cursor.execute(placa)
        datos=cursor.fetchall()
        pprint(datos)
        #extraer id
        if datos!=[]:
            id_placa=datos[0][0]
            return id_placa
        else:
            return 0
    def verificar_id_pagado(self,placa):
        cursor=self.connect.cursor()
        fecha=str(datetime.date.today())
        pago=1
        placa="SELECT * FROM placas WHERE Placa='{}' AND Fecha='{}' AND Pago='{}' AND Salida='0'".format(placa,fecha,pago)
        cursor.execute(placa)
        datos=cursor.fetchall()
        #pprint(datos)
        #extraer id
        if datos!=[]:
            id_placa=datos[0][0]
            return id_placa
        else:
            return 0
    def actualizar_pago(self,placa):
        cursor=self.connect.cursor()
        ids=self.verificar_id(placa)
        pago="UPDATE placas SET Pago='1' WHERE ID='{}'".format(ids)
        cursor.execute(pago)
        self.connect.commit()
        cursor.close()