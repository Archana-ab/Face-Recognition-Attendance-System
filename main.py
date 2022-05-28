from cProfile import label
from email.mime import image
from tkinter import*
from tkinter import ttk
import tkinter
from turtle import width
from PIL import Image,ImageTk
from student import Student
from tkinter import messagebox
from tkinter.tix import Select
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        img1=Image.open(r"F:\face recognition\Images\img1.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=0,y=0,width=500,height=130)

        img2=Image.open(r"F:\face recognition\Images\img2.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb2=Label(self.root,image=self.photoimg2)
        f_lb2.place(x=500,y=0,width=500,height=130)

        img3=Image.open(r"F:\face recognition\Images\img3.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lb3=Label(self.root,image=self.photoimg3)
        f_lb3.place(x=1000,y=0,width=550,height=130)

        #bg image
        img4=Image.open(r"F:\face recognition\Images\img10.jpg")
        img4=img4.resize((1530,660),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=660)

        title_lb1=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        #student button
        img5=Image.open(r"F:\face recognition\Images\img7.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=300,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=300,y=300,width=220,height=40)

        #Detect face button 
        img6=Image.open(r"F:\face recognition\Images\img9.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=600,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=600,y=300,width=220,height=40)

        #Attendence button 
        img7=Image.open(r"F:\face recognition\Images\img4.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=900,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=900,y=300,width=220,height=40)

        #Train Data  button 
        img8=Image.open(r"F:\face recognition\Images\img8.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=300,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=300,y=580,width=220,height=40)

        #Photos button 
        img9=Image.open(r"F:\face recognition\Images\img6.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=600,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=600,y=580,width=220,height=40)

        #Exit button 
        img10=Image.open(r"F:\face recognition\Images\img11.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.iExit)
        b1.place(x=900,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=900,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure,you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


    #functions of button
    #student
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    #Train Data set
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    #Face recognition
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    
    #Attendance Function
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)






if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
