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
from conect import visor

class camara_actualizar(QThread):
    camara_signal=Signal(QImage)
    def run(self):
        cap=cv2.VideoCapture(0)
        while True:
            ret,frame=cap.read()
            if ret:
                frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                height,width,channel=frame.shape
                step=channel*width
                qImg=QImage(frame.data,width,height,step,QImage.Format_RGB888)
                self.camara_signal.emit(qImg)
            else:
                break