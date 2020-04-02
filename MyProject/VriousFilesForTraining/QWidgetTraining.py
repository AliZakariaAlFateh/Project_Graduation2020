import cv2,os
from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import Image
from tkinter import messagebox,filedialog
# import pyQt4
import numpy as nnn
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
import tkinter as tk
from tkinter import ttk
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox,QApplication,QPushButton,QVBoxLayout
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
# a=QApplication(sys.argv)
# Controlwindow=QWidget()
# Controlwindow.setAutoFillBackground(True)
# p=Controlwindow.palette()
# p.setColor(Controlwindow.backgroundRole(),Qt.blue)
# Controlwindow.setPalette(p)
# p1=QPushButton('hello',Controlwindow)
# Controlwindow.show()
app = QApplication([])
window = QWidget()
window.setFixedSize(500,500)
# window.setGeometry(10,10,500,500)
# window.QSize(640, 140)
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
# b=QPushButton("kljjk",window).setGeometry(5,80,90,90)
b=QPushButton("kljjk",window)
b.move(20,100)
c=QComboBox(window)
c.addItem("hfhfh")
c.addItem("mfnnfn")
c.addItem("yruru")
window.show()
app.exec_()