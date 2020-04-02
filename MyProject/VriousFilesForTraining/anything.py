# import cv2
# import mysql.connector
# # import face_recognition
# # import face_recognition
# from tkinter import *
# from tkinter import messagebox
# from tkinter import font
# # import pyQt4
# # import face_recognition
# import numpy as nnn
# from PIL import Image
# # import face_recognition.api
# import pickle
# root =Tk()
# root.geometry("700x430");
# root.title("New Window By Object Oiented")
# image = PhotoImage(file="register9.png")
# c = Canvas(root, bg='green')
# c.pack(fill=BOTH, expand=1)
# c.create_image(0, 0, image=image, anchor=NW)
#
# _flage="no"
# def trainimages():
#     global _flage
#     _flage = "okey"
#
#
# def onsubmtting():
#     global _flage
#     a = _flage
#     # name=Entry_Name.get()
#     if (a == "okey"):
#         messagebox.showinfo("ok you acctually train "+name)
#     else:
#         messagebox.showinfo("you cant submit without taining image ")
#     #     return
#     # flage="no"
#     # messagebox.showinfo("images you must press key of train images")
#
# Entry_Name = Entry(root, width="50", justify=CENTER,bd=2).place(x=250, y=93)
# Entry_Id = Entry(root, width="50", justify=CENTER,bd=2).place(x=250, y=133)
# f=0
#
# def ff():
#     global f
#     f=1
# ff()
# if(f==1):
#     print("okey")
# else:
#     print("no")
#
# Imagetraining = Button(root, text="ImageTraining", fg="white", bg="red", font="15", border=5, width=15,activebackground="blue", command=trainimages).place(x=550, y=295)
# but_Submit = Button(root, text="Submit", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue",command=onsubmtting).place(x=350, y=350)
#
# root.mainloop()
# # s="ktkkkk"
# # print(len(s))
###############################    another code    ###################################
# from tkinter import *
# import tkinter as ttk
#
#
# root = Tk()
# root.title("Tk dropdown example")
# root.resizable(width=False,height=False)
# root.geometry("500x430");
# # Add a grid
# # mainframe = Frame(root)
# # mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
# # mainframe.columnconfigure(0, weight = 1)
# # mainframe.rowconfigure(0, weight = 1)
# # #for resize the window
# # mainframe.pack(pady = 100, padx = 100)
#
# # Create a Tkinter variable
# tkvar = StringVar(root)
#
# # Dictionary with options
# choices = { 'C++','Php','C#','Java','fortrn','Python'}
# tkvar.set('Select_Subject') # set the default option
#
# popupMenu = OptionMenu(root, tkvar, *choices)
# # Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
# Label(root, text="Choose a dish").place(x=100,y=100)
# # popupMenu.grid(row = 2, column =1)
# popupMenu.place(x=100,y=120)
#
# # on change dropdown value
# def change_dropdown(*args):
#         print(tkvar.get())
#
#
# # link function to change dropdown
# tkvar.trace('w', change_dropdown)
#
# root.mainloop()
######################################################    third code    ##################################################
# st1="ALi"
# st2="Ahmed"
# if st1 == "" and st2 == "":
#     print("Yes are empty")
# elif st1=="ALi" or st2=="Esslam":
#     print("Yes")
# else:
#     print("No")
# f="88"
#
# print(type(f))
# # if type(f)=='str':
# #     print("Yes")
# # else:
# #     ptint("no")
# # in1=3
# # if in1.isalpha()==True:
# #     print("yes")
# # else:
# #     print("no")
#######################################             get size for files or directory                ######################3#######################
import cv2
import re
import mysql.connector
# import face_recognition
# import face_recognition
from tkinter import *
from tkinter import messagebox
from tkinter import font
# import pyQt4
# import face_recognition
import os
import numpy as nnn
from PIL import Image
# import face_recognition.api
import pickle
# root =Tk()
# root.geometry("700x430");
# root.title("New Window By Object Oiented")
# image = PhotoImage(file="register9.png")
# c = Canvas(root, bg='green')
# c.pack(fill=BOTH, expand=1)
# c.create_image(0, 0, image=image, anchor=NW)
#
# _flage="no"
# def trainimages():
#     global _flage
#     _flage = "okey"
#
#
# def clear_all_fields():
#     Entry_Name.delete(0,END)
#     Entry_Id.delete(0,END)
#     Entry_Level.delete(0,END)
#     Entry_Email.delete(0,END)
#
#
#
# def onsubmtting():
#     global _flage
#     a = _flage
#     # name=Entry_Name.get()
#     if (a == "okey"):
#         messagebox.showinfo("ok you acctually train "+name)
#     else:
#         messagebox.showinfo("you cant submit without taining image ")
#     #     return
#     # flage="no"
#     # messagebox.showinfo("images you must press key of train images")
#
# Entry_Name = Entry(root, width="50", justify=CENTER,bd=2).place(x=250, y=93)
# Entry_Id = Entry(root, width="50", justify=CENTER,bd=2).place(x=250, y=133)
# f=0
#
# # Clear_Fields = Button(root, text="Clear all fields", fg="white", bg="red", font="15", border=5,width=40, activebackground="blue", command=clear_all_fields).place(x=200, y=20)
# Imagetraining = Button(root, text="ImageTraining", fg="white", bg="red", font="15", border=5, width=15,activebackground="blue", command=trainimages).place(x=550, y=295)
# but_Submit = Button(root, text="Submit", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue",command=onsubmtting).place(x=350, y=350)
# root.mainloop()
###################################################             regular Expretion                  ##############################################
# txt="The rain Spain"
# x=re.search("^The.*Spain$",txt)
# if x:
#     print("Yes ,is mmatched")
# else:
#     print("No, not matched")
# text3="1234567899"
# text1="AZakaryagmail"
# text="AZakarya@gmailcom"
# x=re.findall('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>)',text)
# if x:
#     print("Yes ,is mmatched gmail")
# else:
#     print("No, This gmail not true")
#
# x=re.findall("[a-zA-Z]",text3)
# if x:
#     print("Yes , text3 is mmatched ")
# else:
#     print("No, text3 This not mmatched")

