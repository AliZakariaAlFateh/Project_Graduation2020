import cv2,os
from  tkinter import*
from tkinter import font
from tkinter import messagebox
# import pyQt4
# import face_recognition
import numpy as nnn
from PIL import Image
# import face_recognition.api
import pickle
import dlib
#detector = dlib.get_frontal_face_detector()

main_window=Tk()
main_window.title("Face_Detection") #title for window.
main_window.geometry("700x400")
main_window.configure(background='green')
main_window.grid_rowconfigure(0,weight=1)
main_window.grid_columnconfigure(0,weight=1)
# main_window.geometry("700x400")
# c=Canvas(main_window)
# image=PhotoImage(file="Flag.png")
# c.pack(expand=1)
# c.create_image(0,0,image=image,anchor=NW)
main_Label=Label(main_window,text="Attendance System By Face Recognation ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=10)

#Face Detection for our project
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0)
input='true'
input1=StringVar()
def FaceDetection():
    # font=cv2.cv2.InitFont(cv2.cv2.CV_FONT_HERSHEY_SIMPLEX,1,.5,0,2,1) #Creates a font.
    while (True):
        ret,img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # cv2.cv2.PutText(cv2.cv2.fromarray(img),"UnKnown_Face",(x,y+h+20),font,(0,0,255)) #Draws a text.
        # cv2.waitKeyEx(80)
        cv2.imshow("Face Detection , press q to close the camera .", img)
        if (cv2.waitKey(1) == ord('q')):
            break;

    cam.release();
    cv2.destroyAllWindows();
input1=StringVar()
input2=StringVar()


