import cv2,os
from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import Image
# import pyQt4
# import face_recognition
import numpy as nnn
# from PIL import Image
# import face_recognition.api
# import pickle
# import dlib
class Class_LogInAdmin():
    def show_frame(self):
        window_login=Tk();
        window_login.title("Regiseter Your Information");
        window_login.geometry("600x390");
        window_login.resizable(width=False, height=False)
        Input_Login_Lecturer_user= StringVar()
        Input_Login_Lecturer_password= StringVar()
        window_login.configure(background='green')
        window_login.grid_rowconfigure(0, weight=1)
        window_login.grid_columnconfigure(0, weight=1)
        image = PhotoImage(file="BackGroundImages\Registeration_Photo.png")
        c = Canvas(window_login, bg='green')
        c.pack(fill=BOTH, expand=1)
        c.create_image(0, 0, image=image, anchor=NW)
        def BackToHomePage():
            if os.path.exists("FinalProject_Main.py"):
                window_login.destroy()
                import FinalProject_Main
            else:
                messagebox.showerror("error","the file not found , Please ceate new one ,and make its operaation")
                return
        def After_Submitting():
            if os.path.exists("Final_Project_AfterSubmitting_Admin.py"):
                name=Input_Login_Lecturer_user.get()
                password=Input_Login_Lecturer_password.get()
                window_login.destroy()
                import Final_Project_AfterSubmitting_Admin
                Final_Project_AfterSubmitting_Admin.AfterSubmittingAdminclass().show_frame()

            else:
                 messagebox.showerror("error", "the file not found , Please ceate new one ,and make its operaation")
                 return

        # def getDataFromLogin():
        #     name=Input_Login_Lecturer_user.get()
        #     password=Input_Login_Lecturer_password.get()
        #     return name
        Label_Header=Label(c,text="Login ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=0)
        Label_User=Label(window_login,text="Please,Enter user name: ",bg="yellow",relief="solid",fg="green",font=("arial",12,"bold"),width="20",height="2").place(x=0,y=90)
        Label_Password = Label(window_login,text="Please,Enter Password: ",bg="yellow",relief="solid",fg="green",font=("arial", 12, "bold"),width="20",height="2").place(x=0,y=155)
        Entry_User = Entry(window_login, textvariable=Input_Login_Lecturer_user,width="50",bg="#eee",font=("arial",13,"bold"),justify=CENTER,bd=5).place(x=250,y=93)
        Entry_Password = Entry(window_login,show="*", textvariable=Input_Login_Lecturer_password,width="50",bg="#eee",font=("arial",13,"bold"),justify=CENTER,bd=5).place(x=250,y=158)
        but_Login = Button(window_login, text="Submit", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue",command=After_Submitting).place(x=240, y=210)
        HomePage_but = Button(window_login, text="Back to home page", fg="white", bg="red", font="15", border=5, width=15,activebackground="blue", command=BackToHomePage).place(x=240, y=265)
        window_login.mainloop()
# Class_LogInAdmin().show_frame()