#################################################     to create aa file      ######################################
# file1=open("Attendance/AhmedFile.txt","w")
# file2=open("Attendance/Training.yml","w")
#
#
# try:
#     for i in range(50):
#         file1.write("this is line no %d\n"%i)
# finally:
#     file1.close()
#
# try:
#     for i in range(50):
#         file2.write("this is line no %d\n"%i)
# finally:
#     file2.close()


###################################          get the size of files or directories   ###########################

import os
b = os.path.getsize("New folder")
print(b)

#now i will try to remove the files from the New folder.

#print all files
# arr_files_from_data_set=os.listdir("New folder")
# # print(arr_files_from_data_set)
# for num in arr_files_from_data_set:
#     print(num+"\n")
# #delete all files
# arr_files_from_data_set=os.listdir("New folder")
# for x in arr_files_from_data_set:
#     os.remove("New folder/"+x)




############################# remove a content from a file    ##########################
# file1=open("Attendance/AliFile.txt","r+")
# file1.truncate(0)
# file1.close()

#################################################     to remove a file     ####################################

# if os.path.exists("nnnnnnnnnnew.txt"):
#     os.remove("nnnnnnnnnnew.txt")
#     print("the file is removed")
# else:
#     print("the file does not exist")

#################################################       to delete a file inside directory        ############################

# if os.path.exists("Attendance/attendancefile.txt"):
#     os.remove("Attendance/attendancefile.txt")
#     print("the file is removed")
# else:
#     print("the file does not exist")

################################################            to catch the all files        #####################################

# arr_files_from_data_set=os.listdir("Data_Set")
# print(arr_files_from_data_set)
# for num in arr_files_from_data_set:
#     print(num+"\n")

######### if i want delete the previous files in arry   ##########################
# for x in arr_files_from_data_set:
#     os.remove("Data_Set/"+x)


#################################################           to check if the directory is exists or no        ###########################

# path=os.path.join("c:\\","temp")
# if os.path.exists(path):
#     print(path+"  : exists")
#     if os.path.isdir(path):
#         print(path+" :is a directory .")


#################################################         to create a directory            ####################################

dir_name="MyDirectory"

# try:
#     os.mkdir(dir_name)
#     print("Durectory ",dir_name," Created .")
# except FileExistsError:
#     print("Directory ",dir_name,"  already exists")



#############################################          to rename directory          ############################################

# if os.path.exists(dir_name):
#     os.renames("MyDirectory","NewDirectory")

##############################################     to remove dir      #####################################################

# dir_name="NewDirectory"
#
# if os.path.exists(dir_name):
#     print(dir_name +"  : exists indeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeed")
#     os.removedirs(dir_name)
#     print(dir_name+" :is a removed .")


###########################################################################################################################

# path=r"C:\Users\Ali_Zakaria\Downloads\Compressed\MyProject"
# list=os.listdir(path)
# print(list)


###############################    Done by God's goodness      #################################################################




#####################################################   to make browse and quetion message box   ######################################

