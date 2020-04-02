import cv2
from  tkinter import*
from tkinter import messagebox
main_window=Tk()
main_window.title("Face_Detection") #title for window.
main_window.geometry("400x400")
def p1():
    #messagebox.showinfo("Al_Fateh","Face_Recognation_Project . \n  Hello Eng/Ali .")
    messagebox.showerror("error message","something error")

input1=StringVar()
input2=StringVar()
def catchInputFields():
    in1=input1.get()
    in2=input2.get()

    # concat_n1_n2=in1+in2
    messagebox.showinfo("Inputs","user name : "+in1+"\n"+"passsword : "+in2) #this function just take two inputs


b1=Button(main_window,text="Show_Data",fg="white",bg="red",font="15",border=5,width=15,command=p1,activebackground="blue")
b1.place(x=40,y=80)
b2=Button(main_window,text="Show_DayReport",fg="white",bg="red",font="15",border=8,width=15,command=catchInputFields)
b2.place(x=40,y=120)
text_1=Entry(main_window,textvariable=input1,width="50")
text_2=Entry(main_window,textvariable=input2,width="50")
label_text1=Label(main_window,text="Enter Your Name :       ")
label_text2=Label(main_window,text="Enter your password : ")
main_Label=Label(main_window,text="LogIn",bg="yellow",fg="green",font="15",width="50",height="1")
main_Label.place(x=0)
label_text1.place(x=0,y=25)
label_text2.place(x=0,y=45)
text_1.place(x=70,y=25)
text_2.place(x=70,y=45)



# _text_1=Entry(main_window,text="Enter Your Name :       ")
# _text_1.place(x=30,y=145)
# _text_1.focus()
main_window.mainloop() #to show the window.

