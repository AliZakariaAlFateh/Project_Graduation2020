import cv2,os
from tkinter import *
from tkinter import messagebox
from tkinter import font
# import pyQt4
# import face_recognition
import numpy as nnn
from PIL import Image
# import face_recognition.api
import pickle
import dlib
class GUI_Object_Oriented():
    _flage = "no"

    root=Tk()
    root.geometry("700x430");
    root.title("New Window By Object Oiented")
    image = PhotoImage(file="register9.png")
    c = Canvas(root, bg='green')
    c.pack(fill=BOTH, expand=1)
    c.create_image(0, 0, image=image, anchor=NW)

    var_name_1 = StringVar()
    var_id_2 = StringVar()
    var_level_3 = StringVar()
    var_email_4 = StringVar()
    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam = cv2.VideoCapture(0)
    def GenerateDataSet():
        in1 = var_name_1.get()
        level = var_level_3.get()
        samplnum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceDetect.detectMultiScale(gray, 1.3, 5);
            for (x, y, w, h) in faces:
                samplnum = samplnum + 1
                cv2.imwrite("Data_Set"+level+"/User." + str(in1) + "." + str(samplnum) + ".jpg", gray[y:y + h, x:x + w])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.waitKey(100)
            cv2.imshow("Generate Photos.", img)
            cv2.waitKey(1)
            if (samplnum == 100):
                break;

        cam.release();
        cv2.destroyAllWindows();

    def welcom():
        in1 = var_name_1.get()
        in2 = var_id_2.get()
        in3 = var_level_3.get()
        in4 = var_email_4.get()
        messagebox.showinfo("Inputs", "user name : " + in1+"\n"+"ID : "+in2+"\n"+"level : "+in3+"\n"+"email : "+in4)


    def trainimages():
        global _flage
        _flage="okey"


    def onsubmtting():
        global _flage
        a=_flage
        if(a == "okey"):
            messagebox.showinfo("ok you acctually train ")
        else:
            messagebox.showinfo("you cant submit without taining image ")
        #     return
        # flage="no"
        # messagebox.showinfo("images you must press key of train images")

    Label_Name = Label(root, text="Please,Enter name: ", bg="yellow", relief="solid", fg="green",font=("arial", 12, "bold"), width="20", height="1").place(x=0, y=90)
    Label_Id = Label(root, text="Please,Enter Id: ", bg="yellow", relief="solid", fg="green",font=("arial", 12, "bold"), width="20", height="1").place(x=0, y=130)
    Label_Level = Label(root, text="Please,Enter Level: ", bg="yellow", relief="solid", fg="green",font=("arial", 12, "bold"), width="20", height="1").place(x=0, y=170)
    Label_Email = Label(root, text="Please,Enter Email: ", bg="yellow", relief="solid", fg="green",font=("arial", 12, "bold"), width="20", height="1").place(x=0, y=210)
    Entry_Name = Entry(root, textvariable=var_name_1, width="50", justify=CENTER,bd=2).place(x=250, y=93)
    Entry_Id = Entry(root, textvariable=var_id_2, width="50", justify=CENTER,bd=2).place(x=250, y=133)
    Entry_Level = Entry(root, textvariable=var_level_3, width="50", justify=CENTER,bd=2).place(x=250, y=173)
    Entry_Email = Entry(root, textvariable=var_email_4, width="50", justify=CENTER,bd=2).place(x=250, y=213)
    Label_Take_Photo = Label(root, text="You must take a photo before submitting", bg="yellow",relief="solid", fg="green", font=("arial", 12, "bold"), width="30", height="1").place(x=0, y=300)
    but_Take_Photo = Button(root, text="Take_Photo", fg="white", bg="red", font="15", border=5,width=15, activebackground="blue", command=GenerateDataSet).place(x=350, y=295)
    Imagetraining = Button(root, text="ImageTraining", fg="white", bg="red", font="15", border=5,width=15, activebackground="blue",command=trainimages).place(x=550, y=295)
    but_Submit = Button(root, text="Submit", fg="white", bg="red", font="15", border=5, width=15,activebackground="blue",command=welcom).place(x=350, y=350)
    but_Close = Button(root, text="Close", fg="white", bg="red", font="15", border=5, width=40,activebackground="blue", relief=GROOVE, bd=5, command=root.destroy)
    but_Close.place(x=200, y=400)

    root.mainloop()
GUI_Object_Oriented()

