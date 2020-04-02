import cv2,os
from tkinter import *
from tkinter import messagebox
from tkinter import font
# import pyQt4
# import face_recognition
import numpy as nnn
# import pickle
# import dlib
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
# import pandas as pd
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar

class GenerateDataSetClass():
    def show_frame(self):
        root=Tk()
        root.geometry("800x450");
        root.title("New Window By Object Oiented")
        root.resizable(width=False, height=False)
        image = PhotoImage(file="BackGroundImages/register9.png")
        c = Canvas(root, bg='green')
        c.pack(fill=BOTH, expand=1)
        c.create_image(0, 0, image=image, anchor=NW)
##########################################################    select box for level     ##################################
        global SelectLevel
        SelectLevel = StringVar(root)
        # Dictionary with options
        choices = {1, 2, 3, 4}
        SelectLevel.set('Select_Level')  # set the default option
        popupMenu = OptionMenu(root, SelectLevel, *choices)
        # Label(Controlwindow, text="Choose a level").place(x=100, y=100)
        popupMenu.place(x=250, y=200)


####################################      clear all fields    ##################################################
        def clear():
            Entry_Name.delete(0, 'end')
            Entry_Id.delete(0, 'end')
            Entry_Email.delete(0, 'end')


#############################           to check if id is numeric or no                 ##############################
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                pass

            try:
                import unicodedata
                unicodedata.numeric(s)
                return True
            except (TypeError, ValueError):
                pass

            return False
        global SubmitAfterTakePhoto
        SubmitAfterTakePhoto=True
        global flage_take_image_pre_train
        flage_take_image_pre_train=False
        global flage_Training
        global flage_take_image_pre_submit
        flage_take_image_pre_submit=False
        flage_Training= "no"
        var_name_1 = StringVar()
        var_id_2 = StringVar()
        var_level_3 = StringVar()
        var_email_4 = StringVar()
        ################## Generate PPhotos    ##############
        def GenerateDataSet():
            level = SelectLevel.get()
            if os.path.exists("Data_Set" + level):
                if os.path.exists("haarcascade_frontalface_default.xml"):
                    global SubmitAfterTakePhoto
                    flage=1
                    in1 = var_name_1.get()
                    # level = var_level_3.get()
                    id=var_id_2.get()
                    email=var_email_4.get()
                    _email=Check_Email(email)
                    if in1=='':
                        flage=0
                    if SelectLevel.get() == 'Select_Level':
                        messagebox.showinfo("message", "You must select the level .")
                        return
                    if(email==''):
                        flage=0
                    if flage==0:
                        messagebox.showinfo("Inputs","you must fill all top fields")
                        return
                    if is_number(id)==False:
                         flage=0
                         messagebox.showinfo("Inputs", "you must Enter only numbers in id field")
                         return
                    if(_email==False):
                        messagebox.showinfo("Inputs", "Your email not valid ,\n please enter a valid email")
                        return
                    # we want to check about id if found make return with a meaasge else continoue to take a photo.
                    else:
                        if SubmitAfterTakePhoto==False:
                            messagebox.showinfo("Inputs", "you must do submit .")
                            return
                        else:
                            level = SelectLevel.get()
                            global flage_take_image_pre_submit
                            flage_take_image_pre_submit = True
                            global flage_take_image_pre_train
                            flage_take_image_pre_train = True
                            faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
                            cam = cv2.VideoCapture(0)
                            samplnum = 0
                            while (True):
                                ret, img = cam.read()
                                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                faces = faceDetect.detectMultiScale(gray, 1.3, 5);
                                for (x, y, w, h) in faces:
                                    samplnum = samplnum + 1
                                    cv2.imwrite("Data_Set" + level + "/" + in1 + "." + id + '.' + str(samplnum) + ".jpg",
                                                gray[y:y + h, x:x + w])
                                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                    cv2.waitKey(100)
                                cv2.imshow("Generate Photos.", img)
                                cv2.waitKey(1)
                                if (samplnum == 100):
                                    break;

                            cam.release();
                            cv2.destroyAllWindows();
                            SubmitAfterTakePhoto = False
                            messagebox.showinfo("message for helping", "Please do not delete or change the data,\n as this will lead to a failure to identify you later.")
                else:
                    messagebox.showerror("error","the file haarcascade_frontalface_default.xml not exists ,\nPlease bring this file to MyProject directory ,\n to generate photos")
            else:
                messagebox.showinfo("message","The Data_Set"+level+" Is created Now .")
                os.mkdir("Data_Set" + level)
                messagebox.showinfo("message", "The directory created is done , please take photos again ")
                return
        def welcom():
            in1 = var_name_1.get()
            in2 = var_id_2.get()
            in3 = var_level_3.get()
            in4 = var_email_4.get()
            messagebox.showinfo("Inputs", "user name : " + in1+"\n"+"ID : "+in2+"\n"+"level : "+in3+"\n"+"email : "+in4)


