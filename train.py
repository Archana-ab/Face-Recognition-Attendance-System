from cProfile import label
from cgitb import text
from email.mime import image
from importlib.resources import path
from textwrap import fill
from tkinter import*
from tkinter import ttk
from tkinter.tix import Select
from turtle import update, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lb1 = Label(self.root, text="TRAIN DATA SET", font=("time new roman", 35, "bold"), bg="black", fg="red")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"F:\face recognition\Images\img16.jpeg")
        img_top.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb3 = Label(self.root, image=self.photoimg_top)
        f_lb3.place(x=0, y=55, width=1530, height=325)

        #Button
        b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("time new roman",30,"bold"),bg="yellow",fg="red")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom = Image.open(r"F:\face recognition\Images\img17.jpg")
        img_bottom.resize((1530,325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb3 = Label(self.root, image=self.photoimg_bottom)
        f_lb3.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # train classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training DataSet Completed!")











if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()