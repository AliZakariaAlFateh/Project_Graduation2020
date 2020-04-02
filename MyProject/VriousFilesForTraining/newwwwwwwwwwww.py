from  tkinter import*
from PIL import ImageTk,Image
import turtle
from tkinter import font
main_window=Tk()
main_window.title("Face_Detection") #title for window.
main_window.geometry("750x400")
# mm=turtle.Turtle()
# main_window=turtle.Screen()
# main_window.bgpic("FaceDetection.png")
image=PhotoImage(file="FaceDetection.png")
c=Canvas(main_window,bg='green')
c.pack(fill=BOTH,expand=1)
c.create_image(0,0,image=image,anchor=NW)
main_Label=Label(c,text="Attendance System By Face Recognation ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=0)
but_Team=Button(c,text="Project_Team",fg="white",bg="red",font="15",border=5,width=20,activebackground="blue").pack(padx=100,pady=20)
main_window.mainloop()