############################## this a browse and select the location and display it ####################
# import tkinter
# from tkinter import filedialog
# import os
#
# root = tkinter.Tk()
# # root.withdraw() #use to hide tkinter window
#
# def search_for_file_path ():
#     # currdir = os.getcwd() # catch the the path of project
#     currdir="Attendance"
#     tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
#     if len(tempdir) > 0:
#         print ("You chose: %s" % tempdir)
#     return tempdir
#
#
# but_Submit = Button(root, text="show file attendance", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue",command=search_for_file_path).place(x=50, y=50)
#
# # file_path_variable = search_for_file_path()
# # print ("\nfile_path_variable = ", file_path_variable)
# root.mainloop()
# # currdir = os.getcwd()
# # print(currdir)

##############################      here we open the path of attendance file to comfert the lecurer ####################################
# import tkinter
# from tkinter import messagebox,filedialog
#
# #initiate tinker and hide window
# main_win = tkinter.Tk()
# # main_win.withdraw()
#
# # main_win.overrideredirect(True)
# # main_win.geometry('0x0+0+0')
#
# # main_win.deiconify()
# # main_win.lift()
# # main_win.focus_force()
#
# #open file selector
# def pathattendance():
#     sourceFile = filedialog.askopenfilename(initialdir="C:/Users/Ali_Zakaria/Downloads/Compressed/MyProject/Attendance", title='Please select a directory')
#
# but_Submit = Button(main_win, text="show file attendance", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue",command=pathattendance).place(x=50, y=50)
#
# #close window after selection
# # main_win.destroy()
# main_win.mainloop()
# #print path
# # print(main_win.sourceFile )


###############################   yes or no message  #######################################
# import tkinter as tk
# from tkinter import messagebox
#
# root = tk.Tk()  # create window
#
# canvas1 = tk.Canvas(root, width=300, height=300)
# canvas1.pack()
#
#
# def ExitApplication():
#     MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
#                                        icon='warning')
#     if MsgBox == 'yes':
#         print("Yes")
#         root.destroy()
#     else:
#         print("No")
#         tk.messagebox.showinfo('Return', 'You will now return to the application screen')
#
#
# ExitApplication()
# # button1 = tk.Button(root, text='Exit Application', command=ExitApplication)
# # canvas1.create_window(150, 150, window=button1)
#
# root.mainloop()


###########################################       Done by God's goodness      ############################################################################

#code of recognition in speed
# import cv2,os
# from tkinter import *
# from tkinter import messagebox
# from tkinter import font
# # import pyQt4
# # import face_recognition
# import numpy as nnn
# import pickle
# import dlib
# import datetime
# import time
# import tkinter.ttk as ttk
# import tkinter.font as font
# import tkinter as tk
# from tkinter import Message, Text
# import shutil
# import csv
# import re
# from PIL import Image, ImageTk
# import pandas as pd
#
# recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
# recognizer.read("TrainingImageLabel\Trainner2.yml")
# harcascadePath = "haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(harcascadePath);
# cam = cv2.VideoCapture(0)
# font = cv2.FONT_HERSHEY_SIMPLEX
# col_names = ['Id', 'Name', 'Date', 'Time']
# attendance = pd.DataFrame(columns=col_names)
# while True:
#     ret, im = cam.read()
#     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(gray, 1.2, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
#         Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
#         if (conf < 50):
#             if (Id==1111):
#                 name="Ali_Al_Fateh"
#                 ts = time.time()
#                 date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#                 timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#                 attendance.loc[len(attendance)] = [Id, "Ali", date, timeStamp]
#             elif(Id==2222):
#                  name="salah"
#                  ts = time.time()
#                  date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#                  timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#                  attendance.loc[len(attendance)] = [Id, "salah", date, timeStamp]
#             elif(Id==3333):
#                 ts = time.time()
#                 date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#                 timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#                 attendance.loc[len(attendance)] = [Id, "Elmagico", date, timeStamp]
#                 name="El_Magico"
#
#         else:
#             name = 'Unknown'
#         if (conf > 75):
#             noOfFile = len(os.listdir("ImagesUnknown")) + 1
#             cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
#         cv2.putText(im, str(name), (x, y + h), font, 1, (250, 250, 250), 2)
#     attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
#     cv2.imshow('im', im)
#     if (cv2.waitKey(1) == ord('q')):
#         break
# ts = time.time()
# date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
# timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
# Hour, Minute, Second = timeStamp.split(":")
# fileName = "Attendance\Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
# attendance.to_csv(fileName, index=False)
# cam.release()
# cv2.destroyAllWindows()
# in1="على زكريا كامل"
# def welcom(n):
#     messagebox.showinfo("Inputs", "user name : " + n)
#
# x=input("enter a name ");
# welcom(x)
##################################    the Arabic is done why not run in the project            ######################################