##############################################        to check about email          ###########################################
        def Check_Email(email):
            x=re.findall('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>)',email)
            if x:
                return True
            else:
                return False


##########################################         to make training         ###############################################

        def trainimages():
            import FinalProject_Training
            global flage_Training
            global flage_take_image_pre_train
            if SelectLevel.get() == 'Select_Level':
                messagebox.showinfo("message", "You must select the level .")
                return
            if flage_take_image_pre_train == True:
                pb.start(10)
                messagebox.showinfo("Inputs", "please, press ok and waite for seconds \n, until anew message appear.")
                flage_take_image_pre_train=False
                level=SelectLevel.get()
                St_ID = var_id_2.get()
                Name=var_name_1.get()
                FinalProject_Training.TrainingPhotosClass().TrainingPhotos(St_ID,level,Name)
                messagebox.showinfo("Inputs", " Now you can make submit , please press ok.")
                flage_Training = "okey"
                pb.stop()
                return
            else:
                messagebox.showinfo("Inputs"," You must take image .")
                return
##############################################              to make submit             ########################################
        def onsubmtting():
            global SubmitAfterTakePhoto
            global flage_Training
            global flage_take_image_pre_submit
            global flage_take_image_pre_train
            a=flage_Training
            if(a == "okey"):
                flage_take_image_pre_submit=False
                flage_Training = "no"
                messagebox.showinfo("message","ok you acctually train images ,\n and your data is registered ")
                SubmitAfterTakePhoto = True
                return
            else:
                messagebox.showinfo("message","you cant submit without taining images , \n please press train images button")
                return
################################################        back to home        #############################################
        def BackToHomePage():
            root.destroy()
            import FinalProject_Main
################################################      buttons and entries     ################################################
        pb = Progressbar(root, orient="horizontal", length=200, mode="determinate", maximum=100)
        pb.place(x=550, y=380)
        Clear_Fields = Button(root, text="Clear all fields", fg="white", bg="red", font="15", border=5,width=40, activebackground="blue", command=clear).place(x=200, y=20)
        Label_Name = Label(root, text="Please,Enter name: ", bg="yellow", relief="solid", fg="green",font=("arial", 12, "bold"), width="20", height="2").place(x=0, y=90)
        Label_Id = Label(root, text="Please,Enter Id: ", bg="yellow", relief="solid", fg="green",font=("arial", 12, "bold"), width="20", height="2").place(x=0, y=140)
        Label_Level = Label(root, text="Please,Enter Level: ", bg="yellow", relief="solid", fg="green",font=("arial", 12, "bold"), width="20", height="2").place(x=0, y=190)
        Label_Email = Label(root, text="Please,Enter Email: ", bg="yellow", relief="solid", fg="green",font=("arial", 12, "bold"), width="20", height="2").place(x=0, y=240)
        Entry_Name = Entry(root, textvariable=var_name_1, width="50", justify=CENTER,bd=5,font=("arial", 15, "bold"))
        Entry_Name.place(x=250, y=93)
        Entry_Id = Entry(root, textvariable=var_id_2, width="50", justify=CENTER,bd=5,font=("arial", 15, "bold"))
        Entry_Id.place(x=250, y=145)
        # Entry_Level = Entry(root, textvariable=var_level_3, width="50", justify=CENTER,bd=2)
        # Entry_Level.place(x=250, y=173)
        Entry_Email = Entry(root, textvariable=var_email_4, width="50", justify=CENTER,bd=5,font=("arial", 15, "bold"))
        Entry_Email.place(x=250, y=245)
        Label_Take_Photo = Label(root, text="You must take a photo before submitting", bg="yellow",relief="solid", fg="green", font=("arial", 12, "bold"), width="33", height="2").place(x=0, y=310)
        but_Take_Photo = Button(root, text="Take_Photo", fg="white", bg="red", font="15", border=5,width=15, activebackground="blue", command=GenerateDataSet).place(x=350, y=315)
        Imagetraining = Button(root, text="Train_Images", fg="white", bg="red", font="15", border=5,width=15, activebackground="blue",command=trainimages).place(x=550, y=315)
        but_Submit = Button(root, text="Submit", fg="white", bg="red", font="15", border=5, width=15,activebackground="blue",command=onsubmtting).place(x=350, y=360)
        HomePage_but = Button(root, text="Back to home page", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue", command=BackToHomePage).place(x=170, y=360)
        but_Close = Button(root, text="Close", fg="white", bg="red", font="15", border=5, width=40,activebackground="blue", relief=GROOVE, bd=5, command=root.destroy)
        but_Close.place(x=200, y=410)

        root.mainloop()
# GenerateDataSetClass().show_frame()

