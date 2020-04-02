import cv2,os
from tkinter import *
from tkinter import messagebox
from tkinter import font
# import pyQt4
# import face_recognition
import numpy as nnn
import pickle
import dlib
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter as tk
from tkinter import Message, Text
import shutil
import csv
import re
from PIL import Image, ImageTk
import pandas as pd
import validate_utf8
import utf8tobibtex
import utf8config
import utf8cleaner
class FaceRcognitionClass():
    def Recognition_Faces(self,level,subject):
        if os.path.exists("TrainingImageLabel"):
            if os.path.exists("haarcascade_frontalface_default.xml"):
                if os.path.exists("TrainingImageLabel\Trainner"+level+".yml"):
                    FileSizeOfTraining= os.path.getsize("TrainingImageLabel\Trainner"+level+".yml")
                    if(FileSizeOfTraining==0):
                        messagebox.showerror("error","The file"+"Trainner"+level+" "+"has no data to check ,\n Please change the level .")
                        return
                    else:
                        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
                        recognizer.read("TrainingImageLabel\Trainner"+level+".yml")
                        harcascadePath = "haarcascade_frontalface_default.xml"
                        faceCascade = cv2.CascadeClassifier(harcascadePath);
                        cam = cv2.VideoCapture(0)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        col_names = ['Id', 'Name', 'Date', 'Time','Course']
                        attendance = pd.DataFrame(columns=col_names)
                        while True:
                            ret, im = cam.read()
                            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                            for (x, y, w, h) in faces:
                                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                                if (conf < 50):
                                    if (Id==1111):
                                        name="ALi_Al_Fateh"
                                        ts = time.time()
                                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                                        attendance.loc[len(attendance)] = [Id, name, date, timeStamp,subject]
                                    elif(Id==2222):
                                         name="Abu_Ali"
                                         ts = time.time()
                                         date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                                         timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                                         attendance.loc[len(attendance)] = [Id, name, date, timeStamp,subject]
                                    elif(Id==3333):
                                        name = "El_Magico"
                                        ts = time.time()
                                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                                        attendance.loc[len(attendance)] = [Id, name, date, timeStamp,subject]

                                    elif(Id==5555):
                                        name = "Ahmed_Saad"
                                        ts = time.time()
                                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                                        attendance.loc[len(attendance)] = [Id, name, date, timeStamp,subject]


                                else:
                                    name = 'Unknown'
                                # if (conf > 75):
                                    # noOfFile = len(os.listdir("ImagesUnknown")) + 1
                                    # cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                                cv2.putText(im, str(name), (x, y + h), font, 1, (250, 250, 250), 2)
                            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
                            cv2.imshow('im', im)
                            if (cv2.waitKey(1) == ord('q')):
                                break
                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        Hour, Minute, Second = timeStamp.split(":")
                        fileName = "Attendance\Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second +"_"+subject+ ".csv"
                        attendance.to_csv(fileName, index=False)
                        cam.release()
                        cv2.destroyAllWindows()
                else:
                    messagebox.showerror("error","the file "+" Trainner"+level+".yml not exists ,\nPlease create that file in TrainingImageLabel directory in MyProject directory . ")
                    return
            else:
                messagebox.showerror("error", "the file haarcascade_frontalface_default.xml not exists ,\nPlease bring this file to MyProject directory ,\n to generate photos")
                return
        else:
            os.mkdir("TrainingImageLabel")
            messagebox.showinfo("message","The directory TrainingImageLabel  is created now,\n please take a photo again and make training for it")
            return
# FaceDetectionClass().Recognition_Faces()
