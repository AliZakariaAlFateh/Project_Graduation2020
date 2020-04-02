import cv2,os
from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import Image
from tkinter import messagebox,filedialog
# import pyQt4
# import face_recognition
import numpy as nnn
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
# from PIL import Image
# import face_recognition.api
# import pickle
# import dlib
class AfterSubmittingAdminclass():
    def show_frame(self):
        Controlwindow = Tk();
        Controlwindow.title("Regiseter Your Information");
        Controlwindow.geometry("700x400");
        Controlwindow.resizable(width=False, height=False)
        Controlwindow.configure(background='green', relief="solid")
        Controlwindow.grid_rowconfigure(0, weight=1)
        Controlwindow.grid_columnconfigure(0, weight=1)
        image = PhotoImage(file="BackGroundImages\Capture1.png")
        c = Canvas(Controlwindow, bg='green')
        c.pack(fill=BOTH, expand=1)
        c.create_image(0, 0, image=image, anchor=NW)
        var_level=StringVar()
        ######################################        to select subject      ###########################################
        global Select_Subject
        Select_Subject = StringVar(Controlwindow)
        # Dictionary with options
        choices = {'C++', 'Php', 'C#', 'Java', 'fortrn', 'Python'}

        Select_Subject.set('Select_Subject')  # set the default option
        popupMenu = OptionMenu(Controlwindow, Select_Subject, *choices)
        # Label(Controlwindow, text="Choose a subject").place(x=100, y=100)
        popupMenu.place(x=240, y=140)
        # # on change dropdown value
        # def change_dropdown_subject(*args):
        #     print(Select_Subject.get())
        # # link function to change dropdown
        # Select_Subject.trace('w', change_dropdown_subject)

        #######################################          to select level      ##########################################
        global SelectLevel
        SelectLevel = StringVar(Controlwindow)
        # Dictionary with options
        choices = {1, 2, 3, 4}
        SelectLevel.set('Select_Level')  # set the default option
        popupMenu = OptionMenu(Controlwindow, SelectLevel, *choices)
        # Label(Controlwindow, text="Choose a level").place(x=100, y=100)
        popupMenu.place(x=250, y=90)
        # # on change dropdown value
        # def change_dropdown_level(*args):
        #     print(SelectLevel.get())
        #
        # # link function to change dropdown
        # SelectLevel.trace('w', change_dropdown_level)
        global FlageBeforeTraining
        FlageBeforeTraining=False
        def PathAttendence():
            sourceFile = filedialog.askopenfilename(initialdir="C:/Users/Ali_Zakaria/Downloads/Compressed/MyProject/Attendance", title='Please select a directory')
            # import FinalProject_LogIn_Admin
            # name=FinalProject_LogIn_Admin.GUI_Object_Oriented_LogInAdmin().show_frame().getDataFromLogin()
            # messagebox.showinfo("message","Mr : kkk ,"+"The report has not prepared yet . " )
        def BackToHomePage():
            if os.path.exists("FinalProject_Main.py"):
                Controlwindow.destroy()
                import FinalProject_Main
            else:
                messagebox.showerror("error","the file not found , Please ceate new one ,and make its operaation")
                return

        def Recognition_Faces():
            global FlageBeforeTraining
            flage=1
            if Select_Subject.get() == 'Select_Subject':
                flage=0
            if SelectLevel.get() == 'Select_Level':
                flage=0
            if flage==0:
                messagebox.showinfo("message", "You must select the level, and the subject .")
            if FlageBeforeTraining==False:
                messagebox.showinfo("message","You must delete all file in attendence,until you can recognise the attendence file easily")
            else:
                FlageBeforeTraining =False
                level=SelectLevel.get()
                Subject=Select_Subject.get()
                import Final_Project_Face_Recognition
                Final_Project_Face_Recognition.FaceRcognitionClass().Recognition_Faces(level,Subject)

        def DeleteAllFiles():
            global FlageBeforeTraining
            FlageBeforeTraining = True
            arr_files_from_data_set = os.listdir("Attendance")
            for x in arr_files_from_data_set:
                os.remove("Attendance/" + x)

        # pb = Progressbar(Controlwindow, orient="horizontal", length=200, mode="determinate", maximum=100)
        # pb.place(x=450, y=350)
        but_Detection = Button(Controlwindow, text="Rcognition_Images", fg="white", bg="red", font="15", border=5, width=20, command=Recognition_Faces, activebackground="blue")
        but_Detection.place(x=260, y=190)
        Label_Header = Label(c, text="Report For Attendance ", bg="yellow", fg="blue",font=("times", 20, "italic bold underline"), width="50", height="2").pack(fill=BOTH,padx=0, pady=0)
        but_Report = Button(Controlwindow, text="Show _Report", fg="white", bg="red", font="15", border=5,width=15, activebackground="blue", command=PathAttendence).place(x=280, y=250)
        HomePage_but = Button(Controlwindow, text="Back to home page", fg="white", bg="red", font="15", border=5, width=15,activebackground="blue", command=BackToHomePage).place(x=280, y=300)
        but_delete_files = Button(Controlwindow, text="Delete all files in Attendance", fg="white", bg="red", font="15", border=5, width=25, activebackground="blue", command=DeleteAllFiles).place(x=410, y=115)
        Label_Level = Label(Controlwindow, text="Please,select a lvel ",width=20, bg="yellow", fg="blue",font=("times", 15, "italic bold underline"),height="1").place(x=0, y=90)
        Label_Subject = Label(Controlwindow, text="Please , Select a subhect ", width=20, bg="yellow", fg="blue", font=("times", 15, "italic bold underline"), height="1").place(x=0, y=140)
        but_Close=Button(Controlwindow,text="Close",fg="white",bg="red",font="15",border=5,width=20,activebackground="blue",relief=GROOVE,bd=5,command=Controlwindow.destroy)
        but_Close.place(x=260,y=350)
        # Entry_Level = Entry(Controlwindow, textvariable=var_level, width="50", justify=CENTER).place(x=250, y=90)
        Controlwindow.mainloop()

# AfterSubmittingAdminclass().show_frame()