Input_Register_Lecturer_user=StringVar()
Input_Register_Lecturer_password=StringVar()
Input_Register_Lecturer_email=StringVar()
def Registeration_Lecturer():
    window_Registeration=Tk();
    window_Registeration.title("Regiseter Your Information");
    window_Registeration.geometry("700x400");
    window_Registeration.configure(background='green')
    window_Registeration.grid_rowconfigure(0, weight=1)
    window_Registeration.grid_columnconfigure(0, weight=1)
    Label_Header=Label(window_Registeration,text="Registeration_Lecturer ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=10)
    Label_User=Label(window_Registeration,text="Please,Enter user name: ",bg="yellow",relief="solid",fg="green",font=("arial",12,"bold"),width="20",height="1").place(x=0,y=90)
    Label_Password = Label(window_Registeration,text="Please,Enter Password: ",bg="yellow",relief="solid",fg="green",font=("arial", 12, "bold"),width="20",height="1").place(x=0,y=130)
    Label_Email = Label(window_Registeration,text="Please,Enter Email: ",bg="yellow",relief="solid",fg="green",font=("arial", 12, "bold"),width="20",height="1").place(x=0,y=170)
    Entry_User = Entry(window_Registeration, textvariable=Input_Register_Lecturer_user,width="50",justify=CENTER).place(x=250,y=93)
    Entry_Password = Entry(window_Registeration,show="*", textvariable=Input_Register_Lecturer_password,width="50",justify=CENTER).place(x=250,y=133)
    Entry_Email = Entry(window_Registeration, show="*", textvariable=Input_Register_Lecturer_email, width="50",justify=CENTER).place(x=250, y=173)
    but_Login = Button(window_Registeration, text="Submit", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue", command=Show_Report).place(x=280, y=210)


Input_Login_Lecturer_user=StringVar()
Input_Login_Lecturer_password=StringVar()

def Window_Login_Lecturer():
    window_login=Tk();
    window_login.title("Regiseter Your Information");
    window_login.geometry("700x400");
    window_login.configure(background='green')
    window_login.grid_rowconfigure(0, weight=1)
    window_login.grid_columnconfigure(0, weight=1)
    Label_Header=Label(window_login,text="Login ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=10)
    Label_User=Label(window_login,text="Please,Enter user name: ",bg="yellow",relief="solid",fg="green",font=("arial",12,"bold"),width="20",height="1").place(x=0,y=90)
    Label_Password = Label(window_login,text="Please,Enter Password: ",bg="yellow",relief="solid",fg="green",font=("arial", 12, "bold"),width="20",height="1").place(x=0,y=130)
    Entry_User = Entry(window_login, textvariable=Input_Login_Lecturer_user,width="50",justify=CENTER).place(x=250,y=93)
    Entry_Password = Entry(window_login,show="*", textvariable=Input_Login_Lecturer_password,width="50",justify=CENTER).place(x=250,y=133)
    but_Login = Button(window_login, text="Submit", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue", command=Show_Report).place(x=280, y=210)

# global Input_Register_Student_name
# global Input_Register_Student_id
# global Input_Register_Student_level
# global Input_Register_Student_email
Input_Register_Student_name=StringVar()
Input_Register_Student_id=StringVar()
Input_Register_Student_level=StringVar()
Input_Register_Student_email=StringVar()

global in2
global inp

def wellcom():
    in2 ="nn"
    inp="pp"
    # global in2
    # in2= Input_Register_Student_name.get()
    # global inp
    # inp= Input_Register_Student_id.get()
    messagebox.showinfo("Inputs","user name : "+in2+"\n"+"passsword : "+inp)

# Input_Register_Student_name="kkkkkkkkkkkkk"
# Input_Register_Student_id=888888

def Window_Registeration_student():
    Window_Registeration=Tk();
    Window_Registeration.title("Regiseter Your Information");
    Window_Registeration.geometry("700x400");
    Window_Registeration.configure(background='green',relief="solid")
    Window_Registeration.grid_rowconfigure(0, weight=1)
    Window_Registeration.grid_columnconfigure(0, weight=1)
    Label_Header=Label(Window_Registeration,text="Student Registeration ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=10)
    var_1=StringVar()
    var_2=StringVar()
    var_3=StringVar()
    var_4=StringVar()

    Label_Name=Label(Window_Registeration,text="Please,Enter name: ",bg="yellow",relief="solid",fg="green",font=("arial",12,"bold"),width="20",height="1").place(x=0,y=90)
    Label_Id = Label(Window_Registeration,text="Please,Enter Id: ",bg="yellow",relief="solid",fg="green",font=("arial", 12, "bold"),width="20",height="1").place(x=0,y=130)
    Label_Level=Label(Window_Registeration,text="Please,Enter Level: ",bg="yellow",relief="solid",fg="green",font=("arial",12,"bold"),width="20",height="1").place(x=0,y=170)
    Label_Email = Label(Window_Registeration,text="Please,Enter Email: ",bg="yellow",relief="solid",fg="green",font=("arial", 12, "bold"),width="20",height="1").place(x=0,y=210)
    Entry_Name = Entry(Window_Registeration, textvariable=var_1,width="50",justify=CENTER).place(x=250,y=93)
    Entry_Id = Entry(Window_Registeration, textvariable=var_2,width="50",justify=CENTER).place(x=250,y=133)
    Entry_Level = Entry(Window_Registeration, textvariable=var_3,width="50",justify=CENTER).place(x=250,y=173)
    Entry_Email = Entry(Window_Registeration, textvariable=var_4,width="50",justify=CENTER).place(x=250,y=213)
    Label_Take_Photo=Label(Window_Registeration,text="You must take a photo before submitting",bg="yellow",relief="solid",fg="green",font=("arial",12,"bold"),width="30",height="1").place(x=0,y=300)
    but_Take_Photo = Button(Window_Registeration, text="Take_Photo", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue", command=GenerateDataSet).place(x=350, y=295)
    def det_data():
        messagebox.showinfo("Inputs","user: "+var_1.get()+"\n"+"pass : "+var_2.get())
    but_Submit = Button(Window_Registeration, text="Submit", fg="white", bg="red", font="15", border=5, width=15,activebackground="blue", command=det_data).place(x=280, y=350)



def getvalue():
        in2= Input_Register_Student_name.get()
        inp= Input_Register_Student_id.get()
        messagebox.showinfo("Inputs", "user name : " + in2 + "\n" + "passsword : " + inp)

def GenerateDataSet():
    in1 =Input_Register_Student_id.get()
    samplnum=0
    while (True):
        ret,img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            samplnum=samplnum+1
            cv2.imwrite("Data_Set/User."+str(in1)+"."+str(samplnum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.waitKey(100)
        cv2.imshow("Generate Photos.", img)
        cv2.waitKey(1)
        if(samplnum==100):
            break;


    cam.release();
    cv2.destroyAllWindows();


def Show_Report():
    Window_Report=Tk();
    Window_Report.title("Regiseter Your Information");
    Window_Report.geometry("700x400");
    Window_Report.configure(background='green',relief="solid")
    Window_Report.grid_rowconfigure(0, weight=1)
    Window_Report.grid_columnconfigure(0, weight=1)
    but_Detection = Button(Window_Report, text="Detection _Photo", fg="white", bg="red", font="15", border=5, width=20, command=FaceDetection, activebackground="blue")
    but_Detection.place(x=260, y=140)
    Label_Header=Label(Window_Report,text="Report For Attendance ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=10)
    but_Registeration = Button(Window_Report, text="Show _Report", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue", command=wellcom).place(x=280, y=250)
def Team():
    Window_Team=Tk();
    Window_Team.title("Regiseter Your Information");
    Window_Team.geometry("700x400");
    Window_Team.configure(background='green',relief="solid")
    Window_Team.grid_rowconfigure(0, weight=1)
    Window_Team.grid_columnconfigure(0, weight=1)
    Label_Header=Label(Window_Team,text="Our Team  ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=10)
    Label_1=Label(Window_Team,text="Ahmed Ali Abd-El Rasheid",bg="blue",relief="solid",fg="white",font=("times",20,"italic bold underline"),width="40",height="1").pack(fill=BOTH,padx=0,pady=13)
    Label_2 = Label(Window_Team,text="Ahmed Yousef Fathey",bg="blue",relief="solid",fg="white",font=("times",20,"italic bold underline"),width="40",height="1").pack(fill=BOTH,padx=0,pady=16)
    Label_3=Label(Window_Team,text="Ali Zakaria Kamel Thabet",bg="blue",relief="solid",fg="white",font=("times",20,"italic bold underline"),width="40",height="1").pack(fill=BOTH,padx=0,pady=22)
    Label_4 = Label(Window_Team,text="Omar Abd-El Salam Ebrahiem",bg="blue",relief="solid",fg="white",font=("times",20,"italic bold underline"),width="40",height="1").pack(fill=BOTH,padx=0,pady=25)

but_Registeration_Lecturer=Button(main_window,text="Registeration_Lecturer",fg="white",bg="red",font="15",border=5,relief=GROOVE,bd=5,width=20,activebackground="blue",command=Registeration_Lecturer)
but_Registeration_Lecturer.place(x=50,y=150)
but_Login_Lecturer=Button(main_window,text="Login_Lecturer",fg="white",bg="red",font="15",border=5,relief=GROOVE,bd=5,width=20,activebackground="blue",command=Window_Login_Lecturer)
but_Login_Lecturer.place(x=270,y=150)
but_Registeration_Student=Button(main_window,text="Registeratio_Student",fg="white",bg="red",font="15",border=5,width=20,activebackground="blue",command=Window_Registeration_student)
but_Registeration_Student.place(x=270,y=200)
but_Close=Button(main_window,text="Close",fg="white",bg="red",font="15",border=5,width=20,activebackground="blue",relief=GROOVE,bd=5,command=main_window.destroy)
but_Close.place(x=270,y=250)
but_Team=Button(main_window,text="Project_Team",fg="white",bg="red",font="15",border=5,width=20,activebackground="blue",command=Team)
but_Team.place(x=270,y=300)
Entry_Id = Entry(main_window, textvariable=Input_Register_Student_id, width="50").place(x=250, y=300)
main_window.mainloop()