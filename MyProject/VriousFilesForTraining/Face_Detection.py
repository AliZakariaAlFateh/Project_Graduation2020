import cv2,os
from  tkinter import*
import csv
import numpy as nnn
from tkinter import messagebox
main_window=Tk()
main_window.title("Face_Detection") #title for window.
main_window.geometry("700x400")
main_window.configure(background='green')
main_window.grid_rowconfigure(0,weight=1)
main_window.grid_columnconfigure(0,weight=1)
main_Label=Label(main_window,text="Attendance System By Face Recognation ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2")
main_Label.place(x=0,y=10)
#Face Detection for our project
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0)
input='true'

#the new part to make recognation .
# recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
# harcascadePath = "haarcascade_frontalface_default.xml"
# detector = cv2.CascadeClassifier(harcascadePath)
def FaceDetection():
    while (True):
        ret,img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("Face Detection , press q to close the camera .", img)
        if (cv2.waitKey(1) == ord('q')):
            break;

    cam.release();
    cv2.destroyAllWindows();
b1=Button(main_window,text="Check_Face",fg="white",bg="red",font="15",border=5,width=15,command=FaceDetection,activebackground="blue")
b1.place(x=40,y=80)
b2=Button(main_window,text="Close",fg="white",bg="red",font="15",border=5,width=15,activebackground="blue",command=main_window.destroy)
b2.place(x=40,y=130)
main_window.mainloop()