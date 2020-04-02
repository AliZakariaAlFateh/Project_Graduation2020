# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 2018

@author: Ashish Kumar
"""

import tkinter as tk
from tkinter import Message, Text
import cv2, os
import shutil
import csv
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

window = Tk()
# helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Face_Recogniser")
window.geometry("700x430");
# dialog_title = 'QUIT'
# dialog_text = 'Are you sure?'
# answer = messagebox.askquestion(dialog_title, dialog_text)

# window.geometry('1280x720')
window.configure(background='blue')

message = Label(window, text="Face-Recognition-Based-Attendance-Management-System", bg="Green", fg="white", width=50,height=3, font=('times', 30, 'italic bold underline'))

message.place(x=200, y=20)
txt = Entry(window, width=20, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt.place(x=0, y=115)
txt2 = Entry(window, width=20, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt2.place(x=0, y=150)

def clear():
    txt.delete(0, 'end')
    txt2.delete(0, 'end')


def clear2():
    txt2.delete(0, 'end')
clearButton = Button(window, text="Clear", command=clear, fg="red", bg="yellow", width=20, height=1, activebackground="Red", font=('times', 15, ' bold '))
clearButton.place(x=250, y=115)
clearButton2 = Button(window, text="Clear", command=clear2, fg="red", bg="yellow", width=20, height=1,activebackground="Red", font=('times', 15, ' bold '))
clearButton2.place(x=250, y=150)



window.mainloop()